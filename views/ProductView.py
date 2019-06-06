class ProductView:
    def display_product_list(self, product):
        response = {
            "name": product["name"],
            "original_price": product["original_price"],
            "discount_rate": product["discount_rate"],
            "discount_price": product["discount_price"]
        }
        return response

    def display_product_info(self, product):
        response = {
            "name": product["name"],
            "description": product["description"],
            "product_type": product["product_type"],
            "brand": product["brand"],
            "images": product["images"],
            "currency": product["currency"],
            "original_price": product["original_price"],
            "discount_rate": product["discount_rate"],
            "discount_price": product["discount_price"]
        }
        return response
