#!/usr/bin/python
# -*-coding:utf-8 -*-
import pymysql


def goods_data_optimize():
    conn = pymysql.connect(host='192.168.200.152', database='huala_new', user='root',
                           password='xpsh', charset="utf8")
    count = 0
    cursor = conn.cursor()
    cursor.execute(
        "select c.id, g.id from h_seller_goods g left join h_seller_goods_cat c on g.cid = c.cid and g.seller_id = c.seller_id where g.cid is not null and g.cid != ''")
    products = cursor.fetchall()
    print("total prepare execute " + str(products.__len__()) + " sql")
    for product in products:
        ss = "update h_seller_goods set cid = " + str(product[0]) + " where id = " + str(product[1])
        if (product[0] is not None and product[1] is not None):
            count = count + 1
            # cursor.execute(ss)

    print("total execute " + str(count) + " record")
    # conn.commit()


if __name__ == '__main__':
    goods_data_optimize()
