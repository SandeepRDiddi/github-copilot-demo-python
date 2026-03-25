from training.oop_demo.flawed_inventory import inventorymanager, product


def test_product_sell_reduces_stock_and_returns_total() -> None:
    demo_product = product("Notebook", 10.0, stock=5)

    sale_total = demo_product.Sell(2)

    assert sale_total == 20.0
    assert demo_product.stock == 3


def test_inventory_total_inventory_value() -> None:
    manager = inventorymanager()
    manager.add_product("Notebook", 10.0, 5)
    manager.add_product("Pen", 2.0, 10)

    assert manager.total_inventory_value() == 70.0


def test_inventory_sell_product_updates_stock() -> None:
    manager = inventorymanager()
    manager.add_product("Notebook", 10.0, 5)

    sale_total = manager.sell_product("Notebook", 3)

    assert sale_total == 30.0
    assert manager.items[0]["stock"] == 2


def test_inventory_sell_product_raises_for_missing_product() -> None:
    manager = inventorymanager()

    try:
        manager.sell_product("Marker", 1)
    except ValueError as exc:
        assert "not found" in str(exc)
    else:
        raise AssertionError("Expected ValueError for missing product")
