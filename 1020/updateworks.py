# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:17:24 2022

@author: solit
"""

import db2

print("修改工作資料")

sql = "select id from works"

cursor = db2.conn.cursor()

cursor.execute(sql)

db2.conn.commit()

result = cursor.fetchall() #抓取全部的資料

print("員工id")

for row in result:
    print(row[0])

no = input("請輸入員工id:")
wname = input("請輸入欲修改的工作職稱:")
wdetail = input("請輸入欲修改工作內容:")
reid = input("請輸入欲修改的編號:")


sql = "update works set items='{}',info='{}',employeeid='{}' where id='{}'".format(wname,wdetail,reid,no)

cursor.execute(sql)
db2.conn.commit()



db2.conn.close()