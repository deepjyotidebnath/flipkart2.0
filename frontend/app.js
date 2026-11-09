/**
 * Flipkart Intelligence Agent Dashboard Application Logic
 */

let currentMode = "shopping";
let compareList = [];
let allProducts = [];
let elasticityChart = null;
let categoryTrendsChart = null;
let sentimentChart = null;

// Initialize on DOM load
document.addEventListener("DOMContentLoaded", () => {
  fetchCatalog();
  loadBiData();
  setupEventListeners();
});

function switchTab(mode) {
  currentMode = mode;
  document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
  document.querySelectorAll(".view-panel").forEach(panel => panel.classList.remove("active"));

  if (mode === "shopping") {
    document.getElementById("tabShopping").classList.add("active");
    document.getElementById("shoppingView").classList.add("active");
  } else {
    document.getElementById("tabBusiness").classList.add("active");
    document.getElementById("businessView").classList.add("active");
    // Trigger chart renders
    setTimeout(() => {
      if (elasticityChart) elasticityChart.resize();
      if (categoryTrendsChart) categoryTrendsChart.resize();
      if (sentimentChart) sentimentChart.resize();
    }, 100);
  }
}

// ----------------- CATALOG & PRODUCT ACTIONS -----------------
async function fetchCatalog(category = "") {
  try {
    const url = category ? `/api/products?category=${encodeURIComponent(category)}` : "/api/products";
    const res = await fetch(url);
    const data = await res.json();
    allProducts = data.products || [];
    renderCatalog(allProducts);
    populateProductSelector(allProducts);
  } catch (err) {
    console.error("Failed to load catalog:", err);
  }
}

function renderCatalog(products) {
  const grid = document.getElementById("productsGrid");
  if (!products || products.length === 0) {
    grid.innerHTML = `<p style="grid-column: 1/-1; text-align:center; padding: 30px; color:#888;">No products found.</p>`;
    return;
  }

  grid.innerHTML = products.map(p => {
    const isAdded = compareList.includes(p.id);
    return `
      <div class="product-card" data-id="${p.id}">
        <img class="product-thumb" src="${p.image_url}" alt="${p.title}" loading="lazy" />
        <span class="brand-tag">${p.brand}</span>
        <div class="product-name" title="${p.title}">${p.title}</div>
        <div class="ratings-row">
          <span class="rating-badge">★ ${p.rating}</span>
          <span class="review-count">(${Number(p.rating_count).toLocaleString()})</span>
        </div>
        <div class="price-row">
          <span class="final-price">₹${Number(p.price).toLocaleString()}</span>
          <span class="original-price">₹${Number(p.original_price).toLocaleString()}</span>
          <span class="discount-badge">${p.discount_pct}% off</span>
        </div>
        <div class="card-actions">
          <button class="card-btn btn-secondary" onclick="toggleCompare('${p.id}')">
            ${isAdded ? '✓ Added' : '+ Compare'}
          </button>
          <button class="card-btn btn-primary" onclick="sendQuickPrompt('Evaluate and review ${p.title.replace(/'/g, "\\'")}')">
            AI Review
          </button>
        </div>
      </div>
    `;
  }).join("");
}

function filterCatalog() {
  const cat = document.getElementById("catFilter").value;
  fetchCatalog(cat);
}

function toggleCompare(productId) {
  if (compareList.includes(productId)) {
    compareList = compareList.filter(id => id !== productId);
  } else {
    if (compareList.length >= 4) {
      alert("You can compare up to 4 products at a time.");
      return;
    }
    compareList.push(productId);
  }
  document.getElementById("compareCount").innerText = compareList.length;
  renderCatalog(allProducts);
}

async function openCompareDrawer() {
  if (compareList.length < 2) {
    alert("Please select at least 2 products using '+ Compare' before opening the comparison drawer.");
    return;
  }

  const modal = document.getElementById("compareModal");
  const body = document.getElementById("compareModalBody");
  body.innerHTML = `<p>Loading comparison data...</p>`;
  modal.classList.add("open");

  try {
    const res = await fetch(`/api/compare?ids=${compareList.join(",")}`);
    const data = await res.json();

    const headerCols = data.products.map(p => `
      <th>
        <div class="comp-header-card">
          <img src="${p.image_url}" alt="${p.title}" />
          <strong>${p.title}</strong>
          <div style="color:var(--fk-blue); font-weight:700; margin-top:4px;">₹${Number(p.price).toLocaleString()}</div>
        </div>
      </th>
    `).join("");

    const rows = data.comparison_matrix.map(row => {
      const cells = data.products.map(p => `<td>${row[p.id] || "—"}</td>`).join("");
      return `
        <tr>
          <td><strong>${row.spec_name}</strong></td>
          ${cells}
        </tr>
      `;
    }).join("");

    body.innerHTML = `
      <table class="compare-table">
        <thead>
          <tr>
            <th>Specification</th>
            ${headerCols}
          </tr>
        </thead>
        <tbody>
          ${rows}
        </tbody>
      </table>
    `;
  } catch (err) {
    body.innerHTML = `<p style="color:red;">Error loading comparison: ${err.message}</p>`;
  }
}

