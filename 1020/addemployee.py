# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:11:17 2022

@author: solit
"""

import db2

print("新增員工資料")
emname = input("員工姓名:")
sex = input("性別(M/F):")
no = input("請需入id:100201開始:")
tel = input("請輸入電話:")
date = input("請輸入到職日期:yyyy-mm-dd:")

sql = "insert into employee(id,name,sex,tel,assume) values('{}','{}','{}','{}','{}')".format(no,emname,sex,tel,date)

cursor = db2.conn.cursor()
cursor.execute(sql)
db2.conn.commit()
db2.conn.close()