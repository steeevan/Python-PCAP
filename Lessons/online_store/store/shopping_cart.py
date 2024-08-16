class ShoppingCart:
    def __init__(self) -> None:
        self.items = {}

    def add_product(self,product, quantity) -> None:
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
    
    def remove_product(self,product) -> None:
        if product in self.items:
            del self.items[product]

    def view_cart(self) -> str:
        return "\n".join([f"{product.name}: {quantity}" for product,quantity in self.items.items()])
    
    def caculate_total(self) -> float:
        return sum([product.price * quantity for product, quantity in self.items.items()])
    
    def clear_cart(self) -> None:
        self.items = {}


    