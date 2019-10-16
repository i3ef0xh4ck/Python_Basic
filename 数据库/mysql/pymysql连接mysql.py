import pymysql
conn = pymysql.connect(host="39.107.52.113",
                       user="mysql_user",
                       password="Mysql_123",
                       db="dmp")
cur = conn.cursor()

cur.execute("select * from w_cdh_app_daydata limit 10")
result = cur.fetchall()

for i in result:
    print(i)

cur.close()
conn.close()
