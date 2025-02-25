from rest_framework.generics import RetrieveAPIView

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer


class GetOrderAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
