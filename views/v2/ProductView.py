class ProductView:
    def display_list(self, products):
        response = list()

        for product in products:
            currency = product["currency"]
            original_price = "{0:.2f}".format(product["original_price"])
            reviews_count = int(product["reviews_count"])

            data = {
                "id": product["product_id"],
                "name": product["name"],
                "rating": product['rating'],
                "reviews_count": reviews_count,
                "original_price": f'{currency} {original_price}',
                "discount": f'{product["discount"]}% off',
                "price": f'{currency} {product["price"]}'
            }

            response.append(data)

        return response

    def display_details(self, product):
        currency = product["currency"]
        original_price = "{0:.2f}".format(product["original_price"])
        price = "{0:.2f}".format(product["price"])
        discount = int(product["discount"])
        reviews_count = int(product["reviews_count"])

        return {
            "name": product["name"],
            "description": product["description"],
            "product_type": product["product_type"],
            "brand": product["brand"],
            "images": product["images"],
            "rating": product['rating'],
            "reviews_count": reviews_count,
            "original_price": f'{currency} {original_price}',
            "discount": f'{discount}% off',
            "price": f'{currency} {price}'
        }
