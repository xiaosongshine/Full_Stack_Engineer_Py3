#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=9889, user='root', passwd='root', db='douban', charset='utf8')
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)

cursor.execute("select * from movies")

row_1 = cursor.fetchone()
print("数据为")
print(row_1)

# 关闭数据库连接
db.close()

