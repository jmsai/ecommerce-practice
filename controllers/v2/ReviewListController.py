from helpers.JSONHelper import get_json
from models.ReviewModel import ReviewModel

from os import path
import sys

from flask import request
from flask_restful import Resource

sys.path.append(path.join(path.dirname(__file__), '..'))
Review = ReviewModel()


class ReviewListController(Resource):
    def get(self, product_id):
        reviews = Review.find_by_product(product_id)
        if reviews is None:
            return {"message": "no reviews found"}, 404
        return get_json(reviews), 200
