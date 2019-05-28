
import  mysql.connector


def select():
    conn = mysql.connector.connect(user='root', password='123456', database='test_12306', use_unicode=True)
    cursor = conn.cursor()
    sql="SELECT * FROM TICKET"
    try:
        # 执行sql语句
        cursor.execute(sql)
#         获取票的记录
        result=cursor.fetchall()
        for row in result:
            tname=row[0]
            tprice=row[1]
            tid=row[2]
            print("id=%s，票名=%s , 票价=%s  " % (tid,tname,tprice))
    except:
        print("Error: unable to fetch data")
    conn.close()

def save(ID):
    conn = mysql.connector.connect(user='root', password='123456', database='test_12306', use_unicode=True)
    cursor = conn.cursor()
    sql="DELETE FROM TICKET WHERE ID= %s" %(ID)
    try:
        cursor.execute(sql)
        if cursor._affected_rows!=0:
            # 对数据库数据有更新
            conn.commit()
            print('购买成功')
        else:
            print('购买失败，请重新购买')
            result = cursor.fetchall()
            for row in result:
                tname = row[0]
                tprice = row[1]
                tid = row[2]
                print("id=%s，票名=%s , 票价=%s  " % (tid, tname, tprice))
    except:
        conn.rollback()

    conn.close()