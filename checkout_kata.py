class checkout_kata:

    def __init__(self):
        self.prices = {}
        self.total = 0

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        self.total += self.prices[item]

    def calc_total(self):
        return self.total

    def add_discount_rule(self, nmbr_items, amount, disc_price):
        pass
