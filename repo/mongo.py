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
        # DB Fetch
        users = self.database["users"]
        user_details = users.find()

        # Creating a mapping of product id to product name
        products = self.get_products()
        products_mapping = {}
        for product in products:
            products_mapping[product.id] = product.name

        users_list = []
        for user in user_details:
            purchase_names = []

            # Replace product ids with product names
            for purchase in user["purchases"]:
                purchase_names.append(products_mapping[purchase])
            user["purchases"] = purchase_names

            users_list.append(User.from_dict(user))

        return users_list

    def get_products(self):
        # DB Fetch
        products = self.database["products"]
        products_details = products.find()
        product_list = []

        for product in products_details:
            # Convert ObjectId to string
            product["_id"] = str(product["_id"])
            product_list.append(Product.from_dict(product))
        return product_list
