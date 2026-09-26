/**
 * PocketSmart AI - Home Interior Planner Controller
 */

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("home-planner-form");
    const spinner = document.getElementById("loading-spinner");
    const resultsContainer = document.getElementById("results-container");

    if (!form) return;

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const budget = parseFloat(document.getElementById("budget").value);
        const roomType = document.getElementById("room_type").value;
        const style = document.getElementById("style").value;

        // Collect checked priority items
        const checkboxes = document.querySelectorAll("input[name='required_items']:checked");
        const requiredItems = Array.from(checkboxes).map(cb => cb.value);

        if (!budget || budget <= 0) {
            PocketApp.showToast("Please enter a valid positive budget.", "error");
            return;
        }

        // Show spinner, hide previous results
        spinner.style.display = "block";
        resultsContainer.style.display = "none";
        form.querySelector("button[type='submit']").disabled = true;

        const payload = {
            budget: budget,
            room_type: roomType,
            style: style,
            required_items: requiredItems
        };

        try {
            const token = PocketApp.getToken();
            const headers = { "Content-Type": "application/json" };
            if (token) headers["Authorization"] = `Bearer ${token}`;

            const res = await fetch("/generate-home", {
                method: "POST",
                headers: headers,
                body: JSON.stringify(payload)
            });

            if (!res.ok) {
                const errData = await res.json().catch(() => ({}));
                throw new Error(errData.detail || "Failed to generate home plan.");
            }

            const data = await res.json();
            renderHomeResults(data);
            PocketApp.showToast("Interior plan generated successfully!", "success");
        } catch (err) {
            PocketApp.showToast(err.message, "error");
            console.error("Home planner error:", err);
        } finally {
            spinner.style.display = "none";
            form.querySelector("button[type='submit']").disabled = false;
        }
    });

    function renderHomeResults(data) {
        document.getElementById("res-title").textContent = data.title;
        document.getElementById("res-budget").textContent = `$${data.budget.toFixed(2)}`;
        document.getElementById("res-spent").textContent = `$${data.total_estimated_cost.toFixed(2)}`;
        document.getElementById("res-remaining").textContent = `$${data.remaining_budget.toFixed(2)}`;

        // Sample data badge
        const badge = document.getElementById("res-badge");
        if (data.is_sample_data) {
            badge.textContent = "Algorithmic Market Estimate (Sample)";
            badge.className = "badge badge-warning";
        } else {
            badge.textContent = "AI Live Curated";
            badge.className = "badge badge-success";
        }

        // Render Items
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
                    <a href="${item.vendor_link}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm" style="margin-top:8px;">View Item &rarr;</a>
                </div>
            `;
            itemsList.appendChild(card);
        });

        // Design Tips
        const tipsList = document.getElementById("res-tips-list");
        tipsList.innerHTML = "";
        (data.design_tips || []).forEach(tip => {
            const li = document.createElement("li");
            li.textContent = tip;
            li.style.marginBottom = "6px";
            tipsList.appendChild(li);
        });

        resultsContainer.style.display = "block";
        resultsContainer.scrollIntoView({ behavior: "smooth" });
    }
});

