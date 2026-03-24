"""Starter exercise for GitHub Copilot training."""

from __future__ import annotations


def normalize_order_items(items: list[dict]) -> list[dict]:
    """Return cleaned order items.

    Desired behavior:
    - keep only ``name``, ``quantity``, and ``unit_price``
    - trim whitespace around ``name``
    - default missing or invalid ``quantity`` to 1
    - raise ``ValueError`` when ``unit_price`` is negative
    """
    raise NotImplementedError("Implement this during the lab with Copilot.")


def build_order_summary(items: list[dict], tax_rate: float = 0.1) -> dict:
    """Return a simple order summary dictionary.

    Expected keys:
    - ``item_count``: total number of units across all items
    - ``item_names``: alphabetically sorted unique names
    - ``subtotal``: sum of quantity * unit_price
    - ``tax``: subtotal * tax_rate
    - ``total``: subtotal + tax

    Notes:
    - use normalized items before calculating
    - round monetary values to 2 decimal places
    """
    raise NotImplementedError("Implement this during the lab with Copilot.")
