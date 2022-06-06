from logging import root
import mysql.connector

class BD():
    def __init__(self):
        self.mydb = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='Taller_Jose')
        self.mycursor = self.mydb.cursor()
        
    def Consulta(self,tabla):
        self.tablas=tabla
        self.consulta="select * from " + self.tablas
        self.mycursor.execute(self.consulta)
        self.r =  self.mycursor.fetchall()
        return self.r


    # mydb.commit()