from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory
from djmoney.forms import MoneyWidget

from apps.orders.models import Order, OrderItem


class BaseOrderItemFormSet(forms.BaseModelFormSet):
    def clean(self):
        super().clean()

        if not any(form.cleaned_data for form in self.forms):
            raise ValidationError("Добавьте хотя бы одно блюдо.")


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = (
            "dish",
            "price",
            "quantity",
        )
        widgets = {
            "price": MoneyWidget(
                amount_widget=forms.NumberInput(
                    attrs={"class": "form-control"}
                ),
                currency_widget=forms.Select(
                    attrs={"class": "form-control"},
                    choices=[("BYN", "BYN")],
                ),
            ),
        }


OrderItemFormSet = modelformset_factory(
    OrderItem,
    form=OrderItemForm,
    formset=BaseOrderItemFormSet,
    extra=1,
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("table_number",)


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("status",)
