from data import Data
from praktikum.bun import Bun


class TestBun:
    def test_get_name_bun_return_name_bun(self):
        create_bun = Bun(name=Data.BUN_NAME, price=Data.BUN_PRICE)
        assert create_bun.get_name() == "Булочка с корицей"

    def test_get_price_bun_return_price_bun(self):
        create_bun = Bun(name=Data.BUN_NAME, price=Data.BUN_PRICE)
        assert create_bun.get_price() == 100.0
