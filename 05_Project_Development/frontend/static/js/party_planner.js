/**
 * PocketSmart AI - Party & Event Planner Controller
 */

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("party-planner-form");
    const spinner = document.getElementById("loading-spinner");
    const resultsContainer = document.getElementById("results-container");

    if (!form) return;

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const occasion = document.getElementById("occasion").value;
        const budget = parseFloat(document.getElementById("budget").value);
        const guestCount = parseInt(document.getElementById("guest_count").value, 10);
        const venueType = document.getElementById("venue_type").value;

        if (!budget || budget <= 0) {
            PocketApp.showToast("Please enter a valid positive budget.", "error");
            return;
        }

        if (!guestCount || guestCount < 1) {
            PocketApp.showToast("Guest count must be at least 1.", "error");
            return;
        }

        spinner.style.display = "block";
        resultsContainer.style.display = "none";
        form.querySelector("button[type='submit']").disabled = true;

        const payload = {
            occasion: occasion,
            budget: budget,
            guest_count: guestCount,
            venue_type: venueType
        };

        try {
            const token = PocketApp.getToken();
            const headers = { "Content-Type": "application/json" };
            if (token) headers["Authorization"] = `Bearer ${token}`;

            const res = await fetch("/generate-party", {
                method: "POST",
                headers: headers,
                body: JSON.stringify(payload)
            });

            if (!res.ok) {
                const errData = await res.json().catch(() => ({}));
                throw new Error(errData.detail || "Failed to generate party plan.");
            }

            const data = await res.json();
            renderPartyResults(data);
            PocketApp.showToast("Event budget roadmap created!", "success");
        } catch (err) {
            PocketApp.showToast(err.message, "error");
            console.error("Party planner error:", err);
        } finally {
            spinner.style.display = "none";
            form.querySelector("button[type='submit']").disabled = false;
        }
    });

    function renderPartyResults(data) {
        document.getElementById("res-title").textContent = data.title;
        document.getElementById("res-budget").textContent = `$${data.budget.toFixed(2)}`;
        document.getElementById("res-spent").textContent = `$${data.total_estimated_cost.toFixed(2)}`;
        document.getElementById("res-perhead").textContent = `$${data.per_guest_cost.toFixed(2)}`;
        document.getElementById("res-remaining").textContent = `$${data.remaining_budget.toFixed(2)}`;

        // Badge
        const badge = document.getElementById("res-badge");
        if (data.is_sample_data) {
            badge.textContent = "Algorithmic Market Estimate (Sample)";
            badge.className = "badge badge-warning";
        } else {
            badge.textContent = "AI Live Curated";
            badge.className = "badge badge-success";
        }

        // Allocations breakdown
        const allocContainer = document.getElementById("res-allocations");
        allocContainer.innerHTML = "";
        const alloc = data.allocations || {};
        for (const [key, val] of Object.entries(alloc)) {
            const formattedKey = key.replace(/_/g, " ").replace(/\b\w/g, l => l.toUpperCase());
            const percent = ((val / data.budget) * 100).toFixed(0);
            const div = document.createElement("div");
            div.style.marginBottom = "10px";
            div.innerHTML = `
                <div style="display:flex; justify-content:space-between; font-size:0.9rem; margin-bottom:4px;">
                    <span><strong>${formattedKey}</strong> (${percent}%)</span>
                    <span>$${val.toFixed(2)}</span>
                </div>
                <div style="background:var(--border); border-radius:9999px; height:8px; overflow:hidden;">
                    <div style="background:var(--primary); height:100%; width:${percent}%;"></div>
                </div>
            `;
            allocContainer.appendChild(div);
        }

        // Items list
        const itemsList = document.getElementById("res-items-list");
        itemsList.innerHTML = "";
        data.items.forEach(item => {
            const card = document.createElement("div");
            card.className = "item-card";
            card.innerHTML = `
                <div class="item-info">
                    <span class="badge badge-info" style="margin-bottom:6px;">${item.category}</span>
                    <h4>${item.name}</h4>
                    <p>${item.description}</p>
                    <small style="color:var(--muted);">Qty: ${item.quantity} | Link Type: <em>${item.link_type}</em></small>
                </div>
                <div class="item-price">
                    <div class="price-tag">$${item.estimated_price.toFixed(2)}</div>
                    <a href="${item.vendor_link}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm" style="margin-top:8px;">View Option &rarr;</a>
                </div>
            `;
            itemsList.appendChild(card);
        });

        // Checklist
        const checkList = document.getElementById("res-checklist");
        checkList.innerHTML = "";
        (data.checklist || []).forEach(task => {
            const li = document.createElement("li");
            li.textContent = task;
            li.style.marginBottom = "6px";
            checkList.appendChild(li);
        });

        resultsContainer.style.display = "block";
        resultsContainer.scrollIntoView({ behavior: "smooth" });
    }
});

