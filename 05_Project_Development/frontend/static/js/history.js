/**
 * PocketSmart AI - History & Recommendation Archives Controller
 */

document.addEventListener("DOMContentLoaded", () => {
    loadUserHistory();
});

async function loadUserHistory() {
    const container = document.getElementById("history-container");
    const emptyState = document.getElementById("empty-state");
    const loginPrompt = document.getElementById("login-prompt");

    if (!container) return;

    try {
        const token = PocketApp.getToken();
        const headers = token ? { "Authorization": `Bearer ${token}` } : {};

        const res = await fetch("/history", { headers });

        if (res.status === 401) {
            if (loginPrompt) loginPrompt.style.display = "block";
            if (emptyState) emptyState.style.display = "none";
            return;
        }

        if (!res.ok) {
            throw new Error("Failed to load recommendation history.");
        }

        const items = await res.json();
        if (items.length === 0) {
            if (emptyState) emptyState.style.display = "block";
            if (loginPrompt) loginPrompt.style.display = "none";
            container.innerHTML = "";
            return;
        }

        if (emptyState) emptyState.style.display = "none";
        if (loginPrompt) loginPrompt.style.display = "none";
        container.innerHTML = "";

        items.forEach(rec => {
            const card = document.createElement("div");
            card.className = "card";
            card.style.marginBottom = "16px";

            const dateStr = new Date(rec.created_at).toLocaleDateString(undefined, {
                year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
            });

            card.innerHTML = `
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; flex-wrap:wrap; gap:10px;">
                    <div>
                        <span class="badge badge-info" style="margin-right:8px;">${rec.category.toUpperCase()}</span>
                        <span class="badge ${rec.is_sample_data ? 'badge-warning' : 'badge-success'}">
                            ${rec.is_sample_data ? 'Sample / Heuristic' : 'AI Live'}
                        </span>
                        <h3 style="margin-top:8px; font-size:1.2rem; color:var(--dark);">${rec.title}</h3>
                        <small style="color:var(--muted);">${dateStr}</small>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-size:1.25rem; font-weight:700; color:var(--primary);">$${rec.total_estimated_cost.toFixed(2)}</div>
                        <small style="color:var(--muted);">Budget: $${rec.budget.toFixed(2)}</small>
                    </div>
                </div>
                <div style="display:flex; justify-content:flex-end; gap:10px; margin-top:16px;">
                    <a href="/details-page?id=${rec.id}" class="btn btn-primary btn-sm">Inspect Details</a>
                    <button onclick="deleteRecommendation(${rec.id})" class="btn btn-secondary btn-sm" style="color:var(--danger); border-color:#fecaca;">Delete</button>
                </div>
            `;
            container.appendChild(card);
        });
    } catch (err) {
        console.error("History loading error:", err);
        PocketApp.showToast("Could not retrieve history. Please ensure you are logged in.", "error");
    }
}

async function deleteRecommendation(id) {
    if (!confirm("Are you sure you want to delete this recommendation record?")) {
        return;
    }

    try {
        const token = PocketApp.getToken();
        const headers = token ? { "Authorization": `Bearer ${token}` } : {};

        const res = await fetch(`/history/${id}`, {
            method: "DELETE",
            headers: headers
        });

        if (!res.ok) {
            throw new Error("Failed to delete record.");
        }

        PocketApp.showToast("Recommendation removed.", "success");
        loadUserHistory();
    } catch (err) {
        PocketApp.showToast(err.message, "error");
    }
}

