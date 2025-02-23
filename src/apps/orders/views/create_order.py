from django.core.handlers.wsgi import WSGIRequest
from django.db import transaction
from django.db.models.signals import post_save
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
        items_formset = OrderItemFormSet(request.POST)

        if form.is_valid() and items_formset.is_valid():
            with transaction.atomic():
                order = Order(**form.cleaned_data, total_price=0)
                order.save()

                for item_form in items_formset:
                    if cd := item_form.cleaned_data:
                        order_item = OrderItem(order=order, **cd)
                        order_item.save()

                post_save.send(sender=Order, instance=order)
            return redirect("orders:list")

        context = {
            "form": form,
            "items_formset": items_formset,
            **extra_context,
        }
        return render(request, "orders/create.html", context)
    else:
        context = {
            "form": OrderForm(),
            "items_formset": OrderItemFormSet(
                queryset=OrderItem.objects.none()
            ),
            **extra_context,
        }
        return render(request, "orders/create.html", context)
