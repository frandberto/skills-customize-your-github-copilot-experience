# 📘 Assignment: Python Testing with pytest

## 🎯 Objective

Learn how to write automated tests with pytest to validate Python functions, cover edge cases, and build confidence when changing code.

## 📝 Tasks

### 🛠️ Write Your First Unit Tests

#### Descrição
Use the provided starter code and create unit tests for price calculations. Focus on normal behavior and predictable output.

#### Requisitos
O programa concluído deve:

- Create a test file named `test_starter_code.py`
- Add tests for `calculate_subtotal(items)` with at least 3 scenarios
- Add tests for `apply_discount(subtotal, discount_percent)` with at least 3 scenarios
- Run tests with `pytest -q` and confirm they pass


### 🛠️ Test Validation and Error Handling

#### Descrição
Expand your test suite to verify invalid input handling and boundary values.

#### Requisitos
O programa concluído deve:

- Add tests that assert `ValueError` is raised for invalid discount values
- Add tests that assert `ValueError` is raised for negative quantities or prices
- Include boundary tests for `discount_percent = 0` and `discount_percent = 100`
- Keep tests independent and readable using clear test names


### 🛠️ Add Integration-Style Tests for Order Totals

#### Descrição
Create integration-style tests for `calculate_order_total(items, discount_percent, tax_percent)` to validate full checkout behavior.

#### Requisitos
O programa concluído deve:

- Add at least 3 tests covering realistic order flows
- Validate the final total with and without discount
- Validate tax application in the final result
- Use `pytest.approx(...)` where floating-point comparison is needed
