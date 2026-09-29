import mysql.connector
con=mysql.connector.connect(user="root",
                           password="root",
                             host="localhost",
                             database="school_db")
print(con)
c=con.cursor()
query="update student set age='%s' where roll_no='%s'"
data=(23,101)
c.execute(query,data)
con.commit()
if c.rowcount>0:
    print("data is updated")
else:
    print("No record")

c.close()
con.close()
