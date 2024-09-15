"""importaciones"""


"""variables"""
opcion,condicion=0,1

lista_usuarios=[("admin",1234),("adm",123)]

"""funciones"""
def limpiar():
    print("""
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          """) 
def menu():
    opcion=int(input("""
                     1.Cliente
                     2.Staff
                     3.Salir"""))
    limpiar()
    while opcion<1 or opcion>3:
        print("opcion no valida")
        opcion=int(input("""
                     1.Cliente
                     2.Staff
                     3.Salir"""))
        limpiar()
    return opcion
def cliente():
    print("nada")
    #aqui deberiamos poner las actividades que realiza el cleinte
def staff(lista_usuarios):
    #local-variales
    condicion=1
    
    nombre_usuario=input("ingrese su nombre de usuario: ")
    contraseña=int(input("ingrese su contraseña: "))
    #Agregar verificacion de usuario y contraseña con lista_usuarios
    """se puede optimizar proceso con ultimos metodos de acceso a iterables"""
    
    #si entra con cuenta correcta le aparecen las siguientes opciones
    while condicion==1:
        opcion=int(input("""
                     1.Recepcion #diagrama de actividades //empleado.recepcionista//
                     2.Pedidos #diagrama de actividades //empleado.cocinero//
                     3.Salon #diagrama de actividades //empleado.mesero//
                     4.Inventario #diagrama de actividades //empleado.administrador//
                     5.configuraciones #diagrama de actividades //empleado.administrador//
                     6.Volver al menu principal
                     """))#todas las opciones son funciones separadas->
        #if opcion==1:
            #recepcion()
        #elif opcion==2:
            #pedidos()
        #elif opcion==3:
            #salon()
        #elif opcion==4:
            #inventario()
        #elif opcion==5:
            #configuraciones()
        #elif opcion==6:
            #condicion=0
        #else:
            #print("opcion no valida")
            #input("presione enter para continuar")
        #limpiar()
        

"""programa"""
while condicion==1:
    limpiar()
    opcion=menu()
    limpiar()
    if opcion==1:
        print("cliente")
        input("presione enter para continuar")
        #cliente()
    elif opcion==2:
        staff(lista_usuarios)
    elif opcion==3:
        condicion=0
    else:
        print("opcion no valida")
        input("presione enter para continuar")
    limpiar()