function closeCompareDrawer() {
  document.getElementById("compareModal").classList.remove("open");
}

// ----------------- AI CHAT & LANGGRAPH WORKFLOW -----------------
function sendQuickPrompt(promptText) {
  document.getElementById("chatInput").value = promptText;
  handleChatSubmit(new Event("submit"));
}

async function handleChatSubmit(e) {
  if (e) e.preventDefault();
  const input = document.getElementById("chatInput");
  const query = input.value.trim();
  if (!query) return;

  // Render User Message
  appendMessage("user", query);
  input.value = "";

  // Show live agent trace box
  const traceBox = document.getElementById("liveAgentTrace");
  const traceBody = document.getElementById("traceBody");
  traceBox.style.display = "block";
  traceBody.innerHTML = `
    <div class="trace-step">
      <span class="trace-agent-tag">LangGraph Engine:</span>
      <span class="trace-desc">Initiating multi-agent state graph for query...</span>
    </div>
  `;

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: query, mode: "shopping" })
    });
    const data = await res.json();

    // Render trace details
    if (data.agent_trace && data.agent_trace.length > 0) {
      document.getElementById("traceSummaryCount").innerText = `(${data.agent_trace.length} nodes executed)`;
      traceBody.innerHTML = data.agent_trace.map(t => `
        <div class="trace-step">
          <span class="trace-agent-tag">⚡ ${t.agent}:</span>
          <div class="trace-desc">${t.action}</div>
        </div>
      `).join("");
    }

    // Render agent answer
    appendMessage("agent", data.response);

    // If products were returned, filter catalog view
    if (data.products && data.products.length > 0) {
      renderCatalog(data.products);
      document.getElementById("catalogSubtitle").innerText = `Showing AI recommendations for: "${query}"`;
    }

    // Render dynamic follow-up chips
    if (data.suggestions && data.suggestions.length > 0) {
      renderQuickChips(data.suggestions);
    }
  } catch (err) {
    appendMessage("agent", `Sorry, I encountered an error: ${err.message}`);
  }
}

function appendMessage(sender, text) {
  const container = document.getElementById("chatMessages");
  const row = document.createElement("div");
  row.className = `message-row ${sender === 'user' ? 'user-row' : 'agent-row'}`;

  // Simple markdown formatting helper
  const formattedText = text
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^## (.*$)/gim, '<h3>$1</h3>')
    .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/gim, '<em>$1</em>')
    .replace(/^\- (.*$)/gim, '<li>$1</li>')
    .replace(/\n/gim, '<br>');

  row.innerHTML = `
    <div class="bubble ${sender === 'user' ? 'user-bubble' : 'agent-bubble'}">
      ${sender === 'agent' ? `
        <div class="bubble-header">
          <span class="bot-tag">Flipkart Intelligence</span>
          <span class="time-stamp">Just now</span>
        </div>
      ` : ''}
      <div class="bubble-content">${formattedText}</div>
    </div>
  `;
  container.appendChild(row);
  container.scrollTop = container.scrollHeight;
}

function renderQuickChips(suggestions) {
  const chipContainer = document.getElementById("quickChips");
  chipContainer.innerHTML = suggestions.map(s => `
    <button class="chip" onclick="sendQuickPrompt('${s.replace(/'/g, "\\'")}')">${s}</button>
  `).join("");
}

function toggleTraceAccordion() {
  const body = document.getElementById("traceBody");
  const caret = document.getElementById("traceCaret");
  if (body.style.display === "none") {
    body.style.display = "block";
    caret.style.transform = "rotate(0deg)";
  } else {
    body.style.display = "none";
    caret.style.transform = "rotate(-90deg)";
  }
}

