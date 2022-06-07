import mysql.connector
from pymysql import NULL
import Class_BD

a=Class_BD.BD()
print(a.Consulta("DNI,nombre","cliente"))
matricula="1234"

print(a.Consulta_Condicion("*","coche","Matricula="+matricula)) 