class CashRegister:
    def __init__(self):
        self.items = []
        self.last_transaction_amount = 0
        self.total_price = 0

    def add_item(self, item_name, quantity, price_per_unit):
        item = {"name": item_name, "quantity": quantity, "price_per_unit": price_per_unit}
        self.items.append(item)
        self.last_transaction_amount = quantity * price_per_unit
        self.total_price += self.last_transaction_amount

    def calculate_discount(self, discount_percentage):
        discount_amount = (discount_percentage / 100) * self.total_price
        return discount_amount

    def apply_discount(self, discount_percentage):
        discount_amount = self.calculate_discount(discount_percentage)
        discounted_price = self.total_price - discount_amount
        return discounted_price

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total_price -= self.last_transaction_amount

    def display_items(self):
        for item in self.items:
            print(f"{item['quantity']} {item['name']} at ${item['price_per_unit']} each")

    def get_total_price(self):
        return self.total_price



