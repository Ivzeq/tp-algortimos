"""importaciones"""
import copy
"""variables"""
"""pedidos=[
    {'nombre': 'tomas',
     'plato 1': ["bife de chorizo","1","En preparacion"],
     'plato 2': ["asado de tira","1","En preparacion"]},
    {'nombre': 'juan',
     'plato 1': ["bife de chorizo","1","En preparacion"],
     'plato 2': ["asado de tira","2","En preparacion"]}
        ]"""
pedidos=[
    {"nombre":'tomas',
     'platos':[["bife de chorizo","1","En preparacion"],
               ["asado de tira","1","En preparacion"]
               ]},
]

menu = [
    #Matriz con columnas: Plato, Precio, Categoría, Stock

    # Platos de carne"
    ["Bife de Chorizo", 15000, "carne", 10],
    ["Asado de Tira", 12800, "carne", 8],
    ["Milanesa de Ternera", 12000, "carne", 15],
    
    # Platos de pollo
    ["Pollo al Horno", 11000, "pollo", 12],
    ["Suprema a la Napolitana", 13000, "pollo", 9],
    ["Pollo a la Parrilla", 12500, "pollo", 7],
    
    # Platos de pescado
    ["Salmón a la Manteca", 20000, "pescado", 5],
    ["Merluza al Horno", 16000, "pescado", 10],
    ["Paella de Mariscos", 22000, "pescado", 6],
    
    # Ensaladas
    ["Ensalada Caesar", 9000, "ensalada", 20],
    ["Ensalada Mixta", 7500, "ensalada", 18],
    ["Ensalada Caprese", 8000, "ensalada", 15]
]

