import pytest
from django.shortcuts import resolve_url
from django.test import Client
from faker import Faker
from model_bakery import baker
from rest_framework import status


@pytest.mark.e2e
@pytest.mark.django_db
def test_can_update_dish(client: Client, faker: Faker) -> None:
    # arrange
    dish = baker.make("Dish")

    # act
    new_title = faker.word()
    url = resolve_url("dishes:update", dish.slug)
    response = client.post(url, data={"title": new_title})

    dish.refresh_from_db()

    # assert
    assert response.status_code == status.HTTP_302_FOUND
    assert dish.title == new_title
