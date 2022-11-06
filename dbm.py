import pymysql as p

def connect():
    return p.connect(host="localhost",user="root",password="",database="azkbatch")

def insert(t):
    con=connect()
    cur=con.cursor()
    sql="insert into user values (%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def showdata():
    con=connect()
    cur=con.cursor()
    sql="select * from user"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def editdetails(e):
    con=connect()
    cur=con.cursor()
    sql="select * from user where email=%s"
    cur.execute(sql,e)
    userdetail=cur.fetchall()
    con.commit()
    con.close()
    return userdetail

def update(t):
    con=connect()
    cur=con.cursor()
    sql="update user set name=%s,city=%s,email=%s,password=%s where email=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()

def drop(e):
    con=connect()
    cur=con.cursor()
    sql="delete from user where email=%s"
    cur.execute(sql,e)
    con.commit()
    con.close()

def check(email):
    con=connect()
    cur=con.cursor()
    sql="select email,password from user where email=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
