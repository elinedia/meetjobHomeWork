# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:50:47 2022

@author: solit
"""

import db2

print("新增工作資料")
eid = input("輸入員工編號:(A01-W25):")
no = input("請輸入id:100201開始:")
work = input("請輸入工作項目:")
detail = input("請輸入工作內容:")

sql = "insert into works(employeeid,id,items,info) values('{}','{}','{}','{}')".format(eid,no,work,detail)

cursor = db2.conn.cursor()
cursor.execute(sql)
db2.conn.commit()
db2.conn.close()