from data import Data
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_type_ingredient_return_type_ingredient(self):
        create_ingredient = Ingredient(
            name=Data.INGREDIENT1_NAME,
            price=Data.INGREDIENT1_PRICE,
            ingredient_type=Data.INGREDIENT1_TYPE)
        assert create_ingredient.get_type() == "SAUCE"

    def test_get_name_ingredient_return_name_ingredient(self):
        create_ingredient = Ingredient(
            name=Data.INGREDIENT1_NAME,
            price=Data.INGREDIENT1_PRICE,
            ingredient_type=Data.INGREDIENT1_TYPE)
        assert create_ingredient.get_name() == "1000 островов"

    def test_get_price_ingredient_return_price_ingredient(self):
        create_ingredient = Ingredient(
            name=Data.INGREDIENT1_NAME,
            price=Data.INGREDIENT1_PRICE,
            ingredient_type=Data.INGREDIENT1_TYPE)
        assert create_ingredient.get_price() == 10.0
