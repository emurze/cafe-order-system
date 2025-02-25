from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from django.views.decorators.http import require_GET

from apps.orders.forms import OrderShiftRevenueForm
from apps.orders.models import Order


@require_GET
def get_shift_revenue(request: WSGIRequest) -> HttpResponse:
    extra_context = {"selected": "shift_revenue"}

    if request.GET:
        form = OrderShiftRevenueForm(request.GET)
        if form.is_valid():
            start_time = form.cleaned_data["start_time"]
            end_time = form.cleaned_data["end_time"]

            today = timezone.now().date()

            start_datetime = timezone.make_aware(
                timezone.datetime.combine(today, start_time)
            )
            end_datetime = timezone.make_aware(
                timezone.datetime.combine(today, end_time)
            )

            if end_time <= start_time:
                end_datetime += timezone.timedelta(days=1)

            orders = Order.objects.filter(
                status=Order.Status.PAID,
                paid_at__isnull=False,
                paid_at__gte=start_datetime,
                paid_at__lte=end_datetime,
            )

            revenue = (
                    orders.aggregate(total_revenue=Sum("total_price"))[
                        "total_revenue"
                    ]
                    or 0
            )
            total_orders = orders.count()

            context = {
                "form": form,
                "revenue": revenue,
                "total_orders": total_orders,
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
