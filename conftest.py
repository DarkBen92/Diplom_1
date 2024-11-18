import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture()
def create_bun():
    bun = Bun(
        name="Булочка с корицей",
        price=100.0
    )
    return bun


@pytest.fixture()
def create_ingredient():
    ingredient = Ingredient(
        ingredient_type="Соус",
        name="Сырный",
        price=10.0
    )
    return ingredient
