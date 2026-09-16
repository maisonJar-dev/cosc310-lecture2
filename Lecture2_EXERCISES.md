# Lecture 2 Exercises - Python & Git

There are 5 exercises in total.

Starter files are in `starter/`. Copy that folder somewhere of your own before you
begin.

**Setup**

```bash
cd starter
python -m venv .venv          # python3 on macOS/Linux
.venv\Scripts\Activate.ps1    # source .venv/bin/activate on macOS/Linux
pip install pytest
```

You should see `(.venv)` in your prompt before continuing.

---

## Exercise 1: Menu filtering

**File:** `starter/exercise1.py`

`starter/data/menu.json` holds a small restaurant menu. Write code that:

1. Loads the file with the `json` module.
2. Prints every item that is available **and** costs less than $10.00.
3. Prints them sorted by price, cheapest first, formatted like:
   ```
   Green Tea            $3.25
   Gyoza (6 pc)         $8.00
   ```

**Constraints**

- Use an f-string for the output.
- Add type hints to every function you write.

**Hints**

- `sorted(items, key=lambda i: i["price"])`
- `f"{name:<20} ${price:.2f}"` left-pads the name to 20 characters.

**Stretch:** make it a function `available_under(menu: list[dict], limit: float) -> list[dict]`
so the price limit is not hard-coded.

---

## Exercise 2: A Cart class

**File:** `starter/exercise2.py`

Write a `Cart` class with:

| Method | Behaviour |
|---|---|
| `add_item(item: dict, qty: int = 1)` | Add an item. If it is already in the cart, increase its quantity instead of adding a duplicate line. |
| `remove_item(item_id: int)` | Remove that item entirely. |
| `clear()` | Empty the cart. |
| `total() -> float` | Sum of `price × qty` for every line, rounded to 2 decimal places. |
| `__repr__() -> str` | Something readable, e.g. `<Cart 3 items, $27.75>` |

**Requirements**

- Store lines as dictionaries: `{"item_id": 1, "name": "...", "price": 16.50, "qty": 2}`.
- Type-hint every method.
- `total()` must round **once**, at the end.

**Check and Test**

```python
cart = Cart()
cart.add_item(gyoza, 2)
cart.add_item(gyoza, 1)     # should become qty 3, not a second line
print(len(cart.lines))      # 1
print(cart.total())         # 24.0
```

---

## Exercise 3: Enforce a business rule

**File:** `starter/exercise3.py`

Extend your `Cart` so invalid operations are rejected **by the cart**.

1. Define `class OutOfStockError(Exception)`.
2. In `add_item`, raise:
   - `ValueError` if `qty < 1`
   - `OutOfStockError` if the item's `available` field is `False`
3. In `remove_item`, raise `KeyError` if that item is not in the cart.
4. Demonstrate each one with a `try` / `except` that prints a readable message.

**Why this matters:** #5 of the project specification says a business rule is not
implemented merely because the frontend prevents the action. The rule has to live in
the code that owns the data.

---

## Exercise 4: Ship it through Git

This is an interesting exercise.

1. Create a new repository on GitHub called `cosc310-lecture2`. Do **not** add a README yet.
2. Set it up locally, on `main`:
   ```bash
   git init
   git add .gitignore README.md
   git commit -m "Initial project structure"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
   Copy `starter/.gitignore` in **before** your first commit. Your `.venv` folder must
   never appear on GitHub.
3. Create a feature branch:
   ```bash
   git checkout -b feature/1-cart
   ```
4. Add your exercise 1–3 solutions. Make **at least three separate commits** with
   meaningful messages. Not one commit called "done".
5. Push the branch and open a **pull request** against `main`. In the description,
   state what you built, which business rules you enforced, and where they are
   enforced.
6. Just for this assignment, you can merge your own pull request.
7. Merge it, and update your local `main`:
   ```bash
   git checkout main
   git pull
   ```

**Submit:** the URL of your merged pull request.

---

## Exercise 5: Your first tests

**File:** `starter/tests/test_cart.py`

Some tests are written for you and currently fail. Make them pass, then add your own:

1. A test that a cart total is correct for multiple items.
2. A test that adding the same item twice increases the quantity rather than creating
   a second line.
3. A test that `add_item` with `qty=0` raises `ValueError`.
4. A test that an unavailable item raises `OutOfStockError`.

```bash
pytest -v
```

Include the passing output in your pull request description.

**Hint for the rejection cases:**

```python
import pytest

def test_rejects_zero_quantity():
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_item(GYOZA, 0)
```

---
