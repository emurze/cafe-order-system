import pytest
from django.shortcuts import resolve_url
from django.test import Client
from faker import Faker
from rest_framework import status


@pytest.mark.django_db
def test_can_get_dish(client: Client, faker: Faker) -> None:
    # arrange
    url = resolve_url("dishes:create")
    title = faker.text(max_nb_chars=20)
    client.post(url, data={"title": title})

    # act
    url = resolve_url("dishes:list")
    response = client.get(url)

    # assert
    assert response.status_code == status.HTTP_200_OK
