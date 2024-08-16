import hashlib
from store.customer import Customer
from store.admin import Admin

class UserManager:
    def __init__(self) -> None:
        self.users = {}
        self.orders = []

    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self,user_id,name, email, password, user_type="Customer"):
        if email in self.users:
            raise ValueError("User already exists")
        hashed_password = self.hash_password(password)
        if user_type == "Customer":
            user = Customer(user_id,name,email,hashed_password)
        elif user_type == "Admin":
            user = Admin(user_id,name,email,hashed_password)
        else:
            raise ValueError("Invalid User Type")
        
        self.users[email] = user
        return user
    
    def autheticate_user(self,email,password):
        hashed_password = self.hash_password(password)
        user = self.users.get(email)
        if user and user.password == hashed_password:
            return user
        else:
            raise ValueError("Invalid email or password")

    def add_order(self, order):
        self.orders.append(order)
        self.save_order_to_file(order)

    def save_order_to_file(self,order):
        with open("data/orders.txt","a") as file:
            file.write(f"{order.order_id},{order.customer_name}.{order.total_price},{order.status}\n")
            