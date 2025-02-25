document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".close-btn").forEach(button => {
        button.addEventListener("click", () => {
            this.parentElement.remove();
        });
    });
});