class Payment:
    def __init__(self,payment_id,order,amount,payment_method) -> None:
        self.payment_id = payment_id
        self.order = order
        self.amount = amount
        self.payment_method = payment_method
        self.status = "Pending"

    def process_payment(self) -> bool:
        # simulare payment processing
        self.status = "Completed"
        return True

    def display_payment_info(self):
        return f"Payment {self.payment_id} for Order {self.order.order_id}: #{self.amount} via {self.payment_method} - {self.status}"