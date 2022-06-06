import mysql.connector

mydb = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='Taller_Jose')
mycursor = mydb.cursor()

v1='1231243'
v2='gfdsgsfgs'
v3='123444'
v4='sgasgas'
valores = "'"+v1+"','"+v2+"','"+v3+"','"+v4+"'"
print(valores)
consulta="INSERT INTO `cliente` (`DNI`, `Nombre`, `Telefono`, `Correo`) VALUES ("+valores+")"
mycursor.execute(consulta)
mydb.commit()
print("todo bien")

#consulta="INSERT INTO `cliente` (`DNI`, `Nombre`, `Telefono`, `Correo`) VALUES ('1231243', 'gfdsgsfgs', '123444', 'sgasgas')"
