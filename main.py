from db_connect import get_records, connect
from authenticate import authenticate

def main():
    conn = connect()
    print("Enter your Id to login:")
    user_id = input()
    print("Enter your password:")
    user_pwd = input()

    if authenticate(conn, user_id, user_pwd):
        print("Login successful.")
        function(conn)
    else: 
        print("Login failed")


def function(conn):
    rows, column_names = get_records(conn)
    print('|'.join(column_names))
    for row in rows:
        print('|'.join(map(str,row) ))
   

if __name__ == "__main__":
    main()