"""inventario para almacenar ingredientes y sus cantidades"""
inventario = {
    "Bife de Chorizo": 10,  # Cantidad en unidades
    "Sal": 5,               # Cantidad en kg
    "Pimienta": 2,         # Cantidad en kg
    "Ternera": 8,          # Cantidad en unidades
    "Pan rallado": 3,      # Cantidad en kg
    "Huevo": 20,           # Cantidad en unidades
    "Pollo": 15,           # Cantidad en unidades
    "Aceite": 5,           # Cantidad en litros
    "Especias": 1,         # Cantidad en kg
    "Pechuga de Pollo": 10,# Cantidad en unidades
    "Jamón": 5,            # Cantidad en kg
    "Queso": 5,            # Cantidad en kg
    "Limón": 20,           # Cantidad en unidades
    "Salmón": 5,           # Cantidad en unidades
    "Manteca": 2,          # Cantidad en kg
    "Merluza": 5,          # Cantidad en unidades
    "Arroz": 10,           # Cantidad en kg
    "Mariscos": 8,         # Cantidad en kg
    "Caldo de pescado": 5, # Cantidad en litros
    "Pimiento": 10,        # Cantidad en unidades
    "Guisantes": 3,        # Cantidad en kg
    "Azafrán": 0.1,        # Cantidad en kg
    "Lechuga": 10,         # Cantidad en unidades
    "Tomate": 10,          # Cantidad en unidades
    "Cebolla": 5,          # Cantidad en unidades
    "Vinagre": 2,          # Cantidad en litros
    "Mozzarella": 5,       # Cantidad en kg
    "Albahaca": 0.5        # Cantidad en kg
}
recetas = [
    {
        "nombre": "Bife de chorizo",
        "ingredientes": [
            {"Bife de Chorizo": 1},
            {"Sal": "al gusto"},
            {"Pimienta": "al gusto"}
        ],
        "tiempo_preparacion": "30 minutos",
        "instrucciones": "Sazonar el bife y asar a la parrilla."
    },
    {
        "nombre": "Asado de tira",
        "ingredientes": [
            {"Asado de Tira": 1},
            {"Sal": "al gusto"},
            {"Pimienta": "al gusto"}
        ],
        "tiempo_preparacion": "45 minutos",
        "instrucciones": "Sazonar y asar a la parrilla."
    },
    {
        "nombre": "Milanesa de ternera",
        "ingredientes": [
            {"Ternera": 1},
            {"Pan rallado": "al gusto"},
            {"Huevo": 1},
            {"Sal": "al gusto"},
            {"Pimienta": "al gusto"}
        ],
        "tiempo_preparacion": "20 minutos",
        "instrucciones": "Empanar la ternera y freír hasta dorar."
    },
    {
        "nombre": "Pollo al horno",
        "ingredientes": [
            {"Pollo": 1},
            {"Aceite": "al gusto"},
            {"Sal": "al gusto"},
            {"Pimienta": "al gusto"},
            {"Especias": "al gusto"}
        ],
        "tiempo_preparacion": "1 hora",
        "instrucciones": "Sazonar y hornear hasta que esté cocido."
    },
    {
        "nombre": "Suprema a la napolitana",
        "ingredientes": [
            {"Pechuga de Pollo": 1},
            {"Jamón": 1},
            {"Queso": 1},
            {"Pan rallado": "al gusto"},
            {"Huevo": 1},
            {"Sal": "al gusto"},
            {"Pimienta": "al gusto"}
        ],
        "tiempo_preparacion": "30 minutos",
        "instrucciones": "Empanar y hornear con jamón y queso."
    },
    {
        "nombre": "Pollo a la parrilla",
        "ingredientes": [
            {"Pollo": 1},
            {"Sal": "al gusto"},
            {"Pimienta": "al gusto"},
            {"Limón": "al gusto"}
        ],
        "tiempo_preparacion": "25 minutos",
        "instrucciones": "Sazonar y asar a la parrilla."
    },
    {
        "nombre": "Salmón a la manteca",
        "ingredientes": [
            {"Salmón": 1},
            {"Manteca": "al gusto"},
            {"Sal": "al gusto"},
            {"Pimienta": "al gusto"}
        ],
        "tiempo_preparacion": "20 minutos",
        "instrucciones": "Cocinar en sartén con manteca."
    },
    {
        "nombre": "Merluza al horno",
        "ingredientes": [
            {"Merluza": 1},
            {"Aceite": "al gusto"},
            {"Limón": "al gusto"},
            {"Sal": "al gusto"},
            {"Pimienta": "al gusto"}
        ],
        "tiempo_preparacion": "30 minutos",
        "instrucciones": "Sazonar y hornear hasta que esté cocido."
    },
    {
        "nombre": "Paella de mariscos",
        "ingredientes": [
            {"Arroz": "2"},
            {"Mariscos": "al gusto"},
            {"Caldo de pescado": "4 tazas"},
            {"Pimiento": "1"},
            {"Guisantes": "al gusto"},
            {"Azafrán": "al gusto"},
            {"Sal": "al gusto"}
        ],
        "tiempo_preparacion": "40 minutos",
        "instrucciones": "Cocinar todos los ingredientes en una paellera."
    },
    {
        "nombre": "Ensalada caesar",
        "ingredientes": [
            {"Lechuga": "1"},
            {"Pollo": "200 g"},
            {"Aderezo Caesar": "al gusto"},
            {"Crutones": "al gusto"}
        ],
        "tiempo_preparacion": "15 minutos",
        "instrucciones": "Mezclar todos los ingredientes y servir."
    },
    {
        "nombre": "Ensalada mixta",
        "ingredientes": [
            {"Lechuga": "1"},
            {"Tomate": "1"},
            {"Cebolla": "1"},
            {"Aceite": "al gusto"},
            {"Vinagre": "al gusto"},
            {"Sal": "al gusto"}
        ],
        "tiempo_preparacion": "10 minutos",
        "instrucciones": "Mezclar todos los ingredientes y servir."
    },
    {
        "nombre": "Ensalada caprese",
        "ingredientes": [
            {"Tomate": "1"},
            {"Mozzarella": "1"},
            {"Albahaca": "al gusto"},
            {"Aceite de oliva": "al gusto"},
            {"Sal": "al gusto"}
        ],
        "tiempo_preparacion": "10 minutos",
        "instrucciones": "Alternar capas de tomate y mozzarella, agregar albahaca."
    }
]
possibleStatesTupla = ('login', 'verPerfiles', 'verMesas','pedidos','operar','finalizado')

userTypes = [
    {
       "userType": 'admin',
       "permisos": ['verPerfiles', 'verMesas',"pedidos",'finalizado']
    },
    {
       "userType": 'cliente',
       "permisos": ['operar', 'finalizado']
    }
]

