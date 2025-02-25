from django.core.handlers.wsgi import WSGIRequest
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from apps.orders import services
from apps.orders.exceptions import OrderNotFoundException


@require_http_methods(["POST", "DELETE"])
def delete_order(request: WSGIRequest, pk: int) -> HttpResponse:
    try:
        with transaction.atomic():
            services.delete_order(pk)
    except OrderNotFoundException:
        raise Http404("Заказ не найден")

    return HttpResponseRedirect(reverse("orders:list"))
