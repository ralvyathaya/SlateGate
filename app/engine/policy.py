"""
Deterministic Content Greenlight Decision Policy Engine.
Enforces strict hierarchical decision rules with evidence verification:
- RED: Expired/conflicting/missing territory rights OR missing/failed master video QC.
- AMBER: Valid rights and master video, but missing/failed subtitle, artwork, metadata, or deliverable.
- GREEN: 100% of required checks passed with valid evidence.
- Incomplete/missing data must NEVER produce GREEN.
"""

from datetime import date, datetime
from typing import Any, Dict, List, Optional, Tuple
from app.models.response import CheckItem, DecisionEnum, GreenlightResponse


def parse_date(d: Any) -> Optional[date]:
    """Helper to convert string or date object to date."""
    if isinstance(d, date):
        return d
    if isinstance(d, str):
        try:
            return datetime.strptime(d[:10], "%Y-%m-%d").date()
        except ValueError:
            return None
    return None


def get_owner_and_action(category: str, territory: str, issue: str) -> Tuple[str, str]:
    """Map check category to operational team owner and recommended next action."""
    cat_lower = category.lower()
    if cat_lower == "rights":
        return (
            "Rights & Licensing",
            f"Confirm or renew FAST distribution license for {territory} before launch."
        )
    elif "master" in cat_lower or cat_lower == "master_video":
        return (
            "Technical Operations",
            f"Ingest and QC conform broadcast master video in {territory} ({issue})."
        )
    elif "sub" in cat_lower or cat_lower == "subtitle":
        return (
            "Localization",
            f"Ingest and QA localized subtitle track for {territory} ({issue})."
        )
    elif "art" in cat_lower or "poster" in cat_lower or "banner" in cat_lower:
        return (
            "Creative Operations",
            f"Deliver compliant key art / promotional assets for {territory} ({issue})."
        )
    elif "meta" in cat_lower or cat_lower == "metadata":
        return (
            "Content Operations",
            f"Submit complete localized metadata and synopsis package for {territory}."
        )
    else:
        return (
            "Operations & Delivery",
            f"Fulfill mandatory delivery specification for {territory} ({issue})."
        )


