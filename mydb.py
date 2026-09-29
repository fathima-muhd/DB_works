import mysql.connector

# #establish connection betweenmysql server and python code
# con=mysql.connector.connect(user="root",password="root",host="localhost")

# #returns connection object
# print(con)

# #connection object for executing sql queries
# c=con.cursor()

# query="create database school_db"
# c.execute(query)

# print("db file created")
# c.close()
# con.close()

con=mysql.connector.connect(user="root",
                           password="root",
                             host="localhost",
                             database="school_db")
c=con.cursor()

# query=("""create table student(
#        roll_no int not null primary key,
#        name varchar(30),
#        age int,
#        place varchar(30),
#        phone_no varchar(15),
#        total_mark int )""")
# c.execute(query)
# print("table created")

# create a new record/insert into table

# query="insert into student(roll_no,name,age,place,phone_no,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(101,"Fathima",22,"Kochi","7559886267",89)
# c.execute(query,data)
# con.commit()  #has to be used when any chnage is applied to the table like insert ,delete,update
# print("Inserted data successfully")
# c.close()
# con.close()






