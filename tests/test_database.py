import pytest

from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @pytest.mark.parametrize(
        'bun', [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]
    )
    def test_available_buns_return_buns(self, bun):
        database = Database()
        database.buns = bun
        assert database.available_buns() == bun

    @pytest.mark.parametrize(
        'ingredient', [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]
    )
    def test_available_ingredients_return_ingredients(self, ingredient):
        database = Database()
        database.ingredients = ingredient
        assert database.available_ingredients() == ingredient
