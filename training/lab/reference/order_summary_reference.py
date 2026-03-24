"""Reference implementation for the GitHub Copilot training lab."""

from __future__ import annotations


def normalize_order_items(items: list[dict]) -> list[dict]:
    cleaned_items: list[dict] = []

    for item in items:
        name = str(item.get("name", "")).strip()
        quantity = item.get("quantity", 1)
        unit_price = float(item.get("unit_price", 0.0))

        if not isinstance(quantity, int) or quantity < 1:
            quantity = 1

        if unit_price < 0:
            raise ValueError("unit_price cannot be negative")

        cleaned_items.append(
            {
                "name": name,
                "quantity": quantity,
                "unit_price": unit_price,
            }
        )

    return cleaned_items


def build_order_summary(items: list[dict], tax_rate: float = 0.1) -> dict:
    normalized = normalize_order_items(items)
    subtotal = round(
        sum(item["quantity"] * item["unit_price"] for item in normalized), 2
    )
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)

    return {
        "item_count": sum(item["quantity"] for item in normalized),
        "item_names": sorted({item["name"] for item in normalized}),
        "subtotal": subtotal,
        "tax": tax,
        "total": total,
    }
