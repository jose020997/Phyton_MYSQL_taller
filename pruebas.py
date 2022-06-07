import mysql.connector
from pymysql import NULL
import Class_BD

a=Class_BD.BD()
print(a.Consulta("DNI,nombre","cliente"))
matricula="jose12"
a.Insertar_Co("123","26509218","bmw","serie6","azul")