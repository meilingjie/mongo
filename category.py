# coding：utf-8
import pymysql


def category_data_optimize():
    conn = pymysql.connect(host='192.168.200.152', database='huala_shanxi', user='root',
                           password='xpsh', charset="utf8")
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
                ss = "INSERT INTO h_seller_goods_cat ( seller_id, cid, cname, cat_img, parent_cid, parent_cname, is_parent, sort, add_time, add_user,is_delete) VALUES ( " + str(
                    data[2]) + ", " + str(data[1]) + ", " + str(dp[1]) + ", " + str(dp[2]) + ", " + str(
                    dp[3]) + ", " + str(dp[4]) + ", " + str(dp[5]) + ", " + str(dp[6]) + ", " + str(dp[7]) + ", " + str(
                    dp[8]) + ", " + str(dp[9]) + ")"
                count = count + 1
                cursor.execute(ss)

    print("total execute " + str(count) + " record")
    conn.commit()


if __name__ == '__main__':
    category_data_optimize()
