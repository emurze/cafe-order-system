document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".close-btn").forEach(button => {
        button.addEventListener("click", (event) => {
            event.target.closest(".alert").remove();
        });
    });
});