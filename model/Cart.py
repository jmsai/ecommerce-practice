class Cart:
    def __init__(self, items, payment_total, customer_id):
        self.cart_id = 1
        self.items = items
        self.payment_total = payment_total
        self.customer_id = customer_id