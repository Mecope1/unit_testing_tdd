
class checkout_kata:
    class Discount:
        def __init__(self, nmbr_items, price):
            self.nmbr_items = nmbr_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.total = 0

    def add_discount_rule(self, item, nmbr_items, disc_price):
        discount = self.Discount(nmbr_items, disc_price)
        self.discounts[item] = discount

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        self.total += self.prices[item]

    def calc_total(self):
        return self.total

