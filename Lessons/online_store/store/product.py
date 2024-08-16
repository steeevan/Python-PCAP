class Product:
    def __init__(self, product_id:str, name:str, description:str, price:float, stock:int) -> None:
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity) -> None:
        self.stock += quantity

    def display_product_info(self) -> str:
        return f"{self.name}: {self.description} - ${self.price} (Stock: {self.stock})"
    

if __name__ == "__main__":
    item = Product("01","Lays","Lemon flavored",1.99,10)
    print(item)
    print(item.display_product_info())
    item.update_stock(5)
    print(item.display_product_info())