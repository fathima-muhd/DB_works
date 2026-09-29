import mysql.connector
class BooklistCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",
                                        password="root",
                                        host="localhost",
                                        database="library")
        self.cursor=self.con.cursor()
        print("successfully connected")
    def list(self): #to take all records from table thats why no id
        query="select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
               for row in records:
                     print(row)
        else:
              print("no records")
    def create(self,title,author,price,pages,language): # to create,so no id 
            query="insert into book(title,author,price,pages,language) values(%s,%s,%s,%s,%s)"
            data=(title,author,price,pages,language)
            self.cursor.execute(query,data)
            self.con.commit()
            print("data inserted successfully")
    def retrieve(self,id):
            query="select * from book where id=%s"
            data=(id,)
            self.cursor.execute(query,data)
            record=self.cursor.fetchone()
            if record:
                  print(record)
            else:
                  print("No record")
    def update(self,id,title,author,price,pages,language):
            query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id='%s'" 
            data=(title,author,price,pages,language,id)
            self.cursor.execute(query,data)
            self.con.commit()
            if self.cursor.rowcount>0:
                print("data is updated")
            else:
                print("No record")
                              

    def delete(self,id):
            query="delete from book where id=%s"
            data=(id,)
            self.cursor.execute(query,data)
            self.con.commit()
            if self.cursor.rowcount>0:
                  print("Deleted successfully")
            else:
                  print("No record found")

book_instance = BooklistCreateRetrieveUpdateDelete()
# book_instance.list()
# book_instance.create("ABC","devika",2300,75,"english")
# book_instance.retrieve(3)
# book_instance.delete(4)
book_instance.update(5,"DEF","Saniya",2200,100,"Malayalam")


