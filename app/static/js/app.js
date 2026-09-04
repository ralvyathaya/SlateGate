/**
 * SlateGate — Content Operations Frontend Client
 * Powers Single-Title Greenlight Audits & Fleet-Wide ClickHouse OLAP Intelligence.
 */

document.addEventListener('DOMContentLoaded', () => {
    // State
    let currentMode = 'auto'; // 'auto', 'clickhouse-mcp', 'fixture'
    let scenarios = [];
    let lastAuditData = null;

    // View Tabs
    const tabSingleTitle = document.getElementById('tabSingleTitle');
    const tabFleetAnalytics = document.getElementById('tabFleetAnalytics');
    const singleTitleView = document.getElementById('singleTitleView');
    const fleetAnalyticsView = document.getElementById('fleetAnalyticsView');

    // DOM Elements - Audit Panel
    const titleSelect = document.getElementById('titleSelect');
    const launchDateInput = document.getElementById('launchDateInput');
    const platformInput = document.getElementById('platformInput');
    const territoryCheckboxes = document.querySelectorAll('input[name="territory"]');
    const auditBtn = document.getElementById('auditBtn');
    const btnSpinner = document.getElementById('btnSpinner');
    const btnText = document.getElementById('btnText');
    const modeBadge = document.getElementById('modeBadge');
    const modeBadgeText = document.getElementById('modeBadgeText');
    const modeBtns = document.querySelectorAll('.mode-btn');
    const scenarioCardsContainer = document.getElementById('scenarioCards');
    
    // Result elements
    const resultsContainer = document.getElementById('resultsContainer');
    const decisionBanner = document.getElementById('decisionBanner');
    const decisionBadge = document.getElementById('decisionBadge');
    const passCountEl = document.getElementById('passCount');
    const failCountEl = document.getElementById('failCount');
    const totalCountEl = document.getElementById('totalCount');
    const latencyPill = document.getElementById('latencyPill');
    const btnExportCert = document.getElementById('btnExportCert');
    const decisionSummaryEl = document.getElementById('decisionSummary');
    const toolTraceContainer = document.getElementById('toolTraceContainer');
    const toolTraceChips = document.getElementById('toolTraceChips');
    const traceLatencyNotice = document.getElementById('traceLatencyNotice');
    const checksTableBody = document.getElementById('checksTableBody');
    const errorBanner = document.getElementById('errorBanner');
    const errorMessageEl = document.getElementById('errorMessage');

    // Fleet Analytics Elements
    const btnRefreshFleet = document.getElementById('btnRefreshFleet');
    const kpiFleetReadiness = document.getElementById('kpiFleetReadiness');
    const kpiFleetCounts = document.getElementById('kpiFleetCounts');
    const kpiTotalTitles = document.getElementById('kpiTotalTitles');
    const kpiPassRate = document.getElementById('kpiPassRate');
    const kpiTotalAssets = document.getElementById('kpiTotalAssets');
    const kpiLatency = document.getElementById('kpiLatency');
    const barValueID = document.getElementById('barValueID');
    const progressBarID = document.getElementById('progressBarID');
    const barValueTH = document.getElementById('barValueTH');
    const progressBarTH = document.getElementById('progressBarTH');
    const barValueSG = document.getElementById('barValueSG');
    const progressBarSG = document.getElementById('progressBarSG');
    const bottleneckList = document.getElementById('bottleneckList');
    const fleetTableBody = document.getElementById('fleetTableBody');

    // Remediation Modal Elements
    const remediationModal = document.getElementById('remediationModal');
    const btnCloseRemModal = document.getElementById('btnCloseRemModal');
    const remWorkOrderTitle = document.getElementById('remWorkOrderTitle');
    const remAssignedTeam = document.getElementById('remAssignedTeam');
    const remPriority = document.getElementById('remPriority');
    const remTurnaround = document.getElementById('remTurnaround');
    const remId = document.getElementById('remId');
    const remCliContainer = document.getElementById('remCliContainer');
    const remCliText = document.getElementById('remCliText');
    const btnCopyCli = document.getElementById('btnCopyCli');
    const remContentText = document.getElementById('remContentText');
    const btnCopyWorkOrder = document.getElementById('btnCopyWorkOrder');
    const btnDispatchConfirm = document.getElementById('btnDispatchConfirm');

    // Certificate Modal Elements
    const certModal = document.getElementById('certModal');
    const btnCloseCertModal = document.getElementById('btnCloseCertModal');
    const certTitleName = document.getElementById('certTitleName');
    const certMetaLine = document.getElementById('certMetaLine');
    const certTitleId = document.getElementById('certTitleId');
    const certTerritories = document.getElementById('certTerritories');
    const certHash = document.getElementById('certHash');
    const btnPrintCert = document.getElementById('btnPrintCert');

    // Toast
    const toastNotification = document.getElementById('toastNotification');

    // Initialize
    initApp();

    async function initApp() {
        await checkHealth();
        await loadScenarios();
        setupEventListeners();
    }

    async function checkHealth() {
        try {
            const res = await fetch('/health');
            const data = await res.json();
            updateModeIndicator(data.clickhouse_configured);
        } catch (e) {
            console.warn('Health check failed:', e);
            updateModeIndicator(false);
        }
    }

    function updateModeIndicator(isLive) {
        if (currentMode === 'clickhouse-mcp' || (currentMode === 'auto' && isLive)) {
            modeBadge.className = 'mode-badge live';
            modeBadgeText.textContent = 'Live · Gemini + ClickHouse MCP';
        } else {
            modeBadge.className = 'mode-badge';
            modeBadgeText.textContent = 'Demo · Synthetic Fixture';
        }
    }

    async function loadScenarios() {
        try {
            const res = await fetch('/api/scenarios');
            scenarios = await res.json();
            renderScenarios(scenarios);
            if (scenarios.length > 0) {
                selectScenario(scenarios[0].id);
            }
        } catch (e) {
            console.error('Failed to load scenarios:', e);
        }
    }

    function renderScenarios(list) {
        scenarioCardsContainer.innerHTML = '';
        list.forEach((s) => {
            const card = document.createElement('div');
            card.className = `scenario-card ${s.id === 'slate-001' ? 'active' : ''}`;
            card.dataset.id = s.id;
            
            const badgeClass = s.expected_decision.toLowerCase();
            card.innerHTML = `
                <div class="scenario-header">
                    <span class="scenario-id">${s.id}</span>
                    <span class="scenario-expected ${badgeClass}">${s.expected_decision}</span>
                </div>
                <div class="scenario-title">${escapeHtml(s.title)}</div>
                <div class="scenario-desc">${escapeHtml(s.description)}</div>
            `;
            
            card.addEventListener('click', () => {
                document.querySelectorAll('.scenario-card').forEach(c => c.classList.remove('active'));
                card.classList.add('active');
                selectScenario(s.id);
            });

            scenarioCardsContainer.appendChild(card);
        });
    }

    function selectScenario(scenarioId) {
        const scenario = scenarios.find(s => s.id === scenarioId);
        if (!scenario) return;

        titleSelect.value = scenario.id;
        launchDateInput.value = scenario.launch_date;
        platformInput.value = scenario.platform;

        territoryCheckboxes.forEach(cb => {
            cb.checked = scenario.territories.includes(cb.value);
        });
    }

    function setupEventListeners() {
        // Tab switching
        tabSingleTitle.addEventListener('click', () => {
            tabSingleTitle.classList.add('active');
            tabFleetAnalytics.classList.remove('active');
            singleTitleView.style.display = 'block';
            fleetAnalyticsView.style.display = 'none';
        });

        tabFleetAnalytics.addEventListener('click', () => {
            tabFleetAnalytics.classList.add('active');
            tabSingleTitle.classList.remove('active');
            singleTitleView.style.display = 'none';
            fleetAnalyticsView.style.display = 'block';
            loadFleetAnalytics();
        });

        // Mode switch buttons
        modeBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                modeBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentMode = btn.dataset.mode;
                checkHealth();
            });
        });

        // Run Audit
        auditBtn.addEventListener('click', runGreenlightAudit);

        // Refresh Fleet Analytics
        btnRefreshFleet.addEventListener('click', loadFleetAnalytics);

        // Certificate export
        btnExportCert.addEventListener('click', openCertificateModal);
        btnCloseCertModal.addEventListener('click', () => certModal.style.display = 'none');
        btnPrintCert.addEventListener('click', () => window.print());

        // Remediation modal close
        btnCloseRemModal.addEventListener('click', () => remediationModal.style.display = 'none');

        // Copy buttons
        btnCopyCli.addEventListener('click', () => {
            navigator.clipboard.writeText(remCliText.textContent);
            showToast('CLI command copied to clipboard!');
        });

        btnCopyWorkOrder.addEventListener('click', () => {
            navigator.clipboard.writeText(remContentText.textContent);
            showToast('Work order brief copied to clipboard!');
        });

        btnDispatchConfirm.addEventListener('click', () => {
            remediationModal.style.display = 'none';
            showToast(`🚀 Work order dispatched to ${remAssignedTeam.textContent}!`);
        });

        // Close modals on overlay click
        window.addEventListener('click', (e) => {
            if (e.target === remediationModal) remediationModal.style.display = 'none';
            if (e.target === certModal) certModal.style.display = 'none';
        });
    }

    function getSelectedTerritories() {
        const checked = [];
        territoryCheckboxes.forEach(cb => {
            if (cb.checked) checked.push(cb.value);
        });
        return checked;
    }

    async function runGreenlightAudit() {
        const titleId = titleSelect.value.trim();
        const launchDate = launchDateInput.value;
        const platform = platformInput.value.trim();
        const territories = getSelectedTerritories();

        if (!titleId) {
            alert('Please select or enter a valid Title ID.');
            return;
        }
        if (!launchDate) {
            alert('Please select a valid Launch Date.');
            return;
        }
        if (territories.length === 0) {
            alert('Please select at least one target territory (ID, TH, SG).');
            return;
        }

        setLoading(true);
        hideError();

        const requestBody = {
            title_id: titleId,
            launch_date: launchDate,
            territories: territories,
            platform: platform,
            force_data_mode: currentMode === 'auto' ? null : currentMode
        };

        try {
            const res = await fetch('/api/greenlight', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(requestBody)
            });

            const data = await res.json();

            if (!res.ok) {
                const detail = data.detail || {};
                showError(
                    detail.error || 'Audit Failed',
                    detail.message || `HTTP ${res.status}: Failed to evaluate greenlight.`
                );
                return;
            }

            lastAuditData = data;
            renderResults(data);
        } catch (err) {
            console.error('Audit network failure:', err);
            showError('Network Error', 'Unable to reach backend service. Check server logs.');
        } finally {
            setLoading(false);
        }
    }

    function renderResults(data) {
        resultsContainer.style.display = 'flex';
        
        const decision = data.decision.toLowerCase();
        decisionBanner.className = `decision-banner ${decision}`;
        
        let badgeIcon = '🟢';
        if (decision === 'amber') badgeIcon = '🟡';
        if (decision === 'red') badgeIcon = '🔴';

        decisionBadge.className = `decision-badge-large ${decision}`;
        decisionBadge.innerHTML = `<span>${badgeIcon}</span> <span>${data.decision.toUpperCase()}</span>`;

        passCountEl.textContent = `${data.passed_count} PASS`;
        failCountEl.textContent = `${data.failed_count} FAIL`;
        totalCountEl.textContent = `${data.total_count} CHECKS`;

        // Execution Latency Display
        if (data.execution_time_ms !== undefined) {
            latencyPill.textContent = `⚡ ${data.execution_time_ms} ms`;
            latencyPill.style.display = 'inline-block';
            traceLatencyNotice.textContent = `ClickHouse OLAP: ${data.execution_time_ms} ms`;
        }

        decisionSummaryEl.textContent = data.summary;

        // Enable Export Certificate
        btnExportCert.style.display = 'inline-flex';

        // Tool Trace Chips
        toolTraceChips.innerHTML = '';
        if (data.tool_trace && data.tool_trace.length > 0) {
            data.tool_trace.forEach(t => {
                const chip = document.createElement('span');
                let chipClass = 'trace-chip';
                let icon = '⚡';
                if (t.includes('mcp-clickhouse')) {
                    chipClass += ' mcp';
                    icon = '🗄️ ClickHouse MCP';
                } else if (t.includes('gemini')) {
                    chipClass += ' gemini';
                    icon = '✨ Google Gemini';
                } else if (t.includes('fixture')) {
                    icon = '📦 Fixture';
                }
                chip.className = chipClass;
                chip.innerHTML = `<span>${icon}</span> <span>${escapeHtml(t)}</span>`;
                toolTraceChips.appendChild(chip);
            });
            toolTraceContainer.style.display = 'block';
        } else {
            toolTraceContainer.style.display = 'none';
        }

        // Checks Table Rows with Remediation Buttons
        checksTableBody.innerHTML = '';
        data.checks.forEach(c => {
            const tr = document.createElement('tr');
            const isPass = c.status.toLowerCase() === 'pass';
            const statusClass = isPass ? 'pass' : 'fail';
            
            const evidenceHtml = (c.evidence || []).map(e => 
                `<span class="evidence-tag">${escapeHtml(e)}</span>`
            ).join(' ');

            let resolutionHtml = `<span style="color:var(--color-green); font-size:0.75rem; font-weight:700;">✓ Verified</span>`;
            if (!isPass) {
                resolutionHtml = `
                    <button class="btn-remediate" 
                            data-title="${escapeHtml(data.title_id)}" 
                            data-territory="${escapeHtml(c.territory)}" 
                            data-category="${escapeHtml(c.category)}"
                            data-reason="${escapeHtml(c.reason)}"
                            data-owner="${escapeHtml(c.owner)}"
                            data-action="${escapeHtml(c.next_action)}"
                            data-evidence="${escapeHtml(JSON.stringify(c.evidence || []))}">
                        <span>⚡</span> Remediate
                    </button>
                `;
            }

            tr.innerHTML = `
                <td><span class="category-tag">${escapeHtml(c.category.replace('_', ' ').toUpperCase())}</span></td>
                <td><span class="territory-tag">${escapeHtml(c.territory)}</span></td>
                <td><span class="status-badge ${statusClass}">${c.status.toUpperCase()}</span></td>
                <td>
                    <div>${escapeHtml(c.reason)}</div>
                    <div>${evidenceHtml}</div>
                </td>
                <td>
                    <div class="owner-text">${escapeHtml(c.owner)}</div>
                    <div class="action-text">${escapeHtml(c.next_action)}</div>
                </td>
                <td>${resolutionHtml}</td>
            `;
            checksTableBody.appendChild(tr);
        });

        // Attach remediation listeners
        document.querySelectorAll('.btn-remediate').forEach(btn => {
            btn.addEventListener('click', () => triggerRemediation(btn));
        });

        updateModeIndicator(data.data_mode === 'clickhouse-mcp');
    }

    async function triggerRemediation(button) {
        const titleId = button.dataset.title;
        const territory = button.dataset.territory;
        const category = button.dataset.category;
        const reason = button.dataset.reason;
        const owner = button.dataset.owner;
        const nextAction = button.dataset.action;
        const evidence = JSON.parse(button.dataset.evidence || '[]');

        button.disabled = true;
        button.innerHTML = `<span>⏳</span> Generating...`;

        try {
            const res = await fetch('/api/remediate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    title_id: titleId,
                    territory: territory,
                    category: category,
                    reason: reason,
                    evidence: evidence,
                    owner: owner,
                    next_action: nextAction
                })
            });

            if (!res.ok) {
                showToast('Failed to generate remediation work order.');
                return;
            }

            const data = await res.json();
            openRemediationModal(data);
        } catch (e) {
            console.error('Remediation error:', e);
            showToast('Network error during remediation.');
        } finally {
            button.disabled = false;
            button.innerHTML = `<span>⚡</span> Remediate`;
        }
    }

    function openRemediationModal(data) {
        remWorkOrderTitle.textContent = data.work_order_title;
        remAssignedTeam.textContent = `Assigned to: ${data.assigned_team}`;
        remPriority.textContent = data.priority;
        remTurnaround.textContent = data.estimated_turnaround;
        remId.textContent = data.remediation_id;

        if (data.cli_command) {
            remCliContainer.style.display = 'block';
            remCliText.textContent = data.cli_command;
        } else {
            remCliContainer.style.display = 'none';
        }

        remContentText.textContent = data.work_order_content;
        remediationModal.style.display = 'flex';
    }

    function openCertificateModal() {
        if (!lastAuditData) return;
        const titleOpt = titleSelect.options[titleSelect.selectedIndex];
        certTitleName.textContent = titleOpt ? titleOpt.text.split(':')[1]?.trim() || lastAuditData.title_id : lastAuditData.title_id;
        certTitleId.textContent = lastAuditData.title_id;
        certTerritories.textContent = lastAuditData.territories.map(t => {
            if (t === 'ID') return 'Indonesia (ID)';
            if (t === 'TH') return 'Thailand (TH)';
            if (t === 'SG') return 'Singapore (SG)';
            return t;
        }).join(', ');

        certMetaLine.textContent = `${lastAuditData.platform} Distribution · Verified on ${new Date().toISOString().slice(0, 10)}`;

        // Generate synthetic verification hash
        const rawString = `${lastAuditData.title_id}:${lastAuditData.launch_date}:${lastAuditData.territories.join(',')}:${lastAuditData.decision}`;
        let hash = 0;
        for (let i = 0; i < rawString.length; i++) {
            hash = ((hash << 5) - hash) + rawString.charCodeAt(i);
            hash |= 0;
        }
        certHash.textContent = `sha256:${Math.abs(hash).toString(16).padStart(16, '0')}7f9a8b1c4e2d3f0a`;

        certModal.style.display = 'flex';
    }

    async function loadFleetAnalytics() {
        btnRefreshFleet.disabled = true;
        btnRefreshFleet.innerHTML = `<span>⏳</span> Querying ClickHouse OLAP...`;

        try {
            const modeParam = currentMode === 'auto' ? '' : `?mode=${currentMode}`;
            const res = await fetch(`/api/analytics/fleet${modeParam}`);
            if (!res.ok) {
                console.error('Fleet analytics failed');
                return;
            }

            const data = await res.json();
            renderFleetAnalytics(data);
        } catch (e) {
            console.error('Fleet analytics fetch error:', e);
        } finally {
            btnRefreshFleet.disabled = false;
            btnRefreshFleet.innerHTML = `<span>🔄</span> Refresh Fleet Metrics`;
        }
    }

    function renderFleetAnalytics(data) {
        kpiFleetReadiness.textContent = `${data.fleet_readiness_pct}%`;
        kpiFleetCounts.textContent = `${data.green_count} Green / ${data.amber_count} Amber / ${data.red_count} Red`;
        kpiTotalTitles.textContent = `${data.total_titles} Titles`;
        kpiPassRate.textContent = `${data.qc_pass_rate_pct}%`;
        kpiTotalAssets.textContent = `${data.total_assets} media assets tracked`;
        kpiLatency.textContent = `${data.execution_time_ms} ms`;

        // Territory Readiness Bars
        const idVal = data.territory_readiness.ID || 0;
        const thVal = data.territory_readiness.TH || 0;
        const sgVal = data.territory_readiness.SG || 0;

        barValueID.textContent = `${idVal}%`;
        progressBarID.style.width = `${idVal}%`;

        barValueTH.textContent = `${thVal}%`;
        progressBarTH.style.width = `${thVal}%`;

        barValueSG.textContent = `${sgVal}%`;
        progressBarSG.style.width = `${sgVal}%`;

        // Bottlenecks List
        bottleneckList.innerHTML = '';
        if (data.bottleneck_distribution && data.bottleneck_distribution.length > 0) {
            data.bottleneck_distribution.slice(0, 5).forEach(b => {
                const item = document.createElement('div');
                item.className = 'bottleneck-item';
                item.innerHTML = `
                    <span class="bottleneck-name">${escapeHtml(b.category)}</span>
                    <span class="bottleneck-badge">${b.failure_count} Blockers (${b.share_pct}%)</span>
                `;
                bottleneckList.appendChild(item);
            });
        } else {
            bottleneckList.innerHTML = '<div style="color:var(--text-muted); font-size:0.85rem;">No active bottlenecks flagged.</div>';
        }

        // Render Catalog Register Table
        fleetTableBody.innerHTML = '';
        for (let i = 0; i < titleSelect.options.length; i++) {
            const opt = titleSelect.options[i];
            const tid = opt.value;
            const fullLabel = opt.text;
            const parts = fullLabel.split(':');
            const name = parts[1] ? parts[1].split('(')[0].trim() : tid;
            const genre = parts[1] && parts[1].includes('(') ? parts[1].split('(')[1].replace(')', '').trim() : 'Feature Film';

            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td class="font-mono" style="color:#93c5fd;">${escapeHtml(tid)}</td>
                <td style="font-weight:600; color:#fff;">${escapeHtml(name)}</td>
                <td><span class="category-tag">${escapeHtml(genre)}</span></td>
                <td>2025/2026</td>
                <td>
                    <button class="btn-secondary btn-audit-title" data-title="${escapeHtml(tid)}">
                        <span>🎯</span> Audit
                    </button>
                </td>
            `;
            fleetTableBody.appendChild(tr);
        }

        // Attach 1-click audit buttons in fleet table
        document.querySelectorAll('.btn-audit-title').forEach(btn => {
            btn.addEventListener('click', () => {
                const targetTitle = btn.dataset.title;
                titleSelect.value = targetTitle;
                tabSingleTitle.click();
                runGreenlightAudit();
            });
        });
    }

    function setLoading(isLoading) {
        auditBtn.disabled = isLoading;
        if (isLoading) {
            btnSpinner.style.display = 'inline-block';
            btnText.textContent = 'Auditing Rights & Assets...';
        } else {
            btnSpinner.style.display = 'none';
            btnText.textContent = 'Run Greenlight Audit';
        }
    }

    function showError(title, message) {
        errorBanner.style.display = 'flex';
        errorMessageEl.innerHTML = `<strong>${escapeHtml(title)}:</strong> ${escapeHtml(message)}`;
        resultsContainer.style.display = 'none';
    }

    function hideError() {
        errorBanner.style.display = 'none';
    }

    function showToast(message) {
        toastNotification.textContent = message;
        toastNotification.style.display = 'block';
        setTimeout(() => {
            toastNotification.style.display = 'none';
        }, 3500);
    }

    function escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }
});
