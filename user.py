import bcrypt
from db_connect import connect,new_user

def newUser():
    conn = connect()
    print("name")
    name = input()
    print("pwd")
    pwd = input()
    salt = bcrypt.gensalt()
    hashed_pwd= bcrypt.hashpw(pwd.encode('utf-8'),salt)

    new_user(conn, name, hashed_pwd)
    

if __name__ == "__main__":
        newUser()


