from db_connect import get_records, connect


def main():
    conn = connect()
    print("enter pwd to login")
    pwd = input(str)
    if(pwd == '123'):
        print('yes')
        rows, column_names = get_records(conn)
        print('|'.join(column_names))
        for row in rows:
            print('|'.join(map(str,row) ))
    else:
        print('no')

    


if __name__ == "__main__":
    main()