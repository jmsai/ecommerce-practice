class ProductView:
    def display_list(self, products):
        response = list()

        for product in products:
            original_price = "Php {0:.2f}".format(product["original_price"])
            price = "Php {0:.2f}".format(product["price"])
            discount = f'-{product["discount_rate"]}%'

            data = {
                "id": product["product_id"],
                "name": product["name"],
                "original_price": original_price,
                "discount": discount,
                "price": price
            }

            response.append(data)

        return response

    def display_details(self, product):
        original_price = "Php {0:.2f}".format(product["original_price"])
        price = "Php {0:.2f}".format(product["price"])
        discount = f'-{product["discount_rate"]}%'

        return {
            "name": product["name"],
            "description": product["description"],
            "product_type": product["product_type"],
            "brand": product["brand"],
            "model": product["model"],
            "warranty_period": product["warranty_period"],
            "warranty_type": product["warranty_type"],
            "inside_box": product["inside_box"],
            "images": product["images"],
            "original_price": original_price,
            "discount": discount,
            "price": price
        }
