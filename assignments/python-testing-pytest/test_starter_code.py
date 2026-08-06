import pytest

from starter_code import (
    apply_discount,
    calculate_order_total,
    calculate_subtotal,
)


def test_calculate_subtotal_basic_case():
    items = [
        {"name": "Notebook", "price": 10.0, "quantity": 2},
        {"name": "Pen", "price": 2.5, "quantity": 4},
    ]

    assert calculate_subtotal(items) == 30.0


# TODO(student): add at least 2 more tests for calculate_subtotal
# TODO(student): add discount validation tests with pytest.raises(ValueError)
# TODO(student): add integration-style tests for calculate_order_total

def test_apply_discount_boundary_zero_percent():
    assert apply_discount(100.0, 0) == 100.0


def test_calculate_order_total_with_tax_only():
    items = [{"name": "Book", "price": 50.0, "quantity": 1}]
    total = calculate_order_total(items, discount_percent=0, tax_percent=10)

    assert total == pytest.approx(55.0)
