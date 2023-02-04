import pymysql

try:
    con = pymysql.connect(host="localhost",database="demo_db",user="root",password="Akash@1998")
    cursor = con.cursor()
    sql_query = "select * from employees"
    cursor.execute(sql_query)
    print("Data retrived successfully")
    print()
    data = cursor.fetchone()
    for row in data:
        print(row)
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem in database: ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
