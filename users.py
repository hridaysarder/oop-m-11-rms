class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.orders = []
    
    def view_menu(self, menu):
        print("\n--- Restaurant Menu ---")
        for item, price in menu.items():
            print(f"{item}: ${price}")
    
    def place_order(self, menu):
        self.view_menu(menu)
        item = input("\nEnter the item: ").strip()
        if item in menu:
            if self.balance >= menu[item]:
                self.orders.append(item)
                self.balance -= menu[item]
                print(f"Order placed for {item}. Remaining balance: ${self.balance: }")
            else:
                print("Insufficient balance.")
        else:
            print("Item not available in the menu.")
    
    def check_balance(self):
        print(f"\nAvailable balance: ${self.balance: }")
    
    def add_funds(self):
        try:
            amount = float(input("Enter amount to add: "))
            if amount > 0:
                self.balance += amount
                print(f"Funds added: ${amount: }. New balance: ${self.balance: }")
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Invalid amount.")
    
    def view_past_orders(self):
        print("\n--- Past Orders ---")
        if self.orders:
            for order in self.orders:
                print(order)
        else:
            print("No past orders.")

class Admin:
    def __init__(self):
        self.menu = {}
        self.customers = {}
    
    def add_menu_item(self):
        item = input("Enter item name: ").strip()
        try:
            price = float(input(f"Enter price for {item}: "))
            self.menu[item] = price
            print(f"Item '{item}' added with price ${price:.2f}")
        except ValueError:
            print("Invalid price.")
    
    def remove_menu_item(self):
        item = input("Enter item name to remove: ").strip()
        if item in self.menu:
            del self.menu[item]
            print(f"Item '{item}' removed from the menu.")
        else:
            print(f"'{item}' not found in the menu.")
    
    def view_menu(self):
        print("\n--- Restaurant Menu ---")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")
    
    def add_customer(self):
        name = input("Enter customer name: ").strip()
        email = input("Enter customer email: ").strip()
        address = input("Enter customer address: ").strip()
        if email not in self.customers:
            self.customers[email] = Customer(name, email, address)
            print(f"Customer '{name}' added.")
        else:
            print("Customer with this email already exists.")
    
    def remove_customer(self):
        email = input("Enter customer email to remove: ").strip()
        if email in self.customers:
            del self.customers[email]
            print(f"Customer with email '{email}' removed.")
        else:
            print("Customer not found.")
    
    def view_customers(self):
        print("\n--- All Customers ---")
        if self.customers:
            for email, customer in self.customers.items():
                print(f"Name: {customer.name}, Email: {email}, Address: {customer.address}")
        else:
            print("No customers available.")

def main():
    admin = Admin()
    
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            admin_name = input("Enter Admin Name: ").strip()
            print(f"\nWelcome Admin {admin_name}")
            while True:
                print("\n--- Admin Menu ---")
                print("1. Create Customer Account")
                print("2. Remove Customer Account")
                print("3. View All Customers")
                print("4. Manage Restaurant Menu")
                print("5. Exit")
                admin_choice = input("Select an option: ").strip()
                
                if admin_choice == "1":
                    admin.add_customer()
                elif admin_choice == "2":
                    admin.remove_customer()
                elif admin_choice == "3":
                    admin.view_customers()
                elif admin_choice == "4":
                    print("\n--- Manage Restaurant Menu ---")
                    print("1. Add Menu Item")
                    print("2. Remove Menu Item")
                    print("3. View Menu")
                    menu_choice = input("Select an option: ").strip()
                    
                    if menu_choice == "1":
                        admin.add_menu_item()
                    elif menu_choice == "2":
                        admin.remove_menu_item()
                    elif menu_choice == "3":
                        admin.view_menu()
                    else:
                        print("Invalid option.")
                elif admin_choice == "5":
                    break
                else:
                    print("Invalid option.")
        
        elif choice == "2":
            customer_name = input("Enter customer name: ").strip()
            email = input("Enter customer email: ").strip()
            if email in admin.customers:
                customer = admin.customers[email]
                print(f"\n--- {customer_name}'s Menu ---")
                while True:
                    print("\n1. View Restaurant Menu")
                    print("2. View Balance")
                    print("3. Add Balance")
                    print("4. Place Order")
                    print("5. View Orders")
                    print("6. Exit")
                    customer_choice = input("Select an option: ").strip()
                    
                    if customer_choice == "1":
                        customer.view_menu(admin.menu)
                    elif customer_choice == "2":
                        customer.check_balance()
                    elif customer_choice == "3":
                        customer.add_funds()
                    elif customer_choice == "4":
                        customer.place_order(admin.menu)
                    elif customer_choice == "5":
                        customer.view_past_orders()
                    elif customer_choice == "6":
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Customer not found.")
        
        elif choice == "3":
            print("Exiting the system.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
