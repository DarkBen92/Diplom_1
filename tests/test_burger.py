from unittest.mock import patch

from conftest import mock_bun, mock_ingredient, mock_second_ingredient
from praktikum.burger import Burger
from data import Data


class TestBurger:
    def test_set_buns_burger_return_name_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun.name)
        assert burger.bun == 'Булочка с корицей'

    def test_add_ingredient_burger_add_name_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredient1_name)
        assert burger.ingredients == ['1000 островов']

    def test_remove_ingredient_burger_empty_list(self, mock_ingredient, mock_second_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredient1_name)
        burger.add_ingredient(mock_second_ingredient.ingredient2_name)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_second_ingredient.ingredient2_name]

    def test_move_ingredient_burger_moved_ingredient(self, mock_ingredient, mock_second_ingredient):
        burger = Burger()
        burger.ingredients = [mock_ingredient.ingredient1_name, mock_second_ingredient.ingredient2_name]
        burger.move_ingredient(0,  1)
        assert burger.ingredients == ['Курица', '1000 островов']

    def test_get_price_burger_return_price_burger(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.bun = mock_bun
        burger.bun.get_price.return_value = Data.BUN_PRICE
        mock_ingredient.get_price.return_value = Data.INGREDIENT1_PRICE
        burger.add_ingredient(mock_ingredient)
        expected_price = Data.BUN_PRICE * 2 + Data.INGREDIENT1_PRICE
        assert burger.get_price() == expected_price

    @patch("praktikum.burger.Burger.get_price", return_value=Data.BUN_PRICE)
    def test_get_receipt_burger_return_receipt(self, mock_bun, mock_ingredient, mock_second_ingredient):
        burger = Burger()
        burger.bun = mock_bun
        burger.bun.get_name.return_value = Data.BUN_NAME
        mock_ingredient.get_type.return_value = Data.INGREDIENT1_TYPE
        mock_ingredient.get_name.return_value = Data.INGREDIENT1_NAME
        mock_second_ingredient.get_type.return_value = Data.INGREDIENT2_TYPE
        mock_second_ingredient.get_name.return_value = Data.INGREDIENT2_NAME
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_second_ingredient)
        expected = (
            '(==== Булочка с корицей ====)\n'
            '= sauce 1000 островов =\n'
            '= filling Курица =\n'
            '(==== Булочка с корицей ====)\n'
            '\n'
            'Price: 100.0'
        )
        assert burger.get_receipt() == expected