users = [
    {
       "user": 'RoleError',
       "password": 'error',
       "role": None
    },
    {
       "user": 'admin2',
       "password": 'admin2',
       "role": 'admin'
    }
]
mesas = [
    #Identificador de mesa, estado, nombre de quien reservo, cantidad actual o reservada de personas, cantidad maxima de personas en la mesa
    {
        "idMesa": '1',
        "estado": 'libre',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 4
    },
    {
        "idMesa": '2',
        "estado": 'libre',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 2
    },
    {
        "idMesa": '3',
        "estado": 'libre',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 6
    },
    {
        "idMesa": '4',
        "estado": 'comiendo',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 4
    },
    {
        "idMesa": '5',
        "estado": 'abonado',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 8
    },
    {
        "idMesa": '6',
        "estado": 'abonado',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 16
    }
]


"""MODIFICAR VARIABLE PARA QUE COINCIDA CON LAS DEMAS"""

appState = 'login'

loggedUser = ''
loggedPassword = ''
loggedUserType = ''
loggedUserPermissions = None


opcion=0
condicion_general=1
condicion=1




"""funciones"""
def impresionMesas(mesas):
    """
    Esta funcion recibe la estructutura de datos mesa y realiza una impresion
    la estructura debe contener una cantidad de mesas de numero PAR
    """
    if len(mesas)%2==0:
        print(f"""
╔═════════════════════════════════════════════╗
║                                             ║
║            🍽 RESTAURANTE🍽                   ║
║                   Mesas                     ║
║                                             ║""")
        for i in range(0,len(mesas),2):
            print(f"""╠═════════════════════════════════════════════╣
{"║":<2}{"Mesa →":<17}{(mesas[i]["idMesa"]):<4}{"║":<2}{"Mesa →":<17}{(mesas[i+1]["idMesa"]):<4}║
╠═════════════════════════════════════════════╣
{"║":<2}{"Estado →":<9}{(mesas[i]["estado"][0:12].capitalize()):>12}{"║":<2}{"Estado →":<9}{(mesas[i+1]["estado"][0:12].capitalize()):>12}║
{"║":<2}{"Reserva →":<9}{(mesas[i]["reserva"][0:12].capitalize()):>12}{"║":<2}{"Reserva →":<9}{(mesas[i+1]["reserva"][0:12].capitalize()):>12}║
{"║":<2}{"Personas →":<17}{(mesas[i]["cantPersonas"]):<4}{"║":<2}{"Personas →":<17}{(mesas[i+1]["cantPersonas"]):<4}║
{"║":<2}{"Limite →":<17}{(mesas[i]["maxPersonas"]):<4}{"║":<2}{"Limite →":<17}{(mesas[i+1]["maxPersonas"]):<4}║""")       
        input(f"╚═════════════════════════════════════════════╝\n>>Enter para continuar")      
    else:
        print(f"""
╔══════════════════════╗
║                      ║
║   🍽 RESTAURANTE🍽     ║
║     Mesas            ║
║                      ║""")
        for i in range(0,len(mesas)):
            print(f"""╠══════════════════════╣
{"║":<2}{"Mesa → ".center(12)}{mesas[i]["idMesa"]:<9}║
╠══════════════════════╣
{"║":<2}{"Estado →":<9}{(mesas[i]["estado"][0:12].capitalize()):>12}{"║":<2}
{"║":<2}{"Reserva →":<9}{(mesas[i]["reserva"][0:12].capitalize()):>12}{"║":<2}
{"║":<2}{"Personas →":<17}{(mesas[i]["cantPersonas"]):<4}{"║":<2}
{"║":<2}{"Limite →":<17}{(mesas[i]["maxPersonas"]):<4}{"║":<2}""")
       
        input(f"╚══════════════════════╝\n>>Enter para continuar")  
    
    
    
    
def limp():
    print("""
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          """)
def getPerfiles (id):
    if id == 'all':
        return userTypes
    else:
        for userType in userTypes:
            if userType['userType'] == id:
                return userType
            else: 
                return None

def getMesas (id):
    if id == 'all':
        return mesas
    else:
        for mesa in mesas:
            if mesa['idMesa'] == id:
                return mesa
    return None

def verificarTipo (type):
    tipoValido = False
    for userType in userTypes:
        if userType['userType'] == type:
            tipoValido = True
    return tipoValido

