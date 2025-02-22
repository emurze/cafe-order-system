import pytest
from django.shortcuts import resolve_url
from django.test import Client
from rest_framework import status

from _dishes_examples.models import Dish


@pytest.mark.e2e
@pytest.mark.django_db
def test_can_create_dish(client: Client) -> None:
    # act
    url = resolve_url("dishes:create")
    response = client.post(url, data={"title": "Dish"})

    # assert
    assert response.status_code == status.HTTP_302_FOUND
    assert Dish.objects.exists()


@pytest.mark.e2e
@pytest.mark.django_db
def test_cannot_create_dish_using_empty_title(client: Client) -> None:
    # act
    url = resolve_url("dishes:create")
    response = client.post(url, data={"title": ""})

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert "This field is required" in response.content.decode()
    assert not Dish.objects.exists()


@pytest.mark.e2e
@pytest.mark.django_db
def test_cannot_create_dish_with_title_longer_than_255_characters(
        client: Client,
) -> None:
    # act
    url = resolve_url("dishes:create")
    response = client.post(url, data={"title": "_" * 260})

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert (
            "Ensure this value has at most 255 characters"
            in response.content.decode()
    )
    assert not Dish.objects.exists()
