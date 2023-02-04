import pymysql

try:
    con = pymysql.connect(host="localhost",database="demo_db",user="root",password="Akash@1998")
    cursor = con.cursor()
    sql_query = "insert into employees values(146,'Vishnu',500000,'Tamil Nadu');"
    cursor.execute(sql_query)
    print("Data instered successfully")
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
