document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("signup-btn");
    if (btn) {
      const url = btn.getAttribute("data-signup-url");
      btn.addEventListener("click", () => {
        window.location.href = url;
      });
    }
  });
  