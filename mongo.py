# coding：utf-8
from pprint import pprint

from pymongo import MongoClient

client = MongoClient('192.168.79.124', 27017)
db = client["test"]
sp = db['shelf_product']


def find_sp():
    sps = sp.find({"parameters.type": "A", "productId": {"$gt": 100}}, {"productId": 1, "_id": 0}).limit(10)
    for shelf_product in sps:
        pprint(shelf_product)


def find_sp_left():
    sps = sp.aggregate([{"$match": {"parameters.type": "A", "productId": {"$gt": 100}}}, {"$lookup": {
        "from": "product", "localField": "productId", "foreignField": "_id", "as": "productIds"}}])
    step = 0
    for shelf_product in sps:
        if step >= 100:
            return
        else:
            step += 1
        pprint(shelf_product)


def save_sp():
    sp.bulk_write()


if __name__ == '__main__':
    find_sp_left()
