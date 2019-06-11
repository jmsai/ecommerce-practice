class ErrorView:
    def display(self, error):
        return {
            "title": error["title"],
            "message": error["message"]
        }

    def item_not_found(self):
        return {
            "title": "Error 404",
            "message": "Item not found",
            "status": 404
        }

    def customer_not_found(self):
        return {
            "title": "Error 404",
            "message": "Customer not found",
            "status": 404
        }

    def user_not_found(self):
        return {
            "title": "Error 404",
            "message": "User not found",
            "status": 404
        }

    def product_not_found(self):
        return {
            "title": "Error 404",
            "message": "Product not found",
            "status": 404
        }

    def no_results_found(self):
        return {
            "title": "Error 404",
            "message": "No results found",
            "status": 404
        }

    def order_number_not_found(self):
        return {
            "title": "Error 404",
            "message": "Order not found",
            "status": 404            
        }

    def user_already_exist(self):
        return {
            "title": "Error 400",
            "message": "User already exists",
            "status": 400
        }

    def invalid_login(self):
        return {
            "title": "Error 400",
            "message": "Email or password does not match. Please try again.",
            "status": 400
        }       

    def cart_already_exist(self):
        return {
            "title": "Error 400",
            "message": "Cart already exists for user",
            "status": 400
        }  

    def failed_to_perform_action(self):
        return {
            "title": "Error 422",
            "message": "Failed to perform action. Please try again",
            "status": 422
        }  
