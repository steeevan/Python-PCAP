import tkinter as tk
from tkinter import ttk, messagebox
from store.product import Product

class AdminGUI(tk.Tk):
    def __init__(self, admin, user_manger) -> None:
        super().__init__()
        self.title("Admin Dashboard")
        self.geometry("500x400")
        self.admin = admin
        self.user_manager = user_manger

        self.configure(bg='#2e2e2e')

        # load products from file
        self.admin.inventory = Product.load_products_from_file()

        # Debug: print loaded products to console
        print("loaded products:")
        for product in self.admin.inventory.values():
            print(product.display_product_info())
    
        self.create_widgets()

    def create_widgets(self):
        title_lable = tk.Label(self, text=f"Welcome, {self.admin.name} (Admin)",fg='white',bg='#2e2e2e',font = ('Helvetica', 16))
        title_lable.pack(pady=10)



