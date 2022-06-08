import mysql.connector
from pymysql import NULL
import Class_BD
from datetime import datetime

a=Class_BD.BD()
dni="26509218"
averi=str(len(a.Consulta_Condicion("matricula,modelo,marca","coche","DNI="+dni)))
coches=a.Consulta_Condicion("matricula,modelo,marca","coche","DNI="+dni)
nombre=str(a.Consulta_Condicion("nombre","cliente","DNI="+dni))
characters = "[](),'" #caracteres que vamos a quitar
for x in range(len(characters)): #recorremos todos los caracteres y quitamos lo que sobra
    nombre = nombre.replace(characters[x],"")
print("")    
print(nombre +" tiene un total de: "+averi+" coches")
print("")
print("matricula ,modelo, marca")
print("")
for x in range(0,len(coches)):
    print(coches[x])


