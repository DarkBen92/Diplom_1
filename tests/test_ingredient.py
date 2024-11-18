from conftest import create_ingredient


class TestIngredient:
    def test_get_type_ingredient(self, create_ingredient):
        assert create_ingredient.get_type() == "Соус"

    def test_get_name_ingredient(self, create_ingredient):
        assert create_ingredient.get_name() == "Сырный"

    def test_get_price_ingredient(self, create_ingredient):
        assert create_ingredient.get_price() == 10.0
