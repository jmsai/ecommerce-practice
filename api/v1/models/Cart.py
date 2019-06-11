from api.v1.common import Common

carts = []
Common = Common()


class Cart:
    def __init__(self, customer_id='', items=''):
        self.customer_id = customer_id
        self.items = items
        self.tax_rate = 0.04
        self.shipping_fee = 50.00

    def add(self, new_cart):
        carts.append(new_cart)

    def find_all(self):
        return carts

    def find_by_customer(self, customer_id):
        carts = self.find_all()
        customer = Common.filter_result('customer_id', customer_id, carts)
        return next(customer, None)

    def add_item(self, cart, data):
        items = cart['items']
        for item in items:
            if item['item_id'] == data['item_id']:
                item['quantity'] += data['quantity']
                if item['quantity'] == 1:
                    item['sub_total'] = item['price']
                item['sub_total'] = item['price'] * item['quantity']
                return cart
        items.append(data)
        return cart

    def edit_item(self, cart, item_id, data):
        items = cart['items']
        item = next(Common.filter_result('item_id', item_id, items), None)

        if item is None:
            return item

        item['quantity'] += data['quantity']
        item["number_of_items"] = self.count_all_items(cart)

        return cart

    def remove_item(self, cart, item_id):
        items = cart['items']
        item = next(Common.filter_result('item_id', item_id, items), None)
        if item is None:
            return item
        items.remove(item)
        return cart

    def count_all_items(self, cart):
        count = 0
        items = cart["items"]
        for item in items:
            count += item["quantity"]
        return count

    def get_sub_total(self, cart):
        sub_total = 0
        items = cart["items"]
        for item in items:
            sub_total += item["sub_total"]
        return sub_total

    def get_tax_amount(self, cart):
        return cart["sub_total"] * cart["tax_rate"]

    def get_total(self, cart):
        total = cart["sub_total"] + cart["shipping_fee"] + cart["tax_amount"]
        return total
