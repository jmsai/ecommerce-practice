class ReviewView:
    def display_review(self, review):
        response = {
            "author": review["author"],
            "comment": review["comment"],
            "rating": review["rating"]
        }
        return response
