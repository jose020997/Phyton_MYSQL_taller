import mysql.connector
from pymysql import NULL
import Class_BD
from datetime import datetime

a=Class_BD.BD()
ahora = datetime.now()

# a.Insertar_M("5555555","jose","2022/07/12","1400")
print(datetime.now().strftime("%Y-%m-%d"))