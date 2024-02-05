class Menultem:
    def __init__ ( self, name, price):
        self.name = name
        self.price = price

    def display_info():
        print(f"The item {self.name} costs {self.price}.")

class Coffee(Menultem):
    def __init__ (self, name, price, caffeine_level, customization):
        super().__init__ (name,price )
        self.caffeine_level = caffeine_level
        self.customization = customization

    def display_info(self):
        super().display_info()
        print(f"The Coffee {self.name} has {self.caffeine_level} percentage.")

    def customize_order(self,customization):
        self.customization.append(customization)
        print(f"Customization Added: {customization} ")

class ShoppingCart:
    def __init__(self, items, discount_percent=0):
        self.items = []
        self.discount_percent = discount_percent 

    def add_item(self,item):
        self.items.append(item)
        print(f"{self.items} was added to the Shopping Cart. ")

    def calculate_total(self):
        total_price = (self.items * self.discount_percent / 100)
        return total_price - self.items
        print(f"Total Price after discount: {calculate_total}")

    def apply_discount(self, discount_percent):
        self.discount_percent = discount_percent
        print(f"Discount of {discount_percent}% applied to the Shopping cart.")

coffe_item1 = Coffee("Mocha", 5.00, "Light", ["Milk"])
coffe_item1.customize_order("Extra Cream")

shopping_cart = ShoppingCart("Coffee Cake")
shopping_cart.add_item(coffe_item1)
shopping_cart.apply_discount(5)
# shopping_cart.calculate_total()


coffe_item1 = Coffee("Black Coffee", 6.00, "Very Strong", ["Sugar"])
coffe_item1.customize_order("Extra Espresso shot")


