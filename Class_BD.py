import mysql.connector

class BD():
    def __init__(self):
        self.mydb = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='Taller_Jose')
        self.mycursor = self.mydb.cursor()
        
    def Consulta(self,campos,tabla):
        self.tablas=tabla
        self.consulta="select "+campos+" from " + self.tablas
        self.mycursor.execute(self.consulta)
        self.r =  self.mycursor.fetchall()
        return self.r

    def Consulta_Condicion(self,campos,tabla,condicion):
        self.tablas=tabla
        self.consulta="select "+campos+" from " + self.tablas+" WHERE "+condicion
        self.mycursor.execute(self.consulta)
        self.r =  self.mycursor.fetchall()
        return self.r

    def Insertar_C(self,v1,v2,v3,v4): #Solo para Cliente
        self.valores = "'"+v1+"','"+v2+"','"+v3+"','"+v4+"'"
        self.consulta="INSERT INTO `cliente` (`DNI`, `Nombre`, `Telefono`, `Correo`) VALUES ("+self.valores+")"
        self.mycursor.execute(self.consulta)
        self.mydb.commit()
    
    def Insertar_Co(self,v1,v2,v3,v4,v5):
        self.valores = "'"+v1+"','"+v2+"','"+v3+"','"+v4+"','"+v5+"'"
        self.consulta="INSERT INTO `coche` (`Matricula`, `DNI`, `Modelo`, `Marca`, `Color`) VALUES ("+self.valores+")"
        self.mycursor.execute(self.consulta)
        self.mydb.commit() #Probado desde aqui
    
    def Insertar_A(self,v1,v2,v3,v4,v5,v6):
        self.valores = "'"+v1+"','"+v2+"','"+v3+"','"+v4+"','"+v5+"','"+v6+"'"
        self.consulta="INSERT INTO `arregla` (`Cod_Averia`, `Matricula`, `DNI`, `Fech_Repara`, `Horas`, `Problema`) VALUES ("+self.valores+")"
        self.mycursor.execute(self.consulta)
        self.mydb.commit()
    
    def Insertar_M(self,v1,v2,v3,v4): #Solo para Cliente
        self.valores = "'"+v1+"','"+v2+"','"+v3+"','"+v4+"'"
        self.consulta="INSERT INTO `mecanico` (`DNI`, `Nombre`, `Fecha_Contrata`, `Salario`) VALUES ("+self.valores+")"
        self.mycursor.execute(self.consulta)
        self.mydb.commit()   
    
    
a=BD()
#print(BD.Consulta("DNI,nombre","cliente"))  -> Ejemplo de Consulta
# print(BD.Consulta_Condicion("*","cliente","DNI=26509218")) -> Ejemplo de consulta con condicion
#a.Insertar_C("11111111", "manolito", "111111111", "noseesunejemplo")
#a.Insertar_Co("5555555","26509218","Ford","Fiesta","Verde")
