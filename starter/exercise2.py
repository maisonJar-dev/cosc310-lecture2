"""Exercise 2: A Cart class.

Implement Cart so the example at the bottom of this file behaves correctly.

  add_item(item, qty=1)  add an item; if it is already in the cart,
                         increase the quantity instead of adding a second line
  remove_item(item_id)   remove that item entirely
  clear()                empty the cart
  total()                sum of price * qty across all lines, rounded to 2dp
  __repr__()             something readable, e.g. <Cart 3 items, $27.75>

Store each line as a dictionary:
    {"item_id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "qty": 2}
"""

from venv import logger

from exercise1 import load_menu # what are we importing here? Food for thought.


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []
        self._menu = load_menu()

    def add_item(self, item: dict, qty: int = 1) -> None:
        if not item in self._menu or not item["available"]:
            return 

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
        for line in self.lines:
            if line["item_id"] == item_id: 
                self.lines.remove(line)

    def clear(self) -> None:
        if len(self.lines) == 0: return 
        self.lines.clear()

    def total(self) -> float:
        _total = 0.0
        if len(self.lines) == 0:
            return
        else:
            for item in self.lines:
                _total += item["price"] * item["qty"]

        return round(_total, 2)

    def __repr__(self) -> str:
        if len(self.lines) == 0: return "Empty"

        cart = "=======CART=======" 
        
        for item in self.lines:
            cart += (f"\nID: {item["item_id"]}, Name: {item["name"]}, Price: {item["price"]}, Quanitity: {item["qty"]}")
        cart += "\n=================="
        return cart


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]
    ramen = menu[0]

    cart = Cart()
    cart.add_item(gyoza, 2)
    cart.add_item(gyoza, 1)      # should become qty 3, NOT a second line
    cart.add_item(ramen, 1)
    
    print(cart)                  # <Cart 2 items, $40.50>
    print(len(cart.lines))       # 2
    print(cart.total())          # 40.5
    
