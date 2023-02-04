import pymysql

try:
    con = pymysql.connect(host="localhost",database="demo_db",user="root",password="Akash@1998")
    cursor = con.cursor()
    sql_query = "create table employees(e_no int(5) primary key,e_name varchar(10),e_sal double(10,2),e_addr varchar(10));"
    cursor.execute(sql_query)
    print("Table created successfully")
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
