document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete-order-btn');
    const modal = document.getElementById('deleteConfirmationModal');
    const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
    const cancelDeleteBtn = document.getElementById('cancelDeleteBtn');

    let deleteForm = null;

    // Открываем модальное окно при клике на кнопку удаления
    deleteButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault(); // Предотвращаем переход по ссылке
            deleteForm = button.closest('form'); // Находим форму для удаления
            modal.classList.add('show'); // Показываем модальное окно с анимацией
        });
    });

    // Подтверждение удаления
    confirmDeleteBtn.addEventListener('click', function () {
        if (deleteForm) {
            const orderCard = deleteForm.closest('.container');
            orderCard.classList.add('removing'); // Анимация удаления карточки

            // Удаляем карточку после завершения анимации
            setTimeout(() => {
                deleteForm.submit(); // Отправляем форму
            }, 200); // Время должно совпадать с длительностью анимации
        }
    });

    // Отмена удаления
    cancelDeleteBtn.addEventListener('click', function () {
        modal.classList.remove('show'); // Скрываем модальное окно с анимацией
    });

    // Закрытие модального окна при клике вне его области
    window.addEventListener('click', function (e) {
        if (e.target === modal) {
            modal.classList.remove('show'); // Скрываем модальное окно с анимацией
        }
    });
});