from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def get_order_revenue(request: WSGIRequest) -> HttpResponse:
    context = {""}
    return render(request, "orders/revenue.html", context)