def getPermisos (type):
    for userType in userTypes:
        if userType['userType'] == type:
            return userType['permisos']
    else:
        return None

def verificarPermisos (state, permisos):
    stateValido = False
    for permiso in permisos:
        if permiso == state:
            stateValido = True
    return stateValido


#Falta incorporarlos en algun menu para admins
#MODIFICARLOS, SE CAMBIO LA ESTRUCTURA DE PEDIDOS
def getClientesReservas():
    personas = set([mesa["reserva"] for mesa in mesas if mesa["reserva"] != "sin reserva"])
    print(personas)

def getClientesPedidos():
    personas = set([pedido["nombre"] for pedido in pedidos])
    print(personas)

def reservasYPedidos(cliente):
    intersec = getClientesPedidos & getClientesReservas
    personas = set([persona for persona in intersec])
    print(personas)




def hacerPedido(nombre,pedido):
    
    listaAuxiliar=[]
    plato = int(input("\nIngrese numero de plato (0 para terminar): "))
    
    while plato<0 or plato>12:
        plato = int(input("\nIngrese numero de plato (0 para terminar): "))    
    
    while plato != 0:
        nombrePlato=menu[plato-1][0]
        cant = int(input(f"Seleccione una cantidad (disponible {menu[plato-1][3]}): "))
        if cant <= menu[plato-1][3]: #Si hay suficiente stock
            listaAuxiliar.clear()
            if len(pedido["platos"])>0:
                flag=True
                for elemento in pedido["platos"]:
                    if elemento[0]==nombrePlato:
                        flag=False
                        elemento[1]+=cant
                if flag:
                    listaAuxiliar.append(nombrePlato)
                    listaAuxiliar.append(cant)
                    listaAuxiliar.append("En preparacion")
                    pedido["platos"].append(listaAuxiliar.copy())
            else:
                listaAuxiliar.append(nombrePlato)
                listaAuxiliar.append(cant)
                listaAuxiliar.append("En preparacion")
                pedido["platos"].append(listaAuxiliar.copy())
        
            menu[plato-1][3] -= cant #Resta la cantidad pedida al stock                   
            print(f"Has agregado {cant} de {nombrePlato} a tu pedido.")
        else:
            print("No hay suficiente stock para esa cantidad.")
        plato = int(input("\nSeleccione su plato (0 para terminar): "))
    print("Gracias por su pedido!")
    
    ###verificacio de datos salientes
    print("ESTE ES SU PEDIDO ACTUAL")
    print(pedido)
    if len(pedido)>1:
        pedidos.append(copy.deepcopy(pedido))#DEEPCOPY PARA EVITAR ERROR DE MUTABILIDAD EN ESTRUCTURAS ANIDADAS
    input("\nEnter para continuar")
    




def reservar(nombre):
    
    impresionMesas(mesas)#solo modificamos la impresion de las mesas
    
    reserva = (input(f">>Que mesa quiere reservar?\n>>"))
    comensales = int(input(f">>Para cuantas personas es la reserva?\n>>"))
    mesaEncontrada = False
    reservado = False
    for mesa in mesas:
        #Verifico que la mesa sea valida y que haya elegido una libre
        if mesa["idMesa"] == reserva and mesa["estado"] == "libre":
            mesaEncontrada = True
            if comensales <= mesa["maxPersonas"]:
                #Si todo es correcto, actualizo la info de la mesa
                reservado = True
                mesa["estado"] = "reservado"
                mesa["reserva"] = nombre
                mesa["cantPersonas"] = comensales
                print(f"Mesa {reserva} reservada para {comensales} personas.")
            else:
                #Si quiere reservar para mas personas que la capacidad de la mesa
                print(f">>La mesa {reserva} tiene capacidad para {mesa['maxPersonas']} personas.")
            break
    
    if mesaEncontrada == False:
        #Se selecciono una mesa que no existe o que no esta libre
        print(">>La mesa solicitada no se encuentra disponible.")
    elif reservado == True:
        #Se realizo correctamente la reserva
        print(f"Gracias por su reserva, {nombre.capitalize()}")
    else:
        #Se intento reservar para mas personas que la capacidad de la mesa
        print("Reserva no realizada.")
    input("\nEnter para continuar")
