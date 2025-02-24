from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from apps.orders.forms import OrderForm, OrderItemFormSet
from apps.orders.models import OrderItem, Order


@require_http_methods(["GET", "POST"])
def create_order(request: WSGIRequest) -> HttpResponse:
    extra_context = {"selected": "orders"}

    if request.method == "POST":
        form = OrderForm(request.POST)
        item_formset = OrderItemFormSet(request.POST)

        if form.is_valid() and item_formset.is_valid():
            with transaction.atomic():
                order = Order(**form.cleaned_data, total_price=0)
                order.save()

                for item_form in item_formset:
                    if cd := item_form.cleaned_data:
                        order_item = OrderItem(order=order, **cd)
                        order_item.save()

                order.save()

            messages.success(
                request,
                f"Заказ #{order.id} был успешно добавлен!",
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
