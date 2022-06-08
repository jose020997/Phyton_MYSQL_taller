#Creación de un programa de seguimiento de un taller
from pickle import TRUE
from pymysql import NULL
import Class_BD
from datetime import datetime
from colorama import Fore, init
a=Class_BD.BD()
# print(a.Consulta("DNI,nombre","cliente"))
# print(a.Consulta_Condicion("*","cliente","DNI=26509218"))
try:
    menus=False
    while not menus:
        print("")
        print(Fore.GREEN +"Buenos dias, que desea gestionar :")
        print("")
        print("1. Ingresar un Cliente")
        print("2. Nuevo vehiculo")
        print("3. Dar de alta a un Mecanico")
        print("4. Abrir una averia")
        print("5. Consultas")
        print("6. Modificaciones") 
        print("7. Dar de baja un mecanico")
        print("8. Salir")
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
                    print("Ya existe este mecanico")
                else:
                    a.Insertar_M(dni_t,Nombre,fecha_t,salario_t)    
                    print("Mecanico insertado correctamente")
            else:
                print("anulando operacion")    
        elif menu == 4:
            print("Buenas tardes, vamos a gestionar las averias")
            cod_averia=len(a.Consulta("*","arregla"))+1 #Autoincrementamos en 1
            mat=input("Introduce la matricula ")
            b=a.Consulta("Nombre,DNI","mecanico")
            for x in range(0,len(b)):
                print(b[x])
            DNIm=int(input("Introduce el DNI del mecanico: "))
            Fecha="0000/00/00" #fecha actual en el formato correcto
            horas="0"
            cod_t=str(cod_averia)
            dni_t=str(DNIm)
            problema=input("Introduce el problema ")
            if a.Consulta_Condicion("*","coche","Matricula="+"'"+mat+"'") != []:
                print("Ese vehiculo existe")
                if a.Consulta_Condicion("*","mecanico","DNI="+dni_t) != []:
                    print("existe todo")
                    a.Insertar_A(cod_t,mat,dni_t,Fecha,horas,problema)
                    print("Averia correcta")
                else:
                    print("No existe ese mecanico")    
            else:
                print("Ese vehiculo no existe, tendria que darlo de alta") #Otra opcion copiar todo de menu == 2 y asi desde aqui generas el vehiculo y luego das de alta todo
        elif menu == 5:
            menu5=False
            while not menu5:
                print("")
                print("1. Consultar Averias pendientes")
                print("2. Cantidad de coches de un cliente")
                print("3. Salir")
                print("")
                menu5_op=int(input("---> "))
                if menu5_op==1:
                    averi=len(a.Consulta_Condicion("*","arregla","Horas=0"))
                    print("Tenemos un total de "+str(averi)+" sin resolver que son :")
                    averi=a.Consulta_Condicion("Cod_Averia,Matricula,DNI,Problema","arregla","Horas=0")
                    print("")
                    print("Cod,Matricula,Mecanico,Problema")
                    for x in range(0,len(averi)):
                        print(averi[x])

                elif menu5_op==2:
                    dni=input("Introduce el DNI del cliente ")
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

                else:        
                    menu5=True
        elif menu == 6:#Arregla en meacnico where dni=0 and horas=0 que son las no completadas, en arregla cambiar fec_rep y horas_empleadas
            menu6=False
            while not menu6:
                print("")
                print("1. Asignar tareas no completadas de un mecanico expulsado")
                print("2. Completar una tarea")
                print("3. Salir")
                print("")
                menu6_op=int(input("---> "))
                if menu6_op==1:
                    b=a.Consulta_Condicion("cod_averia,problema","arregla","dni=0 AND horas=0")
                    if len(b)!= 0:
                        print("tareas:")
                        for x in range(0,len(b)):
                            print(b[x])
                        print("")
                        print("1. Asignar todas a un mecanico")    
                        print("2. Asignar una a una")
                        menu6_op2=int(input("---> "))
                        if menu6_op2==1:
                            b=a.Consulta("Nombre,DNI","mecanico")
                            for x in range(1,len(b)):
                                print(b[x])
                            DNIm=int(input("Introduce el DNI del mecanico: "))
                            dni_t=str(DNIm)
                            if a.Consulta_Condicion("*","mecanico","DNI="+dni_t) != []:
                                print("existe todo")
                                a.Modificar_A_D(dni_t)
                            else:
                                print("No existe ese mecanico")    
                        elif menu6_op2==2:
                            b=a.Consulta("Nombre,DNI","mecanico")
                            for x in range(1,len(b)):
                                print(b[x])
                            DNIm=int(input("Introduce el DNI del mecanico: "))
                            dni_t=str(DNIm)   
                            orden=int(input("Introduce la orden a modificar: "))
                            orden_7=str(orden)
                            if a.Consulta_Condicion("*","mecanico","DNI="+dni_t) != []:
                                if a.Consulta_Condicion("*","arregla","Cod_Averia="+orden_7) != []:
                                    a.Modificar_una(dni_t,orden_7)
                                else:
                                    print("Esa orden no existe")    
                            else:
                                print("No existe ese mecanico")
                        else:
                            print("salir")        
                    else:
                        print("No tienes tareas sin asignar")    
                elif menu6_op==2:
                    print("Estas son las tareas sin completar")    
                    b=a.Consulta_Condicion("cod_averia,matricula,problema","arregla","horas=0")
                    if b != 0:
                        for x in range(0,len(b)):
                            print(b[x])
                        horas=int(input("las horas dedicadas: "))
                        horas_t=str(horas)   
                        cod=int(input("El codigo de averia: "))
                        cod_t=str(cod) 
                        fecha=datetime.now().strftime("%Y-%m-%d")
                        fecha_t=str(fecha)
                        if a.Consulta_Condicion("*","arregla","Cod_Averia="+cod_t) != []:
                            a.Cambio_Arregla(horas_t,fecha_t,cod_t)
                            print("Cambio realizado correctamente")
                        else:
                            print("No existe esa orden")        
                    else:
                        print("No tienes tareas")    
                else:
                    print("salir")            
                    menu6=True 
        elif menu== 7: #Para dar de baja pasamos los arreglos para mecanico 0
            print("Que mecanico quiere dar de baja")     
            b=a.Consulta("Nombre,DNI","mecanico")
            for x in range(1,len(b)):
                print(b[x])
            DNIm=int(input("Introduce el DNI del mecanico: "))
            dni_t=str(DNIm)
            if a.Consulta_Condicion("*","mecanico","dni="+dni_t) != []:
                if a.Consulta_Condicion("*","arregla","dni="+dni_t) != []:
                    print("tiene ordenes")
                    a.Modificar_A(dni_t)
                    a.Baja_M(dni_t)
                else:
                    print("dar baja")    
                    a.Baja_M(dni_t) #Comprobar si no existe
            else:
                print("No existe ese mecanico")       
        else:
            print("Salir")
            menus=True
            
except ValueError:
    print("Se ha introducido un valor no esperado")