// ----------------- BUSINESS INTELLIGENCE SUITE -----------------
async function loadBiData() {
  try {
    // 1. Overview KPIs
    const overRes = await fetch("/api/bi/overview");
    const overData = await overRes.json();
    document.getElementById("kpiProducts").innerText = overData.total_products;
    document.getElementById("kpiGmv").innerText = `₹${(overData.monthly_gmv_inr / 10000000).toFixed(1)} Cr`;
    document.getElementById("kpiMargin").innerText = `${overData.avg_margin_pct}%`;
    document.getElementById("kpiPriceAdv").innerText = `${overData.price_competitiveness_index}%`;
    document.getElementById("kpiSentiment").innerText = `${overData.overall_sentiment_score.toFixed(2)} / 1.0`;

    // 2. Competitor Table
    const compRes = await fetch("/api/bi/pricing");
    const compData = await compRes.json();
    renderCompetitorTable(compData.benchmarks || []);

    // 3. Demand Trends & Alerts
    const trendRes = await fetch("/api/bi/trends");
    const trendData = await trendRes.json();
    renderCategoryTrendsChart(trendData.category_trends || []);
    renderInventoryAlerts(trendData.inventory_risk_alerts || []);

    // 4. Aspect Sentiment
    const sentRes = await fetch("/api/bi/sentiment");
    const sentData = await sentRes.json();
    renderSentimentChart(sentData.aspect_breakdown || []);

    // 5. Initial elasticity run
    runSimulation();
  } catch (err) {
    console.error("Failed to load BI data:", err);
  }
}

function renderCompetitorTable(benchmarks) {
  const tbody = document.getElementById("competitorTableBody");
  tbody.innerHTML = benchmarks.slice(0, 8).map(b => {
    let tagClass = "parity";
    if (b.status === "Best Price") tagClass = "best";
    else if (b.status === "Overpriced") tagClass = "overpriced";

    const gapText = b.price_gap_pct > 0 ? `+${b.price_gap_pct}%` : `${b.price_gap_pct}%`;

    return `
      <tr>
        <td><strong>${b.title}</strong></td>
        <td>₹${Number(b.flipkart_price).toLocaleString()}</td>
        <td>₹${Number(b.lowest_competitor_price).toLocaleString()}</td>
        <td style="color:${b.price_gap_pct <= 0 ? 'var(--fk-green)' : 'var(--fk-red)'}; font-weight:600;">
          ${gapText}
        </td>
        <td><span class="status-tag ${tagClass}">${b.status}</span></td>
      </tr>
    `;
  }).join("");
}

function renderInventoryAlerts(alerts) {
  const list = document.getElementById("inventoryAlertsList");
  if (!alerts || alerts.length === 0) {
    list.innerHTML = `<p style="font-size:12px; color:var(--text-secondary);">No immediate stock risks detected.</p>`;
    return;
  }

  list.innerHTML = alerts.slice(0, 4).map(a => `
    <div class="alert-item ${a.risk_level.toLowerCase()}">
      <div class="alert-info-text">
        <strong>${a.title}</strong>
        <span>Stock: ${a.stock} units (${a.days_of_stock} days remaining)</span>
      </div>
      <span class="alert-badge ${a.risk_level.toLowerCase()}">${a.action}</span>
    </div>
  `).join("");
}

function populateProductSelector(products) {
  const select = document.getElementById("simProductSelect");
  select.innerHTML = products.slice(0, 15).map(p => `
    <option value="${p.id}">${p.title}</option>
  `).join("");
}

function updateSliderDisplay(val) {
  const badge = document.getElementById("sliderValDisplay");
  const num = Number(val);
  badge.innerText = num === 0 ? "0% (Current)" : (num > 0 ? `+${num}% discount` : `${num}% discount`);
}

async function runSimulation() {
  const pid = document.getElementById("simProductSelect").value || "MOB-APPL-IP15";
  const delta = parseFloat(document.getElementById("discountDeltaSlider").value) || 0.0;

  try {
    const res = await fetch("/api/bi/simulate-price", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ product_id: pid, discount_pct_delta: delta })
    });
    const data = await res.json();
    renderSimulationReadout(data);
    renderElasticityChart(data.elasticity_curve || [], data.simulated_discount_pct);
  } catch (err) {
    console.error("Simulation error:", err);
  }
}

function renderSimulationReadout(data) {
  const grid = document.getElementById("simReadoutGrid");
  const revDeltaClass = data.revenue_delta_pct >= 0 ? "delta-pos" : "delta-neg";
  const profDeltaClass = data.profit_delta_pct >= 0 ? "delta-pos" : "delta-neg";

  grid.innerHTML = `
    <div class="sim-stat-box">
      <div class="sim-stat-title">Simulated Price</div>
      <div class="sim-stat-value">₹${Number(data.simulated_price).toLocaleString()}</div>
      <div class="sim-stat-delta">${data.simulated_discount_pct}% off</div>
    </div>
    <div class="sim-stat-box">
      <div class="sim-stat-title">Estimated Volume</div>
      <div class="sim-stat-value">${Number(data.simulated_units).toLocaleString()} units</div>
      <div class="sim-stat-delta delta-pos">PED: ${data.elasticity_coefficient}</div>
    </div>
    <div class="sim-stat-box">
      <div class="sim-stat-title">Gross Revenue</div>
      <div class="sim-stat-value">₹${(data.simulated_revenue / 100000).toFixed(1)}L</div>
      <div class="sim-stat-delta ${revDeltaClass}">${data.revenue_delta_pct >= 0 ? '+' : ''}${data.revenue_delta_pct}%</div>
    </div>
    <div class="sim-stat-box">
      <div class="sim-stat-title">Gross Profit</div>
      <div class="sim-stat-value">₹${(data.simulated_profit / 100000).toFixed(1)}L</div>
      <div class="sim-stat-delta ${profDeltaClass}">${data.profit_delta_pct >= 0 ? '+' : ''}${data.profit_delta_pct}%</div>
    </div>
  `;
}

