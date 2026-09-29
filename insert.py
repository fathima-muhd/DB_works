import mysql.connector
con=mysql.connector.connect(user="root",
                           password="root",
                             host="localhost",
                             database="school_db")
print(con)
c=con.cursor()
query="insert into student(roll_no,name,age,place,phone_no,total_mark) values(%s,%s,%s,%s,%s,%s)"
data=(101,"Fathima",22,"Kochi","7559886267",89)
c.execute(query,data)
con.commit()  #has to be used when any chnage is applied to the table like insert ,delete,update
print("Inserted data successfully")
c.close()
con.close()