def impresionPedidosIndividuales(diccionario):

    print(f"""
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
{"║":<20}Pedidos de → {diccionario["nombre"].capitalize():<23}║                    
║                                                       ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<3}║{'Plato':<28}║{'Cant':<4}║{'Estado':<17}║
╠═══════════════════════════════════════════════════════╣""")
    for plato in diccionario["platos"]:
        print(f"║{(diccionario["platos"].index(plato)+1):<3}║{plato[0]:<28}║{plato[1]:<4}║{plato[2]:<17}║")
    print("""╚═══════════════════════════════════════════════════════╝""")
    input("Presione Enter para continuar>>")
          
    


    
def verPedidos(nombre):

    for pedido in pedidos:
        if pedido["nombre"]==nombre:#buscamos el diccionacario de pedido de nuestro cliente\nombre
            pedidos.index(pedido)
            pedidosCliente=pedido#este debe estar enlazado al diccionario original para aplicar cambios
            
    if len(pedidosCliente) > 0:#verifica que el el pedido exista
        impresionPedidosIndividuales(pedidosCliente)#llamada a funcion para imprimir diccionarios
        #ESTO DEBERIA SER OTRA FUNCION
        opcion = input("¿Desea cancelar algún pedido? (s/n): ").lower()
        if opcion == 's':
            numPedido = int(input("Ingrese el número de plato que desea cancelar: ")) - 1
            while numPedido<0 or numPedido>len(pedidosCliente):
                numPedido = int(input("Ingrese el número de plato que desea cancelar: ")) - 1
            del pedidosCliente["platos"][numPedido]
            print("Pedido cancelado.")
    else:
        print("Usted no tiene pedidos activos.")
    input("\nEnter para continuar")
        



def verReservas(nombre):
    
    reservasCliente = [mesa for mesa in mesas if mesa["reserva"] == nombre]#enlazamos si es que nuestro cliente tiene nombre, obtenemos una lista de diccionarios
    if len(reservasCliente) > 0:# si existe el diccionario que coincida con el nombre avanzamos
        print(f"Reservas de {nombre.capitalize()}:")
        impresionMesas(reservasCliente)
        opcion = input("¿Desea cancelar alguna reserva? (s/n): ").lower()
        if opcion == 's':
            num_reserva = int(input("Ingrese el número de la reserva que desea cancelar: ")) - 1
            if 0 <= num_reserva < len(reservasCliente):
                mesa_cancelada = reservasCliente[num_reserva]
                mesa_cancelada["estado"] = "libre"
                mesa_cancelada["reserva"] = "sin reserva"
                mesa_cancelada["cantPersonas"] = 0
                print(f"Reserva de la Mesa {mesa_cancelada['idMesa']} cancelada.")
            else:
                print("Número de reserva inválido.")
    else:
        print("No tiene reservas activas.")
        
    input("\nEnter para continuar")

def client_menu():
    limp()
    opcion = int(input(f"""
╔════════════════════════════════════════╗
║                                        ║
║            🍽 RESTAURANTE🍽              ║
║               Bienvenido               ║
║                                        ║
╠════════════════════════════════════════╣
║ Ingrese opcion:                        ║
╠════════════════════════════════════════╣
║ 1 → Menu                               ║
║ 2 → Realizar pedido                    ║
║ 3 → Realizar reserva                   ║
║ 4 → Ver estado de pedidos              ║
║ 5 → ver estado de reserva              ║
║ 6 → Salir                              ║
╚════════════════════════════════════════╝   
>>"""))
    return opcion

def mostrar_menu_platos(menu):
    limp()
    print(f"""
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
║                      Menu de platos                   ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<4}║{'Plato':<28}║{'Precio':<10}║{'Categoría':<10}║
╠═══════════════════════════════════════════════════════╣""")
    for plato in menu:
        print(f"║{(menu.index(plato)+1):<4}║{plato[0]:<28}║{plato[1]:<10}║{plato[2]:<9} {"║":<20}")
    print("""╚═══════════════════════════════════════════════════════╝""")
    input("Presione Enter para continuar>>")

