from store.user import User
from store.shopping_cart import ShoppingCart
from store.order import Order

class Customer(User):
    def __init__(self, user_id: str, name: str, email: str, password: str) -> None:
        super().__init__(user_id, name, email, password)
        self.shopping_cart = ShoppingCart()
        self.order_history = []

    def add_to_cart(self, product, quantity) -> None:
        self.shopping_cart.add_product(product,quantity)

    def remove_from_cart(self,product) -> None:
        self.shopping_cart.remove_product(product)
    
    def view_cart(self) -> str:
        return self.shopping_cart.view_cart()
    
    def checkout(self, user_manager) -> Order:
        total_price = self.shopping_cart.caculate_total()
        new_order = Order(len(user_manager.orders) + 1, self, list(self.shopping_cart.items.keys()),total_price)
        self.order_history.append(new_order)
        self.shopping_cart.clear_cart()
        return new_order