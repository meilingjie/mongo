# coding：utf-8
from pymongo import MongoClient
import pymysql
import json

client = MongoClient('192.168.79.124', 27017)
db = client["test"]


def mysql_migrate_product_data():
    test = db['product']
    conn = pymysql.connect(host='192.168.100.127', database='xinyunlian_demo', user='xinyunlian_admin',
                           password='12345678', charset="utf8")
    cursor = conn.cursor()
    cursor.execute("select name, barcode, product_category, introduction from xinyunlian_product")
    products = cursor.fetchall()
    jc = []
    for product in products:
        s = '{"name": "' + str(product[0]) + '", "barCode": "' + str(product[1]) + '", "categoryId": "' + str(
            product[2]) + '", "description": "' + str(product[3]).replace("\"", "'") + '", "status":  "1"}'
        print(s)
        try:
            j = json.loads(s)
            jc.append(j)
        except Exception as e:
            print(Exception, ":", e)
    test.insert_many(jc)


if __name__ == '__main__':
    mysql_migrate_product_data()