def cliente():

    nombre = input("Ingrese su nombre:\n>>").capitalize()
    
    
    pedido={"nombre":nombre,
            "platos":[]}
    
    opcion = client_menu()
    limp()
    
    while opcion <1 or opcion >6:
        input("Opcion invalida\nENTER para continuar")
        
        opcion = client_menu()
        limp()
    while opcion !=6:    
        if opcion == 1:
            mostrar_menu_platos(menu)
            limp()
        elif opcion == 2:
            mostrar_menu_platos(menu)     
            hacerPedido(nombre,pedido)
            
        elif opcion == 3:
            reservar(nombre)
        elif opcion == 4:
            verPedidos(nombre)
        elif opcion==5:
            verReservas(nombre)
        opcion = client_menu()
    limp()
    print("Gracias!")

def menuAdminPedidos():
    opcion=int(input("""
1.Ver pedidos
2.Administrar pedidos
3.Consultar recetas
4.Solicitar aumento de ingredientes
5.Repriorizar Pedidos
6.Salir
Ingrese numero de opcion="""))
    while opcion<1 or opcion>6:
        opcion=int(input("""
1.Ver pedidos
2.Administrar pedidos
3.Consultar recetas
4.Solicitar aumento de ingredientes
5.Repriorizar Pedidos
6.Salir
Ingrese numero de opcion="""))

    return opcion

def menuAdministrarPedidos():
    opcion=int(input("""
1.Ver pedidos
2.Administrar pedidos
3.Consultar recetas
4.Solicitar aumento de ingredientes
5.Repriorizar Pedidos
6.Salir
Ingrese numero de opcion="""))
    while opcion<1 or opcion>6:
        opcion=int(input("""
1.Ver pedidos
2.Administrar pedidos
3.Consultar recetas
4.Solicitar aumento de ingredientes
5.Repriorizar Pedidos
6.Salir
Ingrese numero de opcion="""))

    return opcion

def menuOpcionesAdministracion():
    
    opcion=int(input("""
1.Sin hacer
2.En preparacion
3.listo
4.Entregado
5.Rechazado
Ingrese numero de opcion="""))
    while opcion<1 or opcion>6:
        opcion=int(input("""
1.Sin hacer
2.En preparacion
3.listo
4.Entregado
5.Rechazado
Ingrese numero de opcion="""))
    return opcion

def impresionPedidos(pedidos,bool,pos):
    """recibe como formato el pedidos
    pedidos=[{
                nombre:xx
                "plato"+ str([i]):[nombre_plato,cantidad,estado],
                }
                ..]
                FIJARSE QUE EL QUE HACE PEDIDOS AL MOMENTO DE AGREGAR PEDIDOS DEBE AGREGARLOS CON UN INDICE COMO AYUDA
                PARA NO REPETIR CLAVES"""
    if bool:
        print(f"\nPEDIDOS")
        nroPedido = 1
        for elemento in pedidos:
            largo=len(elemento)
            claves=list(elemento.keys())
            """creo un alista con los nombres de las keys del diccionario para usarla como indice"""
            print(f"\nPedido {nroPedido}:")
            print(f"Nombre:{elemento["nombre"].capitalize()}")
            for i in range(1,largo):
                print(f"plato {i}:{elemento[claves[i]]}")
            nroPedido += 1
            
    else:
        print(f"\nPedido de {pedidos[pos].get("nombre").capitalize()}")
        largo=len(pedidos[pos])
        claves=list(pedidos[pos].keys())
        """creo un alista con los nombres de las keys del diccionario para usarla como indice"""
        for i in range(1,largo):
            print(f"plato {i}:{pedidos[pos][claves[i]]}")

    return
def administrarPedidos(pedidos):
    opcion=0
    impresionPedidos(pedidos,True,0)
    nom_pedido=input("Ingrese nombre del comensal: ").lower()
    i=0
    limp()
    while i<len(pedidos) and pedidos[i].get("nombre")!=nom_pedido:
        i=i+1
    if i>=len(pedidos):
        print("no encontrado")
        return 
    else:
        impresionPedidos(pedidos,False,i)
        plato=input("ingrese numero de plato a modificar")
        opcion=menuOpcionesAdministracion()
        if opcion==1:
            pedidos[i]["plato " + str(plato)][2]="Sin hacer"
            
        elif opcion==2:
            pedidos[i]["plato " + str(plato)][2]="En preparacion"
            
        elif opcion==3:
            pedidos[i]["plato " + str(plato)][2]="Listo"
            
        elif opcion==4:
            pedidos[i]["plato " + str(plato)][2]="Entregado"
            
        elif opcion==5:
            pedidos[i]["plato " + str(plato)][2]="Rechazado"
            
        """DEBERIAMOS HACER UN BUCLE PARA QUE MODIFIQUE CADA PLATO"""
        return pedidos
