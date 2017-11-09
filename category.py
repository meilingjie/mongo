#!/usr/bin/python
# -*-coding:utf-8 -*-
import pymysql


def category_data_optimize():
    conn = pymysql.connect(host='127.0.0.1', database='test', user='root',
                           password='123456', charset="utf8")
    count = 0
    cursor = conn.cursor()
    cursor.execute("select id, parent_cid, seller_id from h_seller_goods_cat where parent_cid != 0")
    datas = cursor.fetchall()
    print("total prepare execute " + str(datas.__len__()) + " sql")
    for data in datas:
        if data[2] is not None:
            cursor.execute(
                "select id from h_seller_goods_cat where cid = " + str(data[1]) + " and seller_id = " + str(data[2]))
            dataParent = cursor.fetchone()
            if dataParent is not None:
                ss = "update h_seller_goods_cat set parent_cid = " + str(dataParent[0]) + " where id = " + str(
                    data[0]) + " and seller_id = " + str(data[2])
                count = count + 1
                cursor.execute(ss)
            else:
                cursor.execute("select * from h_goods_cat where id = " + str(data[1]))
                dp = cursor.fetchone()
                if dp is not None:
                    ss = "INSERT INTO h_seller_goods_cat ( seller_id, cid, cname, cat_img, parent_cid, parent_cname, is_parent, sort, add_time, add_user,is_delete) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    count = count + 1
                    cursor.execute(ss,
                                   (data[2], data[1], dp[1], dp[2], dp[3], dp[4], dp[5], dp[6], dp[7], dp[8], dp[9]))

    print("total execute " + str(count) + " record")
    conn.commit()


if __name__ == '__main__':
    category_data_optimize()
