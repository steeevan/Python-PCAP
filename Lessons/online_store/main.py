from store.product import Product
from store.user_manager import UserManager
from store.payment import Payment

def main():

    # Initialize usermanagers
    big_boss = UserManager()

    # Register a new customer
    caden = big_boss.register_user(1,"Caden", "caden@example.com", "space")

    print(caden.display_user_info())

    # Register admin
    admin = big_boss.register_user(2,"Admin","admin@example.com", "adminpassword","Admin")


    # autheticate users

    try:
        logged_in_customer = big_boss.autheticate_user("caden@example.com","space")
        print(f"Logged in as {logged_in_customer.display_user_info()}")
    except ValueError as e:
        print(e)

    try:
        logged_in_admin = big_boss.autheticate_user("admin@example.com","adminpassword")
        print(f"Logged in as {logged_in_admin.display_user_info()}")
    except ValueError as e:
        print(e)
    
    # Customer interacts with the store
    laptop = Product(1,"Laptop Dell X100 G5"," A high perfomance small dedicated working laptop",0.99, 100)
    phone = Product(2,"Pearphone","The opposite of an apple phone so its 100x better",0.49,10)

    admin.add_product(laptop)
    admin.add_product(phone)

    caden.add_to_cart(phone,2)
    caden.add_to_cart(laptop,1)

    print(f"Caden's cart: \n{caden.view_cart()}")

    # Checkout and create an order
    order = caden.checkout(big_boss)
    print(order.display_order_info())
    
    # process a payment for the order
    payment = Payment(1,order,order.total_price,"Robucks")
    if payment.process_payment():
        print(payment.display_payment_info())
        order.update_status("Completed")
        print(payment.display_payment_info())
    else:
        print("Decline")
    # admine views all orders
    orders = [order]
    print(admin.view_order(orders))



main()