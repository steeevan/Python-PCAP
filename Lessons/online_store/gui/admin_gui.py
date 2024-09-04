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

        button_style = ttk.Style()
        button_style.configure('TButton',font = ('Helvetica',12), padding=6)

        add_product_btn = ttk.Button(self,text="Add Product" ,command=self.add_product)
        add_product_btn.pack(pady=5)

        modify_product_btn = ttk.Button(self, text="Modify Product", command=self.modify_product)
        modify_product_btn.pack(pady=5)

        remove_product_btn = ttk.Button(self,text="Remove Product", command=self.remove_product)
        remove_product_btn.pack(pady=5)

        view_order_btn = ttk.Button(self,text="View Orders", command=self.view_orders)
        view_order_btn.pack(pady=5)

    def add_product(self):
        self.product_window("Add Product")
    
    def modify_product(self):
        self.list_products_window("Modify Product", self.modify_product_action)
    
    def remove_product(self):
        self.list_products_window("Remove Product", self.remove_product_action)

    def view_orders(self):
        orders_window = tk.Toplevel(self)
        orders_window.title("Orders")
        orders_window.geometry("400x300")
        orders_window.configure(bg='#2e2e2e')
        for order in self.user_manager.orders:
            order_label = tk.Label(orders_window, text=order.display_order_info(),fg='white',bg='#2e2e2e')
            order_label.pack()

    def product_window(self,title,product=None):
        product_win = tk.Toplevel(self)
        product_win.title(title)
        product_win.geometry("350x300")
        product_win.configure(bg="#2e2e2e")

        tk.Label(product_win,text="Product ID:", fg='white',bg='#2e2e2e').pack(pady=5)
        product_id_entry = tk.Entry(product_win)
        product_id_entry.pack(pady=5)

        tk.Label(product_win, text="Name:", fg='white', bg='#2e2e2e').pack(pady=5)
        name_entry = tk.Entry(product_win)
        name_entry.pack(pady=5)

        tk.Label(product_win, text="Description:", fg='white', bg='#2e2e2e').pack(pady=5)
        description_entry = tk.Entry(product_win)
        description_entry.pack(pady=5)

        tk.Label(product_win, text="Price:", fg='white', bg='#2e2e2e').pack(pady=5)
        price_entry = tk.Entry(product_win)
        price_entry.pack(pady=5)

        tk.Label(product_win, text="Stock:", fg='white', bg='#2e2e2e').pack(pady=5)
        stock_entry = tk.Entry(product_win)
        stock_entry.pack(pady=5)

        if product:
            product_id_entry.insert(0,product.product_id)
            name_entry.insert(0,product.name)
            description_entry.insert(0,product.description)
            price_entry.insert(0,product.price)
            stock_entry.insert(0,product.stock)

        action_button = ttk.Button(product_win, text=title.split()[0],
                                   command=lambda: self.add_or_modify_product(product_id_entry,name_entry,description_entry,price_entry,stock_entry,product))
        action_button.pack(pady=20)

    def list_products_window(self,title,action):
        product_list_win = tk.Toplevel(self)
        product_list_win.title(title)
        product_list_win.geometry("350x300")
        product_list_win.configure(bg="#2e2e2e")

        tk.Label(product_list_win,text="Select Product:", fg='white',bg='#2e2e2e').pack(pady=5)

        if not self.admin.inventory:
            tk.Label(product_list_win,text="No Products available!", fg='white', bg='#2e2e2e').pack(pady=20)
            return

        product_combobox = ttk.Combobox(product_list_win,values=[f"{p.product_id}: {p.name}" for p in self.admin.inventory.values()])
        product_combobox.pack(pady=10)

        def on_select():
            selected_product = product_combobox.get().split(":")[0]
            product = self.admin.inventory.get(int(selected_product))
            action(product)

        action_button = ttk.Button(product_list_win, text=title.split()[0], command=on_select)
        action_button.pack(pady=20)

    def add_or_modify_product(self,product_id_entry, name_entry, description_entry, price_entry,stock_entry,product=None):
        product_id = int(product_id_entry.get())
        name = name_entry.get()
        description = description_entry.get()
        price = float(price_entry.get())
        stock = int(stock_entry.get())

        if product:
            self.admin.update_product(product_id,name=name,description=description,price=price,stock=stock)
        else:
            new_product = Product(product_id,name,description,price,stock)
            self.admin.add_product(new_product)
        
        # save updaed inventory to file
        Product.save_products_to_file(self.admin.inventory)

        messagebox.showinfo("Success", f"Product {product_id} {'added' if not product else 'modified'} succesfully!")


    def remove_product_action(self,product):
        self.admin.remove_product(product.product_id)

        Product.save_products_to_file(self.admin.invetory)

        messagebox.showinfo("Success", f"Product {product.product_id} removed successfully!")

    def modify_product_action(self,product):
        self.product_window("Modify Product", product)
        