def impresionRecetas(recetas):
    i=0
    for elemento in recetas: #Imprime los nombres de las recetas
        print(f"{elemento.get("nombre")}")
    nombre=input("Ingrese nombre de plato: ").capitalize()
    limp()
    while i<len(recetas) and recetas[i].get("nombre")!=nombre:
        i=i+1
    if i>=len(recetas):
        print("nombre no encontrado")
    else: #Si encuentra el plato
        for clave,valor in recetas[i].items():
            if clave=="ingredientes":
                largo=len(recetas[i]["ingredientes"])
                for j in range(largo):
                    print(f"Ingrediente \"{j}\"={recetas[i+1]["ingredientes"][j]}")
            else:
                print(f"{clave} : {valor}")
                
def impresionInventario(inventario):
    for clave,valor in inventario.items():
        print(f"{clave}:{valor}")

def solicitarIngredientes(inventario):
    impresionInventario(inventario)
    nombre=input("ingrese nombre del producto a agregar").capitalize()
    cantidad=int(input("ingrese cantidad a pedir"))
    """modificar ingredientes"""
    return inventario

def repriorizarPedidos(pedidos):
    impresionPedidos(pedidos, True, 0)

    # Solicito el numero del pedido que se desea mover y ajusto el indice
    numPedido = int(input("Ingrese el número de pedido que desea mover: ")) - 1

    # Verifico que el numero de pedido sea valido
    while numPedido < 0 or numPedido >= len(pedidos):
        print("Número de pedido inválido.")
        numPedido = int(input("Ingrese el número de pedido que desea mover: ")) - 1

    # Solicito la nueva posicion a la que se desea mover y ajusto el indice
    nuevaPos = int(input("Ingrese la nueva posición (1 para la primera): ")) - 1

    pedidoMovido = pedidos[numPedido]

    # Elimino el pedido de su posicion original
    pedidos = pedidos[:numPedido] + pedidos[numPedido + 1:]

    # Si la nueva posicion excede la longitud de la lista, lo agrego al final
    if nuevaPos >= len(pedidos):
        pedidos.append(pedidoMovido)
    # Si ingresa 0 o negativo, lo pone primero en la lista
    elif nuevaPos <= 0:
        pedidos = [pedidoMovido] + pedidos[:]
    else:
        # Inserto el pedido en la nueva posicion usando rebanado
        pedidos = pedidos[:nuevaPos] + [pedidoMovido] + pedidos[nuevaPos:]

    print("Repriorización hecha.")
    impresionPedidos(pedidos, True, 0)
    return pedidos

def impresionPermisos(userType,appState):
    limp()
    if userType=="cliente":
        appState=input("""
╔════════════════════════════════════════╗
║                                        ║
║            🍽 RESTAURANTE🍽              ║
║                Cliente                 ║
║                                        ║
╠════════════════════════════════════════╣
║ Ingrese opcion:                        ║
╠════════════════════════════════════════╣
║ 1 → Iniciar                            ║
║ 2 → Salir                              ║
║                                        ║
║                                        ║
╚════════════════════════════════════════╝
>>""")
        if appState=="1":
            appState="operar"
        elif appState=="2":
            appState="finalizado"
    elif userType=="admin":
        appState=input("""
╔════════════════════════════════════════╗
║                                        ║
║            🍽 RESTAURANTE🍽              ║
║             Administrador              ║
║                                        ║
╠════════════════════════════════════════╣
║ Ingrese opcion:                        ║
╠════════════════════════════════════════╣
║ 1 → Perfiles                           ║
║ 2 → Mesas                              ║
║ 3 → Pedidos                            ║
║ 4 → Salir                              ║
╚════════════════════════════════════════╝
>>""")
        if appState=="1":
            appState="verPerfiles"
        elif appState=="2":
            appState="verMesas"
        elif appState=="3":
            appState="pedidos"
        elif appState=="4":
            appState="finalizado"        
    return appState
        

