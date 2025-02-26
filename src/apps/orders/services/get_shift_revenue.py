from django.db.models import Sum, Count
from django.utils import timezone

from apps.orders.models import Order


def get_shift_revenue(start_time, end_time) -> dict:
    """
    Calculates the total revenue and total number of orders
    within a specified time range.
    """
    today = timezone.now().date()

    start_datetime = timezone.make_aware(
        timezone.datetime.combine(today, start_time)
    )
    end_datetime = timezone.make_aware(
        timezone.datetime.combine(today, end_time)
    )

    if end_time <= start_time:
        end_datetime += timezone.timedelta(days=1)

    result = Order.objects.filter(
        status=Order.Status.PAID,
        paid_at__isnull=False,
        paid_at__gte=start_datetime,
        paid_at__lte=end_datetime,
    ).aggregate(
        total_revenue=Sum("total_price"),
        total_orders=Count("*"),
    )
    return {
        "total_revenue": result["total_revenue"] or 0,
        "total_orders": result["total_orders"],
    }
