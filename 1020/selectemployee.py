# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:27:23 2022

@author: solit
"""

import db2


print("查詢員工基本資料")

sql = "select employeeid from works"

cursor = db2.conn.cursor()

cursor.execute(sql)

db2.conn.commit()

result = cursor.fetchall() #抓取全部的資料

print("員工編號")

for row in result:
    print(row[0])

wid = input("輸入員工編號:")

sql = "select employee.name, employee.sex,employee.tel,works.employeeid as '員工編號' from employee inner join works on employee.id=works.id where works.employeeid = '{}'".format(wid)

cursor.execute(sql)
db2.conn.commit()
result2 = cursor.fetchall()

for row in result2:
    print("姓名:",row[0])
    print("性別:",row[1])
    print("電話:",row[2])


db2.conn.close()


