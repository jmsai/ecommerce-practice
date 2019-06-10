from helpers.Helper import get_money_value


class CartView:
    def display_cart_items(self, cart):
        itemData = list()
        items = cart["items"]

        for item in items:
            sub_total = f'Php {get_money_value(item["sub_total"])}'
            data = {
                "name": item["name"],
                "description": item["description"],
                "brand": item["brand"],
                "model": item["model"],
                "warranty_period": item["warranty_period"],
                "warranty_type": item["warranty_type"],
                "images": item["images"],
                "quantity": item["quantity"],
                "original_price": item["original_price"],
                "discount": item["discount"],
                "price": item["price"],
                "sub_total": sub_total
            }
            itemData.append(data)

        tax_rate = f'{int(cart["tax_rate"])}%'
        tax_amount = f'Php {get_money_value(cart["tax_amount"],)}'
        total = f'Php {get_money_value(cart["total"])}'
        sub_total = f'Php {get_money_value(cart["sub_total"])}'
        shipping_fee = f'Php {get_money_value(cart["shipping_fee"])}'

        response = {
            "items_count": len(items),
            "items": itemData,
            "order_summary": {
                "number_of_items": cart["total_quantity"],
                "sub_total": sub_total,
                "shipping_fee": shipping_fee,
                "tax_rate": tax_rate,
                "tax_amount": tax_amount,
                "total": total
            }
        }

        return response
