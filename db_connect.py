import sqlite3

def connect():
    conn  = sqlite3.connect('database.db')
    return conn

def get_records(conn):
    cursor=conn.cursor()
    cursor.execute("select * from pwd_manager")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    return rows, column_names

def new_user(conn, user, hashed_pwd):
   cursor=conn.cursor()
   cursor.execute("insert into users (username, password) values (?,?)",(user, hashed_pwd))
   conn.commit()
   return user 


