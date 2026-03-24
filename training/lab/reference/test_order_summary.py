from training.lab.reference.order_summary_reference import (
    build_order_summary,
    normalize_order_items,
)


def test_normalize_order_items_trims_and_filters_fields() -> None:
    items = [
        {
            "name": "  Notebook  ",
            "quantity": 2,
            "unit_price": 4.5,
            "category": "office",
        }
    ]

    assert normalize_order_items(items) == [
        {"name": "Notebook", "quantity": 2, "unit_price": 4.5}
    ]


def test_normalize_order_items_defaults_invalid_quantity() -> None:
    items = [{"name": "Pen", "quantity": 0, "unit_price": 1.25}]

    assert normalize_order_items(items) == [
        {"name": "Pen", "quantity": 1, "unit_price": 1.25}
    ]


def test_normalize_order_items_rejects_negative_price() -> None:
    items = [{"name": "Marker", "quantity": 1, "unit_price": -3.0}]

    try:
        normalize_order_items(items)
    except ValueError as exc:
        assert "unit_price" in str(exc)
    else:
        raise AssertionError("Expected ValueError for negative unit_price")


def test_build_order_summary_returns_expected_totals() -> None:
    items = [
        {"name": "Notebook", "quantity": 2, "unit_price": 4.5},
        {"name": "Pen", "quantity": 3, "unit_price": 1.25},
        {"name": "Notebook", "quantity": 1, "unit_price": 4.5},
    ]

    summary = build_order_summary(items, tax_rate=0.1)

    assert summary == {
        "item_count": 6,
        "item_names": ["Notebook", "Pen"],
        "subtotal": 17.25,
        "tax": 1.73,
        "total": 18.98,
    }


def test_build_order_summary_handles_empty_input() -> None:
    assert build_order_summary([]) == {
        "item_count": 0,
        "item_names": [],
        "subtotal": 0.0,
        "tax": 0.0,
        "total": 0.0,
    }
