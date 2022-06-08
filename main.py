#Creación de un programa de seguimiento de un taller
from pymysql import NULL
import Class_BD
from datetime import datetime
from colorama import Fore, init
a=Class_BD.BD()
# print(a.Consulta("DNI,nombre","cliente"))
# print(a.Consulta_Condicion("*","cliente","DNI=26509218"))
# try:
menus=False
while not menus:
        print("")
        print(Fore.GREEN +"Buenos dias, que desea gestionar :")
        print("")
        print("1. Ingresar un Cliente")
        print("2. Nuevo vehiculo")
        print("3. Dar de alta a un Mecanico")
        print("4. Consultas")
        print("5. Abrir una averia")
        print("6. Modificaciones") #Salario de un mecanico, dueño de un coche 
        print("7. Salir")
        print("")
        menu=int(input("---> "))
        if menu == 1:
           dni=int(input("Introduce el DNI "))
           nombre=input("Introduce el Nombre ")
           tele=int(input("Introduce el Telefono "))
           correo=input("Introduce el Correo ")
           dni_t=str(dni)
           tele_t=str(tele)
           print(nombre+" con DNI :"+dni_t+" Telefono: "+tele_t+" y correo: "+correo)
           correcto=input("¿Estan los datos correctos?  ")
           if correcto == "si" or correcto == "s":
                if a.Consulta_Condicion("*","cliente","DNI="+dni_t) != []:
                    print("Ese usuario ya existe ")
                else:
                    a.Insertar_C(dni_t,nombre,tele_t,correo)
                    print("Usuario creado correctamente")
           else:
                print("Que campo quiere cambiar")

        
        elif menu == 2:
            print("Nuevo vehiculo infresado en el talle")
            matricula=input("Introduce la matricula ")
            dni=int(input("Introduce el DNI "))
            modelo=input("Introduce el modelo ")
            marca=input("Introduce la marca ")
            color=input("Introduce el color del coche ")
            dni_t=str(dni)
            print("Se va a dar de alta un "+modelo+" "+marca+" de color "+color+" con matricula "+matricula+" ")
            correcto=input("¿Estan los datos correctos?  ")
            if correcto == "si" or correcto == "s":
                #Comprobacion de que exista en Dni
                if a.Consulta_Condicion("*","cliente","DNI="+dni_t) != []:
                    print("Ese usuario Si existe ")
                    ###
                    ### Dar de alta coche
                    if a.Consulta_Condicion("*","coche","Matricula="+"'"+matricula+"'") != []:
                        print("Ese vehiculo ya existe")
                    else:
                        print("El vehiculo no existe lo damos de alta")
                        a.Insertar_Co(matricula,dni_t,modelo,marca,color)
                        b=a.Consulta_Condicion("Nombre","cliente","DNI="+dni_t)
                        c=str(b)    #Convertimos en string
                        characters = "[](),'" #caracteres que vamos a quitar
                        for x in range(len(characters)): #recorremos todos los caracteres y quitamos lo que sobra
                            c = c.replace(characters[x],"")
                        print("Coche dado de alta para el usuario : "+c)
                else:
                    print("Ese Usuario no existe quiere darlo de alta") #Usuario no existe
                    opcUsu=input("---> ")
                    if opcUsu == "si" or opcUsu=="s":
                        nombre=input("Introduce el Nombre ")
                        tele=int(input("Introduce el Telefono "))
                        correo=input("Introduce el Correo ")
                        tele_t=str(tele)
                        print(nombre+" con DNI :"+dni_t+" Telefono: "+tele_t+" y correo: "+correo)
                        corrrecto3=input("¿Estan los datos correctos?  ")
                        if corrrecto3 == "si" or correcto == "s":
                            a.Insertar_C(dni_t,nombre,tele_t,correo)
                            if a.Consulta_Condicion("*","coche","Matricula="+"'"+matricula+"'") != []:
                                print("Ese vehiculo ya existe")
                            else:
                                print("El vehiculo no existe lo damos de alta")
                                a.Insertar_Co(matricula,dni_t,modelo,marca,color)
                                b=a.Consulta_Condicion("Nombre","cliente","DNI="+dni_t)
                                c1=str(b)    #Convertimos en string
                                characters = "[](),'" #caracteres que vamos a quitar
                                for x in range(len(characters)): #recorremos todos los caracteres y quitamos lo que sobra
                                    c1 = c1.replace(characters[x],"")
                                print("Se va a dar de alta un "+modelo+" "+marca+" de color "+color+" con matricula "+matricula+" Para el cliente :"+c1)    
                        else:
                            print("Nada")
                    else:
                        print("no pasa nada")    
            else:
                print("nada")    
            
        elif menu == 3:
            print("Hoy es dia de contrataciones")
            b=str(len(a.Consulta("*","mecanico")))
            print("Ahora mismo tenemos: "+b+" Mecanicos") 
            Nombre=input("Introduce el nombre ")
            DNIm=int(input("Introduce el DNI "))
            Fecha=datetime.now().strftime("%Y-%m-%d") #fecha actual en el formato correcto
            Salario=int(input("Cual será el salario de este mecanico "))
            dni_t=str(DNIm)
            fecha_t=str(Fecha)
            salario_t=str(Salario)
            print(Nombre+" con Dni: "+dni_t+" a dia "+fecha_t+" y un salario de "+salario_t)
            correcto=input("¿Estan los datos correctos?  ")
            if correcto == "si" or correcto == "s":
                if a.Consulta_Condicion("*","mecanico","DNI="+dni_t) != []:
                    print("Ya existe este mecanico artista")
                else:
                    a.Insertar_M(dni_t,Nombre,fecha_t,salario_t)    
                    print("Mecanico insertado correctamente")
            else:
                print("anulando operacion")    
        elif menu == 4:
            print()
            
        elif menu == 5:
            print()
        elif menu == 6:
            print()    
        else:
            menus=True
            
# except ValueError:
#     print("Se ha introducido un valor no esperado")