def evaluate_greenlight(
    title_id: str,
    launch_date: date,
    territories: List[str],
    platform: str,
    raw_data: Dict[str, Any],
    tool_trace: List[str],
    data_mode: str,
) -> GreenlightResponse:
    """
    Pure deterministic evaluation of rights and asset readiness.
    """
    checks: List[CheckItem] = []
    
    title_meta = raw_data.get("title")
    rights_list = raw_data.get("rights", [])
    deliverables_list = raw_data.get("deliverables", [])
    assets_list = raw_data.get("assets", [])

    # Missing Title check
    if not title_meta:
        for t in territories:
            checks.append(
                CheckItem(
                    category="catalog",
                    territory=t,
                    status="fail",
                    reason=f"Title '{title_id}' was not found in catalog database.",
                    evidence=[f"catalog:missing:{title_id}"],
                    owner="Catalog Management",
                    next_action=f"Register '{title_id}' in catalog database before auditing.",
                )
            )
        return GreenlightResponse(
            decision=DecisionEnum.RED,
            summary=f"Launch blocked: Title '{title_id}' not found in catalog.",
            checks=checks,
            tool_trace=tool_trace,
            data_mode=data_mode,
            passed_count=0,
            failed_count=len(checks),
            total_count=len(checks),
            title_id=title_id,
            launch_date=launch_date.isoformat(),
            territories=territories,
            platform=platform,
        )

    # 1. RIGHTS CHECK PER TERRITORY
    has_rights_failure = False
    for t in territories:
        # Find matching rights window for this territory & platform
        matched_rights = [
            r for r in rights_list
            if r.get("territory") == t and str(r.get("platform", "")).upper() == platform.upper()
        ]

        if not matched_rights:
            has_rights_failure = True
            checks.append(
                CheckItem(
                    category="rights",
                    territory=t,
                    status="fail",
                    reason=f"No {platform} rights record found for territory {t}.",
                    evidence=[f"rights:{title_id}:{t}:missing"],
                    owner="Rights & Licensing",
                    next_action=f"Acquire or ingest {platform} distribution rights for {t}.",
                )
            )
            continue

        # Check each window
        active_window_found = False
        conflict_detected = False
        expired_contract = ""
        conflict_notes = ""

        for rw in matched_rights:
            start = parse_date(rw.get("start_date"))
            end = parse_date(rw.get("end_date"))
            has_conflict = bool(rw.get("has_conflict", 0))
            contract_ref = rw.get("contract_ref", f"contract-{title_id}-{t.lower()}")

            if has_conflict:
                conflict_detected = True
                conflict_notes = rw.get("conflict_notes", "Contract conflict flagged")
                expired_contract = contract_ref
                break

            if start and end:
                if start <= launch_date <= end:
                    active_window_found = True
                    checks.append(
                        CheckItem(
                            category="rights",
                            territory=t,
                            status="pass",
                            reason=f"Active {platform} rights window valid ({start} to {end}).",
                            evidence=[f"rights:{title_id}:{t}:{contract_ref}"],
                            owner="Rights & Licensing",
                            next_action="Rights confirmed; maintain contract record.",
                        )
                    )
                    break
                elif launch_date > end:
                    expired_contract = contract_ref
                elif launch_date < start:
                    expired_contract = contract_ref

        if conflict_detected:
            has_rights_failure = True
            checks.append(
                CheckItem(
                    category="rights",
                    territory=t,
                    status="fail",
                    reason=f"Rights conflict detected in {t}: {conflict_notes}.",
                    evidence=[f"rights:{title_id}:{t}:{expired_contract}:conflict"],
                    owner="Rights & Licensing",
                    next_action=f"Resolve territory exclusivity conflict for {t}.",
                )
            )
        elif not active_window_found:
            has_rights_failure = True
            checks.append(
                CheckItem(
                    category="rights",
                    territory=t,
                    status="fail",
                    reason=f"No active, conflict-free {platform} rights window was found.",
                    evidence=[f"rights:{title_id}:{t}:{expired_contract or 'none'}"],
                    owner="Rights & Licensing",
                    next_action=f"Confirm or renew {platform} rights for {t} before launch.",
                )
            )

    # 2. DELIVERABLES & ASSETS CHECK PER TERRITORY
    has_master_failure = False
    has_supporting_failure = False

    for t in territories:
        # Determine requirements for this territory & platform
        reqs = [
            d for d in deliverables_list
            if d.get("territory") == t and str(d.get("platform", "")).upper() == platform.upper()
        ]
        
        # Fallback to standard requirements if none defined in DB
        if not reqs:
            reqs = [
                {"asset_type": "master_video", "spec_details": "ProRes 422 HQ / 1080p24"},
                {"asset_type": "subtitle", "spec_details": "Localized SRT/VTT (UTF-8)"},
                {"asset_type": "artwork_poster", "spec_details": "2:3 Portrait Key Art"},
                {"asset_type": "artwork_banner", "spec_details": "16:9 Landscape Hero Banner"},
                {"asset_type": "metadata", "spec_details": "Localized Title & Synopsis"},
            ]

        for req in reqs:
            asset_type = req.get("asset_type")
            spec = req.get("spec_details", "")
            is_master = (asset_type == "master_video")

            # Look for matching asset
            matched_asset = next(
                (a for a in assets_list if a.get("territory") == t and a.get("asset_type") == asset_type),
                None
            )

            owner, next_act = get_owner_and_action(asset_type, t, "delivery required")

            if not matched_asset:
                if is_master:
                    has_master_failure = True
                else:
                    has_supporting_failure = True

                checks.append(
                    CheckItem(
                        category=asset_type,
                        territory=t,
                        status="fail",
                        reason=f"Required {asset_type} deliverable is missing from asset repository ({spec}).",
                        evidence=[f"asset:{title_id}:{t}:{asset_type}:missing"],
                        owner=owner,
                        next_action=next_act,
                    )
                )
            else:
                qc_status = str(matched_asset.get("qc_status", "")).lower()
                qc_notes = matched_asset.get("qc_notes", "No QC notes")
                asset_id = matched_asset.get("asset_id", f"ast-{title_id}-{t.lower()}-{asset_type}")

                if qc_status == "passed":
                    checks.append(
                        CheckItem(
                            category=asset_type,
                            territory=t,
                            status="pass",
                            reason=f"{asset_type.replace('_', ' ').title()} passed technical QC ({qc_notes}).",
                            evidence=[f"asset:{asset_id}:{t}:passed"],
                            owner=owner,
                            next_action="Asset verified and ready for distribution.",
                        )
                    )
                else:
                    # Failed or Pending QC
                    if is_master:
                        has_master_failure = True
                    else:
                        has_supporting_failure = True

                    owner, next_act = get_owner_and_action(asset_type, t, qc_notes)
                    checks.append(
                        CheckItem(
                            category=asset_type,
                            territory=t,
                            status="fail",
                            reason=f"{asset_type.replace('_', ' ').title()} QC status is '{qc_status}': {qc_notes}",
                            evidence=[f"asset:{asset_id}:{t}:{qc_status}"],
                            owner=owner,
                            next_action=next_act,
                        )
                    )

    # 3. COMPUTE FINAL DECISION HIERARCHY
    passed_count = sum(1 for c in checks if c.status == "pass")
    failed_count = sum(1 for c in checks if c.status != "pass")
    total_count = len(checks)

    # Strict Rule Hierarchy
    if has_rights_failure or has_master_failure:
        decision = DecisionEnum.RED
    elif has_supporting_failure:
        decision = DecisionEnum.AMBER
    elif failed_count == 0 and total_count > 0:
        decision = DecisionEnum.GREEN
    else:
        # Incomplete / missing DB data must NEVER produce GREEN
        decision = DecisionEnum.RED

    # Build deterministic executive summary
    title_name = title_meta.get("title_name", title_id)
    if decision == DecisionEnum.GREEN:
        summary = (
            f"LAUNCH APPROVED: '{title_name}' is fully greenlit for {platform} distribution "
            f"across all requested territories ({', '.join(territories)}) on {launch_date}."
        )
    elif decision == DecisionEnum.RED:
        if has_rights_failure and has_master_failure:
            summary = (
                f"LAUNCH BLOCKED (RED): '{title_name}' has critical rights window violations and "
                f"master video QC failures blocking launch on {launch_date}."
            )
        elif has_rights_failure:
            # Check specific territory
            failed_rights_territories = [c.territory for c in checks if c.category == "rights" and c.status == "fail"]
            summary = (
                f"Launch is blocked by an expired or invalid rights window in "
                f"{', '.join(failed_rights_territories)}."
            )
        else:
            failed_master_territories = [c.territory for c in checks if c.category == "master_video" and c.status == "fail"]
            summary = (
                f"LAUNCH BLOCKED (RED): Required broadcast master video failed QC or is missing in "
                f"{', '.join(failed_master_territories)}."
            )
    else:
        # AMBER
        failed_sub_types = list(dict.fromkeys([c.category.replace('_', ' ') for c in checks if c.status == "fail"]))
        summary = (
            f"LAUNCH CONDITIONALLY APPROVED (AMBER): Rights and master video are valid for '{title_name}', "
            f"but launch is pending required {', '.join(failed_sub_types)} deliverables."
        )

    return GreenlightResponse(
        decision=decision,
        summary=summary,
        checks=checks,
        tool_trace=tool_trace,
        data_mode=data_mode,
        passed_count=passed_count,
        failed_count=failed_count,
        total_count=total_count,
        title_id=title_id,
        launch_date=launch_date.isoformat(),
        territories=territories,
        platform=platform,
    )
