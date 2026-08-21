/**
 * SlateGate — Content Operations Frontend Client
 */

document.addEventListener('DOMContentLoaded', () => {
    // State
    let currentMode = 'auto'; // 'auto', 'clickhouse-mcp', 'fixture'
    let scenarios = [];

    // DOM Elements
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
    const decisionSummaryEl = document.getElementById('decisionSummary');
    const toolTraceContainer = document.getElementById('toolTraceContainer');
    const toolTraceChips = document.getElementById('toolTraceChips');
    const checksTableBody = document.getElementById('checksTableBody');
    const errorBanner = document.getElementById('errorBanner');
    const errorMessageEl = document.getElementById('errorMessage');

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
            // Default select first scenario
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

        // Territories
        territoryCheckboxes.forEach(cb => {
            cb.checked = scenario.territories.includes(cb.value);
        });
    }

    function setupEventListeners() {
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

        // Set Loading UI
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
                headers: {
                    'Content-Type': 'application/json'
                },
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
        
        // Decision Banner
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

        decisionSummaryEl.textContent = data.summary;

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

        // Checks Table Rows
        checksTableBody.innerHTML = '';
        data.checks.forEach(c => {
            const tr = document.createElement('tr');
            const statusClass = c.status.toLowerCase() === 'pass' ? 'pass' : 'fail';
            
            const evidenceHtml = (c.evidence || []).map(e => 
                `<span class="evidence-tag">${escapeHtml(e)}</span>`
            ).join(' ');

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
            `;
            checksTableBody.appendChild(tr);
        });

        // Update mode badge
        updateModeIndicator(data.data_mode === 'clickhouse-mcp');
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
