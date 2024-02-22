import bcrypt

def authenticate(conn, userId, userPwd):
    cursor = conn.cursor()
    cursor.execute("select * from users where username = ?", (userId,))
    user = cursor.fetchone()

    if user is not None:
        return bcrypt.checkpw(userPwd.encode('utf-8'), user[2])
    else:
        return False
