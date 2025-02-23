from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory

from apps.orders.models import Order, OrderItem

ORDER_CANNOT_BE_EMPTY_ERROR = "Заказ не должен быть пустым."


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("table_number",)


class BaseOrderItemFormSet(forms.BaseModelFormSet):
    def clean(self):
        super().clean()

        if not any(form.cleaned_data for form in self.forms):
            raise ValidationError(ORDER_CANNOT_BE_EMPTY_ERROR)


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = (
            "dish",
            "price",
            "quantity",
        )


OrderItemFormSet = modelformset_factory(
    OrderItem,
    form=OrderItemForm,
    formset=BaseOrderItemFormSet,
    extra=1,
)


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("status",)