def muestraMesasPerfiles(dato):
    if type(dato)==list:
        for elemento in dato:
            for clave,valor in elemento.items():
                print(f"{clave}:{valor}")
            print("-" * 20)
    else:
        for clave,valor in dato.items():
            print(f"{clave}:{valor}")
    input("\nEnter para continuar")


# Ejecucion
"""PROGRAMA"""
limp()
while(appState != possibleStatesTupla[-1]):
    # Inicializacion 

    if (loggedUserType == '' and appState == 'login'):
        tipoIngresado =input("""
╔════════════════════════════════════════╗
║                                        ║
║            🍽 RESTAURANTE🍽              ║
║                                        ║
╠════════════════════════════════════════╣
║ Ingrese opcion:                        ║
╠════════════════════════════════════════╣
║ 1 → Cliente                            ║
║ 2 → Administrador                      ║
╚════════════════════════════════════════╝          
>>""")
        if tipoIngresado=="1":
            tipoIngresado="cliente"
        elif tipoIngresado=="2":
            tipoIngresado="admin"
        limp()
        while verificarTipo(tipoIngresado) == False:
            print('>>El tipo de usuario ingresado no es valido.')
            input(">>Enter para continuar")
            limp()
            tipoIngresado =input("""
╔════════════════════════════════════════╗
║                                        ║
║            🍽 RESTAURANTE🍽              ║
║                                        ║
╠════════════════════════════════════════╣
║ Ingrese opcion:                        ║
╠════════════════════════════════════════╣
║ 1 → Cliente                            ║
║ 2 → Administrador                      ║
╚════════════════════════════════════════╝          
>>""")
            if tipoIngresado=="1":
                tipoIngresado="cliente"
            elif tipoIngresado=="2":
                tipoIngresado="admin"
        
        loggedUserType = tipoIngresado
        loggedUserPermissions = getPermisos(loggedUserType)
        
    limp()

    
    
    appState=impresionPermisos(tipoIngresado,appState)
    # Verificacion de state
    while (appState not in possibleStatesTupla) | (verificarPermisos(appState,loggedUserPermissions) == False):
        limp()
        print('>>La opcion ingresada no es valido. Ingrese uno de los siguientes posibles')
        input(">>Enter para continuar")
        limp()
        appState=impresionPermisos(tipoIngresado,appState)
    
    
    
    limp()
    # Manejo de funcionalidades en base al state
    # ---Funcionalidad verPerfiles
    # ------- Pendiente validacion de inpu
    if appState == 'verPerfiles':
        idPerfil = input('Ingrese all para ver todos los perfiles o el nombre exacto del userType: ')
        
        perfil = getPerfiles(idPerfil)
        if perfil == None:
            print('El perfil no existe')
        else:
            muestraMesasPerfiles(perfil)
            
    # ---Funcionalidad verMesas
    # ------- Pendiente validacion de input
    if appState == 'verMesas':
        idMesa = input('Ingrese all para ver todas las mesas o el id de la mesa: ')
        limp()
        mesa = getMesas(idMesa)
        if mesa == None:
            print('La mesa no existe')
        else:
            muestraMesasPerfiles(mesa)
            
    if appState == 'operar':
        cliente()
    if appState=="pedidos":
        condicion_general=1
        while condicion_general==1:
            opcion=menuAdminPedidos()
            limp()
            if opcion==1:
                """mostrar lista de diccionarios de pedidos"""
                impresionPedidos(pedidos,True,0)
                input("Enter para conitnuar")
                limp()
            elif opcion==2:
                while condicion==1:
                    pedidos=administrarPedidos(pedidos)
                    condicion=int(input("Seguir modificando pedidos 1/Si 2/No"))
                    limp()
            elif opcion==3:
                impresionRecetas(recetas)
                input("Enter para continuar")
                limp()
            elif opcion==4:
                inventario=solicitarIngredientes(inventario)
                input("Enter para continuar")
                limp()
            elif opcion==5:
                pedidos=repriorizarPedidos(pedidos)
                input("Enter para continuar")
                limp()
            elif opcion==6:
                print("FIN ROL EMPLEADO.COCINERO")
                condicion_general=0
                
    # Finalizacion
    if(appState == possibleStatesTupla[-1]):
        print('La ejecucion finalizo')