// ----------------- CHARTS INITIALIZATION -----------------
function renderElasticityChart(curveData, currentSimDisc) {
  const ctx = document.getElementById("elasticityChart").getContext("2d");
  const labels = curveData.map(d => `${d.discount_pct}%`);
  const profits = curveData.map(d => d.profit / 100000);
  const revenues = curveData.map(d => d.revenue / 100000);

  if (elasticityChart) elasticityChart.destroy();

  elasticityChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Projected Gross Profit (₹ Lakhs)",
          data: profits,
          borderColor: "#2874f0",
          backgroundColor: "rgba(40, 116, 240, 0.12)",
          fill: true,
          tension: 0.35,
          borderWidth: 2.5
        },
        {
          label: "Gross Revenue (₹ Lakhs)",
          data: revenues,
          borderColor: "#ff9f00",
          borderDash: [5, 5],
          fill: false,
          tension: 0.35,
          borderWidth: 1.8
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: "top", labels: { boxWidth: 12, font: { size: 11 } } },
        tooltip: {
          callbacks: {
            label: (ctx) => `${ctx.dataset.label}: ₹${ctx.parsed.y.toFixed(1)} Lakhs`
          }
        }
      },
      scales: {
        x: { title: { display: true, text: "Discount Percentage", font: { size: 11 } } },
        y: { title: { display: true, text: "₹ in Lakhs", font: { size: 11 } } }
      }
    }
  });
}

function renderCategoryTrendsChart(categories) {
  const ctx = document.getElementById("categoryTrendsChart").getContext("2d");
  const labels = categories.map(c => c.category);
  const gmvs = categories.map(c => c.total_gmv / 10000000); // in Crores
  const units = categories.map(c => c.units_sold);

  if (categoryTrendsChart) categoryTrendsChart.destroy();

  categoryTrendsChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Monthly GMV (₹ Crores)",
          data: gmvs,
          backgroundColor: "#2874f0",
          borderRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: "top", labels: { boxWidth: 12, font: { size: 11 } } }
      },
      scales: {
        y: { title: { display: true, text: "GMV (₹ Crores)", font: { size: 11 } } }
      }
    }
  });
}

function renderSentimentChart(aspects) {
  const ctx = document.getElementById("sentimentChart").getContext("2d");
  const topAspects = aspects.slice(0, 6);
  const labels = topAspects.map(a => a.aspect);
  const posData = topAspects.map(a => a.positive_pct);
  const negData = topAspects.map(a => a.negative_pct);

  if (sentimentChart) sentimentChart.destroy();

  sentimentChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "% Positive Feedback",
          data: posData,
          backgroundColor: "#388e3c",
          borderRadius: 4
        },
        {
          label: "% Pain Points / Complaints",
          data: negData,
          backgroundColor: "#ff6161",
          borderRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: "top", labels: { boxWidth: 12, font: { size: 11 } } }
      },
      scales: {
        x: { stacked: true },
        y: { stacked: true, max: 100, title: { display: true, text: "% of Verified Mentions" } }
      }
    }
  });
}

// ----------------- BI STRATEGY CHAT -----------------
function sendBiQuery(queryText) {
  document.getElementById("biChatInput").value = queryText;
  handleBiSubmit(new Event("submit"));
}

async function handleBiSubmit(e) {
  if (e) e.preventDefault();
  const input = document.getElementById("biChatInput");
  const query = input.value.trim();
  if (!query) return;

  const box = document.getElementById("biChatResponse");
  box.innerHTML = `<span style="color:#888;">Consulting LangGraph Business Intelligence Agents...</span>`;

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query: query, mode: "business" })
    });
    const data = await res.json();
    const formatted = data.response
      .replace(/^### (.*$)/gim, '<h4 style="margin:4px 0;">$1</h4>')
      .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
      .replace(/^\- (.*$)/gim, '• $1<br>')
      .replace(/\n/gim, '<br>');

    box.innerHTML = formatted;
  } catch (err) {
    box.innerHTML = `<span style="color:red;">Error: ${err.message}</span>`;
  }
}

function setupEventListeners() {
  // ESC to close modal
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeCompareDrawer();
  });
}
