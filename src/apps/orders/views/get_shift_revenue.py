from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from apps.orders import services
from apps.orders.forms import OrderShiftRevenueForm


@require_GET
def get_shift_revenue(request: WSGIRequest) -> HttpResponse:
    """
    View to display shift revenue details based on
    the provided start and end times.
    """
    extra_context = {"selected": "shift_revenue"}

    if request.GET:
        form = OrderShiftRevenueForm(request.GET)
        if form.is_valid():
            start_time = form.cleaned_data["start_time"]
            end_time = form.cleaned_data["end_time"]
            result = services.get_shift_revenue(start_time, end_time)
            context = {
                "form": form,
                "revenue": result["total_revenue"] or 0,
                "total_orders": result["total_orders"],
                "start_time": start_time,
                "end_time": end_time,
                **extra_context,
            }
            return render(request, "orders/shift_revenue.html", context)
    else:
        form = OrderShiftRevenueForm()

    context = {
        "form": form,
        **extra_context,
    }
    return render(request, "orders/shift_revenue.html", context)
