import mariadb
import dbconnects
import traceback


def login():
    conn = dbconnects.db_connection()
    cursor = dbconnects.db_cursor(conn)
    if(conn == None or cursor == None):
        print("error in database connection")
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)
        return
    try:
        # this is my code for entering a new post into db %s means value we enter will be a string.
       alias = input('alias: ')
       password = input('password: ')
       cursor.execute(f'SELECT id, alias FROM hackers WHERE alias="{alias}" AND password="{password}"')
       result = cursor.fetchone()
    #global statement changes a variable from local to global so you can use it thru out.
       global user_id
       user_id = result[0]
       if(result != None):
             print(f"Hello {result[1]}")
             exploit_choices()
       else:
           print("Wrong username or password!")

    except:
        print("Something went wrong inserting adding new post")
        traceback.print_exc()    
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)

def exploit_choices():
    conn = dbconnects.db_connection()
    cursor = dbconnects.db_cursor(conn)
    if(conn == None or cursor == None):
        print("error in database connection")
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)
        return
    try:
        print("1-Enter new Exploits: ")
        print("2-See all your Exploits: ")
        print("3-See everyones Exploits: ")
        print("4-Exit Hackers: ")
        choices = input('Enter choice: ')
        choices = int(choices)
        # conditional statements 
        if(choices == 1):
            new_exploit()
        elif(choices == 2):
            all_my_exploits()
        elif(choices == 3):
            everyones_exploits()
        elif(choices == 4):
            exit_hackers()
        else:
            print('Make a valid choice!!')
    except:
        print("Something went wrong inserting adding new post")
        traceback.print_exc()    
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)

def  new_exploit():
    conn = dbconnects.db_connection()
    cursor = dbconnects.db_cursor(conn)
    if(conn == None or cursor == None):
        print("error in database connection")
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)
        return
    try:
        enter_exploit = input('enter content: ')
        cursor.execute("INSERT INTO exploits (content, user_id) VALUES (%s, %s)", (enter_exploit, user_id))
        conn.commit()
        print('Succesful Post!')
    except:
        print("Something went wrong inserting adding new post")
        traceback.print_exc()    
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)

def  all_my_exploits():
    conn = dbconnects.db_connection()
    cursor = dbconnects.db_cursor(conn)
    if(conn == None or cursor == None):
        print("error in database connection")
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)
        return
    try:
        cursor.execute(f"SELECT content FROM exploits WHERE user_id={user_id}")
        results = cursor.fetchall()
        for v in results:
            print(v[0])
      
     
    except:
        print("Something went wrong inserting adding new post")
        traceback.print_exc()    
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)

def  everyones_exploits():
    conn = dbconnects.db_connection()
    cursor = dbconnects.db_cursor(conn)
    if(conn == None or cursor == None):
        print("error in database connection")
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)
        return
    try:
        cursor.execute("SELECT content FROM exploits")
        results = cursor.fetchall()
        for v in results:
            print(v[0])
      
     
    except:
        print("Something went wrong inserting adding new post")
        traceback.print_exc()    
        dbconnects.close_db_cursor(cursor)
        dbconnects.close_db_connection(conn)

def exit_hackers():
    print("application closing")

login()