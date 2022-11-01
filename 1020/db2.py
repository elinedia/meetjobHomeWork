# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:31:45 2022

@author: solit
"""

import pymysql

dbsetting = {
    "host":"127.0.0.1",
    "port":3306,##連接阜
    "user":"root",
    "password":"123456789",
    "db":"jobs",
    "charset":"utf8"
     
    }

conn = pymysql.connect(**dbsetting) #資料庫物件