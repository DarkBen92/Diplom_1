from unittest.mock import Mock

import pytest
from data import Data


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.name = Data.BUN_NAME
    mock.price = Data.BUN_PRICE
    return mock


@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.ingredient1_type = Data.INGREDIENT1_TYPE
    mock.ingredient1_name = Data.INGREDIENT1_NAME
    mock.ingredient1_price = Data.INGREDIENT1_PRICE
    return mock


@pytest.fixture
def mock_second_ingredient():
    mock = Mock()
    mock.ingredient2_type = Data.INGREDIENT2_TYPE
    mock.ingredient2_name = Data.INGREDIENT2_NAME
    mock.ingredient2_price = Data.INGREDIENT2_PRICE
    return mock
