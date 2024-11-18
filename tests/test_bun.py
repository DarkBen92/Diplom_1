from conftest import create_bun


class TestBun:
    def test_get_name_bun(self, create_bun):
        assert create_bun.get_name() == "Булочка с корицей"

    def test_get_price_bun(self, create_bun):
        assert create_bun.get_price() == 100.0
