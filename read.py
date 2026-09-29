import mysql.connector

#establish connection betweenmysql server and python code
con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db")

#returns connection object
print(con)

#connection object for executing sql queries
c=con.cursor()

#Read operation

query ="select *from student"
c.execute(query)

records=c.fetchall()
if records:
    for row in records:
        print(row)
else:
    print("No records found")