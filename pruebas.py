import mysql.connector
import Class_BD

a=Class_BD.BD()
print(a.Consulta("DNI,nombre","cliente"))
print(a.Consulta_Condicion("*","cliente","DNI=26509218"))
#a.Insertar("12345678","Carlos","666666666","josejose")