Vamos a mediante una base de datos, diseñar un programa que permita la gestión de un taller básico.

A falta de modificar que no salte la excepción al insertar un str en un campo int.

El funcionamiento del programa es un funcionamiento básico, para hacer funcionar operaciones SQL, los else solamente cierran, por ahora no tiene otra función, presento un menú con varias opciones, voy a comentar la realización:

        1. Ingresar un Cliente
        2. Nuevo vehículo
        3. Dar de alta a un Mecánico
        4. Abrir una avería
        5. Consultas
        6. Modificaciones 
        7. Dar de baja un mecánico

En la primera opción ingresamos un cliente, siempre convertimos los valores int en str antes de introducirlos a la base de datos, al igual antes mostramos en pantalla y preguntamos por una confirmación, en todos los puntos se comprueba que no exista ya cualquier campo con una clave primaria duplicada, ya que daría error.

En la parte 2 aparte de lo anterior, también comprobamos que para el DNI que se introduce en el vehículo exista un cliente, si no se da la opción de crear un cliente y después con los datos almacenados del coche generar un Insert sin volver a pedirlos.

En el punto 3 añadimos como novedad una función que capta la fecha actual para dar de alta el mecánico, ya que se supone que la contratación se realiza el mismo día.

En la parte 4 la clave primaria la realizamos de manera que se autoincrementa en 1, además de mostrar una lista con todos los mecánicos contratados, si no tenemos dado de alta el vehículo lo tendremos que dar de alta en el punto 2.

En el 5 solamente tenemos consultas select, con condiciones.

Para el 6 punto al dar de alta un parte de avería generamos unas horas de 0 y una fecha de 0000/00/00, para poder luego recuperar en este punto las averías que aún no estén gestionadas, que serán las que cumplan esta condición, además otra opción del menú te permite captar las órdenes en las que el DNI sea igual a 0 (las que tiene un usuario por default, al dar de baja un mecánico con tareas pendientes) esta segunda opción permite asignar tareas que no estén completadas por el mecánico eliminado, las tareas completadas no se filtran, ya que no será necesario asignar a nadie.

Para el último punto podemos hacer un DELETE, pero antes comprobamos que no tenga tareas sin realizar (hora=0) si tiene tareas sin realizar se las asigna al usuario con DNI 0 (usuario intermedio para luego asignar esas tareas a otro mecánico)