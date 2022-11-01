# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:48:04 2022

@author: solit
"""

import db2


print("查詢員工工作內容")

sql = "select employeeid from works"

cursor = db2.conn.cursor()

cursor.execute(sql)

db2.conn.commit()

result = cursor.fetchall() #抓取全部的資料

print("員工編號")

for row in result:
    print(row[0])

wid = input("輸入員工編號:")

sql = " select employee.name, works.items as '工作項目',works.info as '工作內容',works.employeeid as '員工編號' from employee inner join works on employee.id = works.id  where works.employeeid = '{}'".format(wid)

cursor.execute(sql)
db2.conn.commit()
result2 = cursor.fetchall()

for row in result2:
    print("姓名:",row[0])
    print("工作項目:",row[1])
    print("工作內容:",row[2])
    


db2.conn.close()