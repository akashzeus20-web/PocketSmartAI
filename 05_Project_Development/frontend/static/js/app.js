/**
 * PocketSmart AI - Global Application Utilities
 */

const PocketApp = {
    // Show toast notification
    showToast(message, type = "info") {
        let container = document.getElementById("toast-container");
        if (!container) {
            container = document.createElement("div");
            container.id = "toast-container";
            container.className = "toast-container";
            document.body.appendChild(container);
        }

        const toast = document.createElement("div");
        toast.className = `toast ${type}`;
        toast.innerHTML = `<span>${message}</span>`;
        container.appendChild(toast);

        setTimeout(() => {
            toast.style.opacity = "0";
            toast.style.transform = "translateX(100%)";
            toast.style.transition = "all 0.3s ease";
            setTimeout(() => toast.remove(), 300);
        }, 4000);
    },

    // Get auth token from localStorage
    getToken() {
        return localStorage.getItem("pocketsmart_token") || "";
    },

    // Set auth token
    setToken(token) {
        if (token) {
            localStorage.setItem("pocketsmart_token", token);
        } else {
            localStorage.removeItem("pocketsmart_token");
        }
    },

    // Get current user payload
    getUser() {
        const u = localStorage.getItem("pocketsmart_user");
        try {
            return u ? JSON.parse(u) : null;
        } catch {
            return null;
        }
    },

    setUser(user) {
        if (user) {
            localStorage.setItem("pocketsmart_user", JSON.stringify(user));
        } else {
            localStorage.removeItem("pocketsmart_user");
        }
    },

    // Global Logout
    async logout() {
        try {
            await fetch("/logout", { method: "POST" });
        } catch (e) {
            console.error("Logout request failed:", e);
        }
        this.setToken("");
        this.setUser(null);
        this.showToast("Logged out successfully.", "info");
        setTimeout(() => {
            window.location.href = "/";
        }, 800);
    },

    // Sync session with backend
    async checkSession() {
        try {
            const token = this.getToken();
            const headers = token ? { "Authorization": `Bearer ${token}` } : {};
            const res = await fetch("/session-info", { headers });
            if (res.ok) {
                const data = await res.json();
                if (data.authenticated) {
                    this.updateAuthNav(data.username);
                } else {
                    this.updateAuthNav(null);
                }
            }
        } catch (err) {
            console.warn("Session check error:", err);
        }
    },

    updateAuthNav(username) {
        const authArea = document.getElementById("nav-auth-area");
        if (!authArea) return;

        if (username) {
            authArea.innerHTML = `
                <span style="font-size:0.9rem; font-weight:600; color:var(--slate);">Hi, ${username}</span>
                <a href="/history-page" class="btn btn-secondary btn-sm">My History</a>
                <button onclick="PocketApp.logout()" class="btn btn-secondary btn-sm">Log Out</button>
            `;
        } else {
            authArea.innerHTML = `
                <a href="/login" class="btn btn-secondary btn-sm">Log In</a>
                <a href="/register" class="btn btn-primary btn-sm">Sign Up</a>
            `;
        }
    }
};

document.addEventListener("DOMContentLoaded", () => {
    PocketApp.checkSession();
});

