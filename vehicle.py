import mysql.connector
class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",
                                    password="root",
                                    host="localhost",
                                    database="vehicle_db")
        self.cursor=self.con.cursor()
        print("successfully connected")
        
    def list(self):
        query="select* from vehicle"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("No records")

    def create(self,brand,model,type,price,year):
        query="insert into vehicle(brand,model,type,price,year) values(%s,%s,%s,%s,%s)"
        data=(brand,model,type,price,year)
        self.cursor.execute(query,data)
        self.con.commit()
        print("data inserted successfully")

    def retrieve(self,id):
        query="select * from vehicle where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        records=self.cursor.fetchone()
        if records:
            print(records)
        else:
            print("No record found")

    def update(self,id,brand,model,type,price,year):
        query="update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s "
        data=(brand,model,type,price,year,id)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            print("updated")
        else:
            print("No records")

    def delete(self,id):
        query="delete from vehicle where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            print("Deleted")
        else:
            print("No records")
v=VehicleListCreateRetrieveUpdateDelete()
# v.list()
# v.create("RE","meteor","bike",123000,2026)
# v.retrieve(1)
# v.update(1,"RE","hunter","bike",433000,2019)
v.delete(1)

