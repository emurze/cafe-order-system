document.addEventListener("DOMContentLoaded", () => {
    const formsetContainer = document.getElementById("order-items");
    const addButton = document.getElementById("add-item");
    const totalForms = document.querySelector("[name='form-TOTAL_FORMS']");
    const emptyFormTemplate = document.getElementById("empty-form").innerHTML;

    function updateFormIndices() {
        const formRows = document.querySelectorAll("#order-items .form-row");
        formRows.forEach((row, index) => {
            row.querySelectorAll("input, select, textarea").forEach(field => {
                const name = field.name.replace(/form-\d+-/, `form-${index}-`);
                field.name = name;
                if (field.id) {
                    const id = field.id.replace(/form-\d+-/, `form-${index}-`);
                    field.id = id;
                }
            });
            row.querySelector(".remove-item").dataset.formId = index;
        });

        totalForms.value = formRows.length;
    }

    function addRemoveHandler(button) {
        button.addEventListener("click", () => {
            const formRow = button.closest(".form-row");
            formRow.remove();
            updateFormIndices();
        });
    }

    addButton.addEventListener("click", () => {
        const totalFormsCount = parseInt(totalForms.value);
        const newForm = emptyFormTemplate.replace(/__prefix__/g, totalFormsCount);
        const newFormElement = document.createElement("div");
        newFormElement.innerHTML = newForm;
        formsetContainer.appendChild(newFormElement);
        totalForms.value = totalFormsCount + 1;

        const newRemoveButton = newFormElement.querySelector(".remove-item");
        addRemoveHandler(newRemoveButton);

        updateFormIndices();
    });

    document.querySelectorAll(".remove-item").forEach(button => {
        addRemoveHandler(button);
    });
});