
class checkout_kata:
    class Discount:
        def __init__(self, nmbr_items, disc_price):
            self.nmbr_items = nmbr_items
            self.price = disc_price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_discount_rule(self, item, nmbr_items, disc_price):
        discount = self.Discount(nmbr_items, disc_price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calc_total(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.prices[item] * cnt
        return total


