document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete-order-btn');
    const modal = document.getElementById('deleteConfirmationModal');
    const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
    const cancelDeleteBtn = document.getElementById('cancelDeleteBtn');

    let deleteForm = null;

    deleteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            deleteForm = button.closest('form');
            modal.classList.add('show');
        });
    });

    confirmDeleteBtn.addEventListener('click', function () {
        if (deleteForm) {
            const orderCard = deleteForm.closest('.container');
            orderCard.classList.add('removing');

            setTimeout(() => {
                deleteForm.submit();
            }, 200);
        }
    });

    cancelDeleteBtn.addEventListener('click', function () {
        modal.classList.remove('show');
    });

    window.addEventListener('click', function (e) {
        if (e.target === modal) {
            modal.classList.remove('show');
        }
    });
});