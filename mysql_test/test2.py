
import pymysql

conn = pymysql.connect(host="182.16.130.82", user="", password="", database="learn_db_one")

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = "select * from employee"

res = cursor.execute(sql)
print(res)

data = cursor.fetchone()
print(data)

data = cursor.fetchmany(2)
for row in data:
    emp_name = row["emp_name"]
    sex = row["sex"]
    print(emp_name)
    print(sex)
print(data)

cursor.close()
conn.close()
