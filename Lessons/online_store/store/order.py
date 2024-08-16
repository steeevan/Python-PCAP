class Order:
    def __init__(self, order_id:str, customer, products,total_price:float) -> None:
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.total_price = total_price
        self.status = "Processing"
    
    def display_order_info(self) -> str:
        product_info = "\n".join([product.display_product_info() for product in self.products])
        return f"Order {self.order_id} for {self.customer.name}:\n{product_info}\nTotal: ${self.total_price}\nStatus: {self.status}"
    
    def update_status(self,new_stats) -> None:
        self.status = new_stats