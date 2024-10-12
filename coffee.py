class CoffeeShopRobot:
    def __init__(self):
        self.menu = {
            "1": {"name": "Espresso", "price": 100},
            "2": {"name": "Latte", "price": 120},
            "3": {"name": "Cappuccino", "price": 160},
            "4": {"name": "Americano", "price": 110},
            "5": {"name": "Mocha", "price": 140},
            "6": {"name": "Flat White", "price": 130},
            "7": {"name": "Macchiato", "price": 150},
            "8": {"name": "Filter Coffee", "price": 90},
            "9": {"name": "Black Forest Cake", "price": 200},
            "10": {"name": "Red Velvet Cake", "price": 180},
            "11": {"name": "Chocolate Truffle Cake", "price": 220},
            "12": {"name": "Blueberry Cheesecake", "price": 190},
            "13": {"name": "Glazed Donut", "price": 50},
            "14": {"name": "Chocolate Donut", "price": 60},
            "15": {"name": "Strawberry Donut", "price": 55},
            "16": {"name": "Cinnamon Roll", "price": 70},
            "17": {"name": "Coffee Cake", "price": 80},
            "18": {"name": "Banana Bread", "price": 75},
            "19": {"name": "Blueberry Muffin", "price": 65},
            "20": {"name": "Chocolate Chip Cookie", "price": 40}
        }
        self.order = []

    def display_menu(self):
        print("Menu:")
        for key, item in self.menu.items():
            print(f"{key}. {item['name']} - Rs{item['price']}")

    def take_order(self):
        while True:
            choice = input("Enter item number to order (or 'done' to finish): ")
            if choice.lower() == 'done':
                break
            elif choice in self.menu:
                self.order.append(self.menu[choice])
                print(f"{self.menu[choice]['name']} added to order.")
            else:
                print("Invalid choice. Please select a valid item.")

    def calculate_total(self):
        total = sum(item['price'] for item in self.order)
        return total

    def print_receipt(self):
        print("Receipt:")
        for item in self.order:
            print(f"{item['name']}: Rs{item['price']}")
        print(f"Total: Rs{self.calculate_total()}")

    def serve_customer(self):
        print("Welcome to the Coffee Shop!")
        self.display_menu()
        self.take_order()
        if self.order:
            print("\nYour order:")
            self.print_receipt()
            print("\nThank you for your order! Enjoy your coffee!")
        else:
            print("\nNo items ordered. Goodbye!")


if __name__ == "__main__":
    robot = CoffeeShopRobot()
    robot.serve_customer()
