from helpers.Helper import get_money_value


class CartView:
    def display_cart(self, cart):
        itemData = list()
        items = cart["items"]

        for item in items:
            sub_total = f'Php {get_money_value(item["sub_total"])}'
            price = f'Php {get_money_value(item["price"])}'
            original_price = f'Php {get_money_value(item["original_price"])}'
            discount = f'-{int(item["discount_rate"])}%'
            quantity = int(item["quantity"])

            data = {
                "item_id": item["item_id"],
                "name": item["name"],
                "description": item["description"],
                "brand": item["brand"],
                "model": item["model"],
                "warranty_period": item["warranty_period"],
                "warranty_type": item["warranty_type"],
                "images": item["images"],
                "quantity": quantity,
                "original_price": original_price,
                "discount": discount,
                "price": price,
                "sub_total": sub_total
            }

            itemData.append(data)

        tax_rate = f'{int(cart["tax_rate"] * 100)}%'
        tax_amount = f'Php {get_money_value(cart["tax_amount"],)}'
        total = f'Php {get_money_value(cart["total"])}'
        sub_total = f'Php {get_money_value(cart["sub_total"])}'
        shipping_fee = f'Php {get_money_value(cart["shipping_fee"])}'

        response = {
            "items_count": len(items),
            "items": itemData,
            "order_summary": {
                "sub_total": sub_total,
                "number_of_items": cart["number_of_items"],
                "shipping_fee": shipping_fee,
                "tax_rate": tax_rate,
                "tax_amount": tax_amount,
                "total": total
            }
        }

        return response
