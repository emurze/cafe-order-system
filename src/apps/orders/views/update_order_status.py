from django.core.handlers.wsgi import WSGIRequest
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST

from apps.orders.forms import OrderUpdateForm
from apps.orders.models import Order


@require_POST
def update_order_status(request: WSGIRequest, pk: int) -> HttpResponse:
    form = OrderUpdateForm(request.POST)
    if not form.is_valid():
        return redirect(reverse("orders:list"))

    with transaction.atomic():
        order = get_object_or_404(Order.objects.select_for_update(), pk=pk)
        order.status = form.cleaned_data["status"]
        order.save()

    if request.POST.get("redirect_to_detail"):
        return redirect(reverse("orders:detail", kwargs={"pk": pk}))
    return redirect(reverse("orders:list"))
