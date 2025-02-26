from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from apps.orders import services
from apps.orders.forms import OrderForm, OrderItemFormSet
from apps.orders.models import OrderItem


@require_http_methods(["GET", "POST"])
def create_order(request: WSGIRequest) -> HttpResponse:
    """
    View for creating a new order. Handles both displaying the order form
    (GET) and processing the form data (POST). On successful order creation,
    redirects to the orders list page and shows a success message.
    """
    extra_context = {"selected": "orders"}

    if request.method == "POST":
        form = OrderForm(request.POST)
        item_formset = OrderItemFormSet(request.POST)

        if form.is_valid() and item_formset.is_valid():
            item_list_dto = [
                cleaned_data
                for item_form in item_formset
                if (cleaned_data := item_form.cleaned_data)
            ]
            order_id = services.create_order(form.cleaned_data, item_list_dto)
            messages.success(
                request,
                f"Заказ #{order_id} был успешно добавлен!",
            )
            return redirect("orders:list")

        context = {
            "form": form,
            "item_formset": item_formset,
            **extra_context,
        }
        return render(request, "orders/create.html", context)
    else:
        context = {
            "form": OrderForm(),
            "item_formset": OrderItemFormSet(
                queryset=OrderItem.objects.none()
            ),
            **extra_context,
        }
        return render(request, "orders/create.html", context)
