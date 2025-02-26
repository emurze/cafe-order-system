from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from apps.orders import services
from apps.orders.exceptions import OrderNotFoundException
from apps.orders.forms import OrderUpdateForm


@require_POST
def update_order_status(request: WSGIRequest, pk: int) -> HttpResponse:
    """
    View to update the status of an order.
    If the update is successful, redirects to the order detail or list view.
    If the order is not found, raises a 404 error.
    """
    form = OrderUpdateForm(request.POST)
    if not form.is_valid():
        return redirect(reverse("orders:list"))

    try:
        cd = form.cleaned_data
        services.update_order_status(pk=pk, status=cd["status"])
    except OrderNotFoundException:
        raise Http404("Заказ не найден")

    if request.POST.get("redirect_to_detail"):
        return redirect(reverse("orders:detail", kwargs={"pk": pk}))
    return redirect(reverse("orders:list"))
