import pytest
from django.shortcuts import resolve_url
from django.test import Client
from faker import Faker

# @pytest.mark.django_db
# def test_can_get_dish(client: Client, faker: Faker) -> None:
#     # arrange
#     url = resolve_url("dishes:create")
#     title = faker.text(max_nb_chars=20)
#     response = client.post(url, data={"title": title})
#
#     # act
#     url = resolve_url("dishes:<>")
#     response = client.get(response)
