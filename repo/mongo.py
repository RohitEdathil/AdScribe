from .business import BusinessRepository
from models.user import User
from models.product import Product
from typing import List
import pymongo
from os import environ


class MongoRepository(BusinessRepository):
    def __init__(self):
        self.client = pymongo.MongoClient(environ["MONGO_URI"])
        self.database = self.client["vendere"]

    def get_users(self):
        users = self.database["users"]
        user_details = users.find()
        users_list = []
        for user in user_details:
            users_list.append(User.from_dict(user))
        return users_list

    def get_products(self):
        products = self.database["products"]
        products_details = products.find()
        product_list = []
        for product in products_details:
            product["_id"] = str(product["_id"])
            product_list.append(Product.from_dict(product))
        return product_list
