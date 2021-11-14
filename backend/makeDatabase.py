import os
import sqlite3
import platform

path = ''
system = platform.system()

if system == 'Windows':
    path = os.environ["userprofile"]
    try:
        os.mkdir(path+"\\Documents\\RAMDatabase")
    except FileExistsError:
        pass
if system == 'Darwin':
    path = os.path.expanduser('~/Documents')
    try:
        os.mkdir(path+"/RAMDatabase")
    except FileExistsError:
        pass

con = ''

if system == 'Windows':
    con = sqlite3.connect(path+"\\Documents\\RAMDatabase\RAMdatabase.db")
if system == 'Darwin':
    con = sqlite3.connect(path+"/Documents/RAMDatabase/RAMdatabase.db")

print("Connection Successful")
cur = con.cursor()

#Creating Tables
con.execute("create table if not exists tips(ID INTEGER PRIMARY KEY AUTOINCREMENT, TIP TEXT);")
con.execute("create table if not exists goals(ID INTEGER PRIMARY KEY AUTOINCREMENT, GOAL TEXT);")
con.execute("create table if not exists users(ID INTEGER PRIMARY KEY AUTOINCREMENT, USERID VARCHAR(20));")
con.execute("create table if not exists questions(ID INTEGER PRIMARY KEY AUTOINCREMENT, DAY INTEGER, QUESTION TEXT, EMOTIONS TEXT);")

cur.close()
print("Tables created Successfully")