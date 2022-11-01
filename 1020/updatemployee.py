# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:42:50 2022

@author: solit
"""

import db2

print("修改員工資料")

sql = "select id from employee"

cursor = db2.conn.cursor()

cursor.execute(sql)

db2.conn.commit()

result = cursor.fetchall() #抓取全部的資料

print("員工ID")

for row in result:
    print(row[0])

no = input("請輸入員工ID:")
tel = input("請輸入欲修改的電話:")
sex = input("請輸入欲修改性別:")


sql = "update employee set tel='{}',sex='{}' where id='{}'".format(tel,sex,no)

cursor.execute(sql)
db2.conn.commit()



db2.conn.close()