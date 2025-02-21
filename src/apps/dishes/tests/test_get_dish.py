import pytest
from django.shortcuts import resolve_url
from django.test import Client
from faker import Faker
from model_bakery import baker
from rest_framework import status


@pytest.mark.e2e
@pytest.mark.django_db
def test_can_get_dish(client: Client) -> None:
    # arrange
    dish = baker.make("Dish")

    # act
    url = resolve_url("dishes:detail", dish.slug)
    response = client.get(url)

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert dish.title in response.content.decode("utf-8")


@pytest.mark.e2e
@pytest.mark.django_db
def test_cannot_get_dish_error_404(client: Client, faker: Faker) -> None:
    # act
    url = resolve_url("dishes:detail", faker.slug())
    response = client.get(url)

    # assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
