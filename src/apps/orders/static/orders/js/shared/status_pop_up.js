document.addEventListener("DOMContentLoaded", () => {
    function toggleStatusPopup(orderId) {
        const popup = document.getElementById(`statusPopup-${orderId}`);
        if (popup) {
            popup.classList.toggle('hidden');
        } else {
            console.error(`Popup with ID "statusPopup-${orderId}" not found.`);
        }
    }

    document.querySelectorAll('.update-status-btn').forEach(button => {
        const orderId = button.dataset.orderId;
        if (!orderId) {
            console.error('Button is missing the "data-order-id" attribute.', button);
            return;
        }

        button.addEventListener('click', (event) => {
            event.stopPropagation();
            toggleStatusPopup(orderId);
        });
    });

    document.addEventListener('click', (event) => {
        const popups = document.querySelectorAll('.status-popup');
        popups.forEach(popup => {
            const form = popup.querySelector('form');
            if (!popup.contains(event.target) && (!form || !form.contains(event.target))) {
                popup.classList.add('hidden');
            }
        });
    });
})
