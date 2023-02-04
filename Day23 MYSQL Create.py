import pymysql

try:
    con = pymysql.connect(host="localhost",user="root",password="Akash@1998")
    cursor = con.cursor()
    cursor.execute("CREATE DATABASE demo_db")
    print("Database created successfully")
    con.commit()
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem in database: ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
