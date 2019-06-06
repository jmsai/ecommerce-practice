class OrderView:
    def display_orders(self, order):
        response = {
            "order_id": order["order_id"],
            "tracking_id": order["tracking_id"],
            "delivery_status": order["delivery_status"],
            "delivery_date": order["delivery_date"],
            "transaction_date": order["transaction_date"],
            "payment_status": order["payment_status"],
            "items": order["items"]
        }
        return response

    def display_order_details(self, order):
        response = {
            "order_id": order["order_id"],
            "tracking_id": order["tracking_id"],
            "delivery_status": order["delivery_status"],
            "delivery_date": order["delivery_date"],
            "transaction_date": order["transaction_date"],
            "shipping_address": order["shipping_address"],
            "billing_address": order["billing_address"],
            "payment_method": order["payment_method"],
            "payment_status": order["payment_status"],
            "shipping_fee": order["shipping_fee"],
            "items": order["items"]            
        }
        return response
