from pprint import pprint

from django.core.handlers.wsgi import WSGIRequest
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from rest_framework.exceptions import ValidationError

from apps.orders.forms import OrderForm, OrderItemFormSet
from apps.orders.models import OrderItem


# @require_http_methods(["GET", "POST"])
# def create_order(request: WSGIRequest) -> HttpResponse:
#     extra_context = {"selected": "orders"}
#
#     if request.method == "POST":
#         pprint(dict(request.POST))
#
#         form = OrderForm(request.POST)
#         items_formset = OrderItemFormSet(request.POST)
#
#         if form.is_valid() and items_formset.is_valid():
#             order = form.save(commit=False)
#             order.total_price = 100  # Todo: to business
#             order.save()
#
#             for item_form in items_formset:
#                 if item_form.cleaned_data:
#                     order_item = item_form.save(commit=False)
#                     order_item.order = order
#                     order_item.save()
#
#             return redirect("orders:list")
#         else:
#             print("HERE")
#             print(form.errors, items_formset.errors)
#             context = {
#                 "form": form,
#                 "items_formset": items_formset,
#                 **extra_context,
#             }
#             return render(request, "orders/create.html", context)
#     else:
#         context = {
#             "form": OrderForm(),
#             "items_formset": OrderItemFormSet(queryset=OrderItem.objects.none()),
#             **extra_context,
#         }
#         print(context["items_formset"])
#         return render(request, "orders/create.html", context)


@require_http_methods(["GET", "POST"])
def create_order(request: WSGIRequest) -> HttpResponse:
    extra_context = {"selected": "orders"}

    if request.method == "POST":
        pprint(dict(request.POST))
        form = OrderForm(request.POST)
        items_formset = OrderItemFormSet(request.POST)

        if form.is_valid() and items_formset.is_valid():
            try:
                with (
                    transaction.atomic()
                ):  # Must be because we have to elems and we can have failure
                    order = form.save(commit=False)
                    order.total_price = 0  # Инициализация общей стоимости
                    order.save()

                    total_price = 0
                    for item_form in items_formset:
                        if item_form.cleaned_data:
                            order_item = item_form.save(commit=False)
                            order_item.order = order
                            order_item.save()
                            total_price += (
                                    order_item.price.amount * order_item.quantity
                            )

                    order.total_price = total_price
                    order.save()

                    return redirect("orders:list")
            except ValidationError as e:
                form.add_error(None, e)
        else:
            print("Form errors:", form.errors)
            print("Formset errors:", items_formset.errors)
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
