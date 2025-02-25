function toggleStatusPopup(orderId) {
    const popup = document.getElementById(`statusPopup-${orderId}`);
    if (popup) {
        popup.classList.toggle('hidden');
    }
}


document.querySelectorAll('.update-status-btn').forEach(button => {
    button.addEventListener('click', (event) => {
        event.stopPropagation();
        toggleStatusPopup(button.dataset.orderId);
    });
});

document.addEventListener('click', (event) => {
    const popups = document.querySelectorAll('.status-popup');
    popups.forEach(popup => {
        const form = popup.querySelector('form');
        if (!popup.contains(event.target) && (form && !form.contains(event.target))) {
            popup.classList.add('hidden');
        }
    });
});