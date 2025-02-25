from decimal import Decimal

from faker import Faker

from apps.orders import services


def make_order() -> int:
    faker = Faker()
    return services.create_order(
        order_dto={"table_number": 10},
        item_list_dto=[
            {
                "dish": faker.word(),
                "price": Decimal(faker.random_int(1, 10)),
                "quantity": faker.random_int(1, 10),
            }
        ],
    )
