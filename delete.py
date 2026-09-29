import mysql.connector
con=mysql.connector.connect(user="root",
                            password="root",
                            host="localhost",
                            database="school_db")
print(con)
c=con.cursor()
query="delete from student where roll_no='%s'"
data=(102,)

c.execute(query,data)
con.commit()
if c.rowcount>0:
    print("data is deleted")
else:
    print("No record")

c.close()
con.close()
