from conftest import create_bun
from praktikum.burger import Burger
from unittest.mock import Mock


class TestBurger:
    def test_set_buns_burger(self, create_bun):
        burger = Burger()

        burger.set_buns(create_bun)
        assert burger.bun == 1

    def test_add_ingredient_burger(self):
        burger = Burger()

        mock_ingredient = Mock()
        mock_ingredient.Ingredient('SAUCE','1000 островов', 10.0)
        # mock_ingredient.type = 'SAUCE'
        # mock_ingredient.name = '1000 островов'
        # mock_ingredient.price = 10.0
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == 3
