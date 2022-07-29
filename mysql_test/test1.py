import pymysql

conn = pymysql.connect(host="182.16.130.82", user="", password="", database="learn_db_one")

cursor = conn.cursor()

sql = "select * from employee"

# result = cursor.execute(sql)
# result = cursor.fetchone()
# print(result)

sql1 = """
create table myt10(
id int unsigned primary key auto_increment,
first_name char(10) not null,
last_name char(10) not null,
age int unsigned,
sex tinyint,
money float
)
"""
# cursor.execute(sql1)

result = cursor.execute("desc myt10")
result = cursor.fetchall()
print(result)

user = input("user>>:").strip()
name = input("name>>:").strip()
sql2 = "select * from user_name where user=%s and name=%s "

res = cursor.execute(sql2, (user, name))
print(res)
if res:
    print("success")
else:
    print("fail")

cursor.close()
conn.close()
