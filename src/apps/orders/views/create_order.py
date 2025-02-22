from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from apps.orders.forms import OrderForm, ItemsFormSet
from apps.orders.models import OrderItem


@require_http_methods(["GET", "POST"])
def create_order(request: WSGIRequest) -> HttpResponse:
    extra_context = {"selected": "orders"}

    if request.method == "POST":
        form = OrderForm(request.POST)
        items_formset = ItemsFormSet(request.POST)

        if form.is_valid() and items_formset.is_valid():
            order = form.save(commit=False)
            order.total_price = 100  # Todo: to business
            order.save()

            for item_form in items_formset:
                if item_form.cleaned_data:
                    order_item = item_form.save(commit=False)
                    order_item.order = order
                    order_item.save()

            return redirect("orders:list")
        else:
            context = {
                "form": form,
                "items_formset": items_formset,
                **extra_context,
            }
            return render(request, "orders/create_order.html", context)
    else:
        context = {
            "form": OrderForm(),
            "items_formset": ItemsFormSet(queryset=OrderItem.objects.none()),
            **extra_context,
        }
        return render(request, "orders/create_order.html", context)
