class ErrorView:
    def display_error(self, title, message):
        response = {
            "title": title,
            "message": message
        }
        return response
