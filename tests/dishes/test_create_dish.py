import pytest
from django.shortcuts import resolve_url
from django.test import Client


@pytest.mark.django_db
def test_can_create_dish(client: Client) -> None:
    # act
    url = resolve_url("dishes:create")
    response = client.post(url, data={"title": "Dish"})

    # assert
    print(response)
