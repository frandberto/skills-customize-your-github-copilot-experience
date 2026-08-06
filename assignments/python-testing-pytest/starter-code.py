"""Starter code for the Python Testing with pytest assignment.

Students should complete TODOs and then create tests in test_starter_code.py.
"""


def calculate_subtotal(items):
    """Calculate subtotal from a list of items.

    Expected item format:
    {
        "name": str,
        "price": float,
        "quantity": int,
    }
    """
    subtotal = 0.0
    for item in items:
        price = item["price"]
        quantity = item["quantity"]

        if price < 0:
            raise ValueError("price cannot be negative")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        subtotal += price * quantity

    return subtotal


def apply_discount(subtotal, discount_percent):
    """Apply discount percentage to subtotal and return discounted value."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100")

    return subtotal * (1 - discount_percent / 100)


def calculate_tax(amount, tax_percent):
    """Return tax amount for a given amount and tax percentage."""
    if tax_percent < 0:
        raise ValueError("tax_percent cannot be negative")
    return amount * (tax_percent / 100)


def calculate_order_total(items, discount_percent=0, tax_percent=0):
    """Calculate final total after discount and tax."""
    subtotal = calculate_subtotal(items)
    discounted = apply_discount(subtotal, discount_percent)
    tax = calculate_tax(discounted, tax_percent)
    return discounted + tax
