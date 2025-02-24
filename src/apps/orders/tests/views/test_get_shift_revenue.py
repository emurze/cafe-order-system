from datetime import timedelta
from pprint import pprint

import pytest
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from model_bakery import baker
from rest_framework import status

from apps.orders.models import Order

# @pytest.mark.django_db
# def test_can_get_shift_revenue(client: Client) -> None:
#     # arrange
#     order = baker.make("Order")
#     item = baker.make("OrderItem", order=order, price=100, quantity=1)
#     order.save()
#
#     order.status = order.Status.PAID
#     order.save()
#
#     start_time = (order.paid_at - timedelta(hours=1)).strftime("%H:%M")
#     end_time = (order.paid_at + timedelta(hours=1)).strftime("%H:%M")
#
#     # act
#     url = reverse("orders:shift_revenue")
#     response = client.get(f"{url}?start_time={start_time}&end_time={end_time}")
#     revenue = response.context.get("revenue")
#     pprint(response.context)
#
#     # assert
#     assert response.status_code == status.HTTP_200_OK
#     assert revenue == item.price
