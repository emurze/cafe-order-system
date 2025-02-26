from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory

from apps.orders.models import Order, OrderItem

ORDER_CANNOT_BE_EMPTY_ERROR = "Заказ не должен быть пустым."


class OrderForm(forms.ModelForm):
    """Form for validating the data for creation of an order."""

    class Meta:
        model = Order
        fields = ("table_number",)


class BaseOrderItemFormSet(forms.BaseModelFormSet):
    """
    Formset for validating that an order contains at least one order item.
    """

    def clean(self):
        super().clean()

        if not any(form.cleaned_data for form in self.forms):
            raise ValidationError(ORDER_CANNOT_BE_EMPTY_ERROR)


class OrderItemForm(forms.ModelForm):
    """Form for validating the data for creation of an order item."""

    class Meta:
        model = OrderItem
        fields = (
            "dish",
            "price",
            "quantity",
        )


# Formset for managing multiple order items.
OrderItemFormSet = modelformset_factory(
    OrderItem,
    form=OrderItemForm,
    formset=BaseOrderItemFormSet,
    extra=1,
)


class OrderUpdateForm(forms.ModelForm):
    """Form for validating the status to update an order."""

    class Meta:
        model = Order
        fields = ("status",)


class OrderShiftRevenueForm(forms.Form):
    """
    Form for validating the start and end times
    for calculating shift revenue.
    """

    start_time = forms.TimeField(
        label="Начало смены (HH:MM)",
        widget=forms.TimeInput(attrs={"type": "time"}),
    )
    end_time = forms.TimeField(
        label="Конец смены (HH:MM)",
        widget=forms.TimeInput(attrs={"type": "time"}),
    )
