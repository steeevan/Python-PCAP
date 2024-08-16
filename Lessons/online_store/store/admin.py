from store.user import User

class Admin(User):
    def __init__(self, user_id: str, name: str, email: str, password: str) -> None:
        super().__init__(user_id, name, email, password)
        self.inventory = {}
    
    def add_product(self,product) -> None:
        self.inventory[product.product_id] = product
    
    def remove_product(self,product_id) -> None:
        if product_id in self.inventory:
            del self.inventory[product_id]
    
    def update_product(self,product_id, **kwargs) -> None:
        if product_id in self.inventory:
            product = self.inventory[product_id]
            for key, value in kwargs.items():
                if hasattr(product,key):
                    setattr(product,key,value)
    
    def view_order(self,orders) -> str:
        return "\n".join([order.display_order_info() for order in orders])
    