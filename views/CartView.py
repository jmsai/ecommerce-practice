class CartView:
    def display_cart(self, cart):
        response = {
            "payment_method": cart["payment_method"],
            "shipping_fee": cart["shipping_fee"],
            "discount_total": cart["discount_total"],
            "payment_total": cart["payment_total"],
            "grand_total": cart["grand_total"]
        }
        return response

    def display_cart_items(self, item):
        response = {
            "name": item["name"],
            "quantity": item["quantity"],
            "price": item["price"]
        }
        return response
