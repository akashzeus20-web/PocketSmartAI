/**
 * PocketSmart AI - Jewelry & Wardrobe Planner Controller
 */

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("jewelry-planner-form");
    const imageInput = document.getElementById("outfit_image");
    const uploadZone = document.getElementById("upload-zone");
    const previewContainer = document.getElementById("preview-container");
    const previewImage = document.getElementById("preview-image");
    const spinner = document.getElementById("loading-spinner");
    const resultsContainer = document.getElementById("results-container");

    // Handle Drag & Drop
    if (uploadZone && imageInput) {
        uploadZone.addEventListener("click", () => imageInput.click());

        ["dragenter", "dragover"].forEach(evt => {
            uploadZone.addEventListener(evt, (e) => {
                e.preventDefault();
                uploadZone.classList.add("dragover");
            });
        });

        ["dragleave", "drop"].forEach(evt => {
            uploadZone.addEventListener(evt, (e) => {
                e.preventDefault();
                uploadZone.classList.remove("dragover");
            });
        });

        uploadZone.addEventListener("drop", (e) => {
            if (e.dataTransfer.files && e.dataTransfer.files[0]) {
                imageInput.files = e.dataTransfer.files;
                displayPreview(imageInput.files[0]);
            }
        });

        imageInput.addEventListener("change", () => {
            if (imageInput.files && imageInput.files[0]) {
                displayPreview(imageInput.files[0]);
            }
        });
    }

    function displayPreview(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            previewImage.src = e.target.result;
            previewContainer.style.display = "block";
        };
        reader.readAsDataURL(file);
    }

    if (!form) return;

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const budget = parseFloat(document.getElementById("budget").value);
        const occasion = document.getElementById("occasion").value;
        const style = document.getElementById("style_preference").value;

        if (!budget || budget <= 0) {
            PocketApp.showToast("Please enter a valid positive budget.", "error");
            return;
        }

        spinner.style.display = "block";
        resultsContainer.style.display = "none";
        form.querySelector("button[type='submit']").disabled = true;

        const formData = new FormData();
        formData.append("budget", budget);
        formData.append("occasion", occasion);
        formData.append("style_preference", style);

        if (imageInput && imageInput.files && imageInput.files[0]) {
            formData.append("image", imageInput.files[0]);
        }

        try {
            const token = PocketApp.getToken();
            const headers = {};
            if (token) headers["Authorization"] = `Bearer ${token}`;

            const res = await fetch("/generate-jewelry", {
                method: "POST",
                headers: headers,
                body: formData
            });

            if (!res.ok) {
                const errData = await res.json().catch(() => ({}));
                throw new Error(errData.detail || "Failed to generate jewelry plan.");
            }

            const data = await res.json();
            renderJewelryResults(data);
            PocketApp.showToast("Jewelry ensemble curated successfully!", "success");
        } catch (err) {
            PocketApp.showToast(err.message, "error");
            console.error("Jewelry planner error:", err);
        } finally {
            spinner.style.display = "none";
            form.querySelector("button[type='submit']").disabled = false;
        }
    });

    function renderJewelryResults(data) {
        document.getElementById("res-title").textContent = data.title;
        document.getElementById("res-budget").textContent = `$${data.budget.toFixed(2)}`;
        document.getElementById("res-spent").textContent = `$${data.total_estimated_cost.toFixed(2)}`;
        document.getElementById("res-remaining").textContent = `$${data.remaining_budget.toFixed(2)}`;

        // Badge
        const badge = document.getElementById("res-badge");
        if (data.is_sample_data) {
            badge.textContent = "Algorithmic Market Estimate (Sample)";
            badge.className = "badge badge-warning";
        } else {
            badge.textContent = "AI Vision Curated";
            badge.className = "badge badge-success";
        }

        // Recommended Metal
        document.getElementById("res-metal").textContent = data.recommended_metal || "Balanced Metals";

        // Vision Insights
        const visionBox = document.getElementById("res-vision-box");
        if (data.vision_analysis && data.vision_analysis.image_processed) {
            visionBox.style.display = "block";
            const colors = (data.vision_analysis.detected_colors || []).join(", ");
            document.getElementById("res-colors").textContent = colors || "Harmonized palette";
            document.getElementById("res-neckline").textContent = data.vision_analysis.neckline_detected || "Standard cut";
            document.getElementById("res-aesthetic").textContent = data.vision_analysis.aesthetic_profile || "Formal elegant";
        } else {
            visionBox.style.display = "none";
        }

        // Styling Advice
        document.getElementById("res-advice").textContent = data.styling_advice || "Pair subtle pieces with your attire.";

        // Items List
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
                    <a href="${item.vendor_link}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm" style="margin-top:8px;">View Jewel &rarr;</a>
                </div>
            `;
            itemsList.appendChild(card);
        });

        resultsContainer.style.display = "block";
        resultsContainer.scrollIntoView({ behavior: "smooth" });
    }
});

