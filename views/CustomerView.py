class CustomerView:
    def display_account_settings(self, customer):
        response = {
            "email": customer["email"],
            "phone_number": customer["phone_number"],
            "billing_address": customer["billing_address"],
            "shipping_address": customer["shipping_address"]
        }
        return response

    def display_personal_info(self, customer):
        response = {
            "first_name": customer["first_name"],
            "middle_name": customer["middle_name"],
            "last_name": customer["last_name"],            
            "gender": customer["gender"],
            "birth_date": customer["birth_date"]
        }
        return response
