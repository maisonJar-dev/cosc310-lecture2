"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    def __init__(self, name, msg = "is not available"):
        self.msg = msg
        self.name = name 
        super().__init__(self.msg)
    def __str__(self):
        return f"Item {self.name} {self.msg}"

class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        """Sanity check parameters and increase cart or update quantity respectively"""
        # TODO: validate FIRST, then mutate.
        #   if qty < 1:                 raise ValueError(...)
        #   if not item["available"]:   raise OutOfStockError(...)
        if not item["available"]:
            raise OutOfStockError(item["name"])
        if qty < 1:
            raise ValueError(f"Quanity Input ({qty}) was less than 1")
        
        item_id = item["id"]

        for line in self.lines:
            if line["item_id"] == item_id: 
                line["qty"] += qty
                return
    
        self.lines.append({"item_id": item_id, 
                                "name": item["name"], 
                                "price": item["price"], 
                                "qty": qty})

    def remove_item(self, item_id: int) -> None:
        """Remove item if it exists"""
        for line in self.lines:
            if line["item_id"] == item_id: 
                self.lines.remove(line)
                return
        raise KeyError("Item not in cart")

    def total(self) -> float:
        """Return total of items in cart"""
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        """Class prinout"""
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

    cart.add_item(gyoza, 1)
    print(cart)

    try:
        cart.add_item(gyoza, 0)
    except ValueError as e:
        print(f"Rejected: {e}")

    try:
        cart.remove_item(1200)
    except KeyError as e:
        print(f"Rejected: {e}")

    try:
        cart.add_item(miso, 0)
    except OutOfStockError as e:
        print(f"Rejected: {e}")
