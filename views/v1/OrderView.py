from helpers.Helper import get_money_value


class OrderView:
    def display_list(self, orders):
        response = list()
        for order in orders:
            total = f'Php {get_money_value(order["total"])}'
            data = {
                    "order_id": order["order_id"],
                    "transaction_date": order["transaction_date"],
                    "delivery_status": order["delivery_status"],
                    "delivery_date": order["delivery_date"],
                    "payment_date": order["payment_date"],
                    "payment_status": order["payment_status"],
                    "total": total
                }
            response.append(data)
        return response

    def display_details(self, order):
        tax_rate = f'{int(order["tax_rate"] * 100)}%'
        tax_amount = f'Php {get_money_value(order["tax_amount"],)}'
        total = f'Php {get_money_value(order["total"])}'
        sub_total = f'Php {get_money_value(order["sub_total"])}'
        shipping_fee = f'Php {get_money_value(order["shipping_fee"])}'

        return {
            "orders": {
                "order_id": order["order_id"],
                "transaction_date": order["transaction_date"],
                "payment_date": order["payment_date"],
                "payment_method": order["payment_method"],
                "payment_status": order["payment_status"],
                "items": order["items"]
            },
            "delivery_info": {
                "tracking_id": order["tracking_id"],
                "delivery_status": order["delivery_status"],
                "delivery_date": order["delivery_date"],
            },
            "customer_info": {
                "customer_name": order["customer_name"],
                "phone_number": order["phone_number"],
                "shipping_address": order["shipping_address"],
                "billing_address": order["billing_address"]
            },
            "order_summary": {
                "number_of_items": order['number_of_items'],
                "sub_total": sub_total,
                "shipping_fee": shipping_fee,
                "tax_rate": tax_rate,
                "tax_amount": tax_amount,
                "total": total
            }
        }
