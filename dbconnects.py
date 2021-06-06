import dbcreds
import mariadb
import traceback

def db_connection():
    try:
        return mariadb.connect(user=dbcreds.user, password=dbcreds.password,
                                host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    except:
        print("Can not connect to DB")
        traceback.print_exc()
        return None

def db_cursor(conn):
    try:
        return conn.cursor()
    except:
        print("cursor not created on DB!")
        traceback.print_exc()
        return None

def close_db_cursor(cursor):
    try:
        cursor.close()
        return True
    except:
        print("Can not close cursor on DB!")
        traceback.print_exc()
        return False

def close_db_connection(conn):
    try:
        conn.close()
        return True
    except:
        print("Can not close connection to DB!")
        traceback.print_exc()
        return False