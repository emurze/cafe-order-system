import pytest
from django.shortcuts import resolve_url
from django.test import Client
from faker import Faker
from model_bakery import baker
from rest_framework import status

from _dishes_examples.models import Dish


@pytest.mark.e2e
@pytest.mark.django_db
def test_can_delete_dish(client: Client) -> None:
    # arrange
    dish = baker.make("Dish")

    # act
    url = resolve_url("dishes:delete", dish.slug)
    response = client.delete(url)

    # assert
    assert response.status_code == status.HTTP_302_FOUND
    assert not Dish.objects.exists()


@pytest.mark.e2e
@pytest.mark.django_db
def test_cannot_delete_dish_error_404(client: Client, faker: Faker) -> None:
    # act
    url = resolve_url("dishes:delete", faker.slug())
    response = client.delete(url)

    # assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
