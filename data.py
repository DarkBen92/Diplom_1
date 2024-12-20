from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data:
    BUN_NAME = "Булочка с корицей"
    BUN_PRICE = 100.0
    INGREDIENT1_TYPE = INGREDIENT_TYPE_SAUCE
    INGREDIENT1_NAME = "1000 островов"
    INGREDIENT1_PRICE = 10.0
    INGREDIENT1 = INGREDIENT1_TYPE, INGREDIENT1_NAME, INGREDIENT1_PRICE
    INGREDIENT2_TYPE = INGREDIENT_TYPE_FILLING
    INGREDIENT2_NAME = "Курица"
    INGREDIENT2_PRICE = 70.0
    INGREDIENT2 = [INGREDIENT2_TYPE, INGREDIENT2_NAME, INGREDIENT2_PRICE]
