import pytest
from django.shortcuts import resolve_url
from django.test import Client
from faker import Faker
from model_bakery import baker
from rest_framework import status


@pytest.mark.e2e
@pytest.mark.django_db
def test_can_get_dishes(client: Client, faker: Faker) -> None:
    # arrange
    dish = baker.make("Dish", title=faker.text(max_nb_chars=50))
    dish2 = baker.make("Dish", title=faker.text(max_nb_chars=50))

    # act
    url = resolve_url("dishes:list")
    response = client.get(url)
    content = response.content.decode("utf-8")

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert content.count(dish.title) == 1
    assert content.count(dish2.title) == 1
