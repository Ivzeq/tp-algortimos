"""importaciones"""
import copy
import sys
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
     "mesa":'1',
     'platos':[["suprema","1","En preparacion"],
               ["milanesa de ternera","1","En preparacion"]
               ]},
    {"nombre":'juan',
     "mesa":'2',
     'platos':[["bife de chorizo","1","En preparacion"],
               ["asado de tira","1","En preparacion"]
               ]},
    {"nombre":'sofia',
     "mesa":'3',
     'platos':[["ensalada","1","En preparacion"],
               ["milanesa de ternera","1","En preparacion"]
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
possibleStatesTupla = ('login', 'verPerfiles', 'verMesas','pedidos','operar','reservar','recepcion','finalizado')

userTypes = [
    {
       "userType": 'admin',
       "permisos": ['verPerfiles', 'verMesas',"pedidos",'finalizado']
    },
    {
       "userType": 'cliente',
       "permisos": ['operar','reservar', 'finalizado']
    },
    {
       "userType": 'cocinero',
       "permisos": ['pedidos','verMesas', 'finalizado']
    },
    {
       "userType": 'mesero',
       "permisos": ['verMesas', 'recepcion','finalizado']
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
def mostrarUserTypes(userTypes):
    #debe recibir una lista de dicts
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║ {'Usuarios':<15}║{'Permisos':<45}║
╠══════════════════════════════════════════════════════════════╣""")
    for userType in userTypes:#va a recorrer la lista de dicts
        permisos = ', '.join(userType['permisos']).lower()#unifica los elementos de la clave "permisos"
        print(f"║ {userType['userType'].capitalize():<15}║{permisos:<45}║")
    print("╚══════════════════════════════════════════════════════════════╝")
    input(">>Enter para continuar\n")

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
{"║":<2}{"Mesa →":<17}{(mesas[i]["idMesa"]):>4}{"║":<2}{"Mesa →":<17}{(mesas[i+1]["idMesa"]):>4}║
╠═════════════════════════════════════════════╣
{"║":<2}{"Estado →":<9}{(mesas[i]["estado"][0:12].capitalize()):>12}{"║":<2}{"Estado →":<9}{(mesas[i+1]["estado"][0:12].capitalize()):>12}║
{"║":<2}{"Reserva →":<9}{(mesas[i]["reserva"][0:12].capitalize()):>12}{"║":<2}{"Reserva →":<9}{(mesas[i+1]["reserva"][0:12].capitalize()):>12}║
{"║":<2}{"Personas →":<17}{(mesas[i]["cantPersonas"]):>4}{"║":<2}{"Personas →":<17}{(mesas[i+1]["cantPersonas"]):>4}║
{"║":<2}{"Limite →":<17}{(mesas[i]["maxPersonas"]):>4}{"║":<2}{"Limite →":<17}{(mesas[i+1]["maxPersonas"]):>4}║""")       
        input(f"╚═════════════════════════════════════════════╝\n>>Enter para continuar")      
    else:
        print(f"""
╔══════════════════════╗
║                      ║
║   🍽 RESTAURANTE🍽     ║
║         Mesas        ║
║                      ║""")
        for i in range(0,len(mesas)):
            print(f"""╠══════════════════════╣
{"║":<5}{"Mesa → ".center(12)}{mesas[i]["idMesa"]:<6}║
╠══════════════════════╣
{"║":<2}{"Estado →":<9}{(mesas[i]["estado"][0:12].capitalize()):>12}{"║":<2}
{"║":<2}{"Reserva →":<9}{(mesas[i]["reserva"][0:12].capitalize()):>12}{"║":<2}
{"║":<2}{"Personas →":<17}{(mesas[i]["cantPersonas"]):>4}{"║":<2}
{"║":<2}{"Limite →":<17}{(mesas[i]["maxPersonas"]):>4}{"║":<2}""")
       
        input(f"╚══════════════════════╝\n>>Enter para continuar")  
    
    
    
    
def limp():
    print("""
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          """)
def getPerfiles (id):
    if id == 'all':
        return userTypes
    else:
        contenedorPerfil=[]
        for userType in userTypes:
            if userType['userType'] == id:
                contenedorPerfil.append(userType)
                return contenedorPerfil
    return None

def getMesas (id):
    if id == 'all':
        return mesas
    else:
        contenedorMesa=[]#para almacenar el diccionario mesa
        for mesa in mesas:
            if mesa['idMesa'] == id:
                contenedorMesa.append(mesa)
                return contenedorMesa
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
    def verificacion(self):
        print('del obejto')
    listaAuxiliar=[]
    
    while True:
        try:
            plato = int(input("\nIngrese numero de plato (0 para terminar): "))
            if plato not in (list(range(0,13))):
                raise ValueError
        except ValueError:
            print(' >>Opcion ingresada no valida\n>> Ingrese una opcion valida')
        else:
            break
    while plato != 0:
        nombrePlato=menu[plato-1][0]
        
        while True:
            try:
                cant = int(input(f"Seleccione una cantidad (disponible {menu[plato-1][3]}): "))
                if cant > menu[plato-1][3]:
                    raise ValueError
            except ValueError:
                print(f'>> Opcion ingresada no valida\n>> Ingrese opcion valida')
            except Exception as ms:
                ms=str(ms)
                print(f'>>ha ocurrido un error -> {ms}')
            else:
                break
        
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
        while True:
            try:
                plato = int(input("\nIngrese numero de plato (0 para terminar): "))
                if plato not in (list(range(0,13))):
                    raise ValueError
            except ValueError:
                print(' >>Opcion ingresada no valida\n>> Ingrese una opcion valida')
            else:
                break            
    print("Gracias por su pedido!")
    if len(pedido)>1:
        pedidos.append(copy.deepcopy(pedido))
    input("\nEnter para continuar")
    
def excepcionNumeroEnteros(mensaje):
    """Esta funcion tiene como fin manejar errores cuando el suusario debe ingresar un dato del tipo entero, retorna un entero"""
    variable=0
    while True:
        try:
            variable=int(input(mensaje))
        except ValueError:
            print(f'>> Opcion ingresada no valida\n>> Ingresar opcion valida')
        except Exception as ms:
            ms=str(ms)
            print(f'>> Ha ocurrido un error -> {ms}')
        else:
            break
    return variable
            
    



def reservar(nombre):
    
    impresionMesas(mesas)
    reserva=str(excepcionNumeroEnteros(f">>Que mesa quiere reservar?\n>>"))
    comensales=excepcionNumeroEnteros(f">>Para cuantas personas es la reserva?\n>>")
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

    print(f"""╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
{"║":<2}Pedidos de → {diccionario["nombre"].capitalize():<31}Mesa -> {diccionario["mesa"]:<2}║                    
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<3}║{'Plato':<28}║{'Cant':<4}║{'Estado':<17}║
╠═══════════════════════════════════════════════════════╣""")
    for plato in diccionario["platos"]:
        print(f"║{(diccionario["platos"].index(plato)+1):<3}║{plato[0]:<28}║{plato[1]:<4}║{plato[2]:<17}║")
    print("""╚═══════════════════════════════════════════════════════╝""")
    input("Presione Enter para continuar>>")
          
    


    
def verPedidos(nombre):#esta funcion solo debe recibir el nombre duelo del pedido
    pedidosCliente={}
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
        opcion=excepcionNumeroEnteros(">> ¿Desea cancelar alguna reserva?\n>> 1 -> Si\n>> 2 -> No ")
        while (opcion !=1 and opcion!=2):
            print(">> Opcion invalida")
            opcion=excepcionNumeroEnteros(">> ¿Desea cancelar alguna reserva?\n>> 1 -> Si\n>> 2 -> No ")
        if opcion == 1:
            aux=[mesa["idMesa"] for mesa in reservasCliente]
            numMesa=str(excepcionNumeroEnteros(f"Ingrese el número de mesa de la reserva que desea cancelar: ")) 
            while numMesa not in aux:
                numMesa=str(excepcionNumeroEnteros(f"Ingrese el número de mesa de la reserva que desea cancelar: "))    
            for mesa in reservasCliente:
                if mesa["idMesa"]==numMesa:
                    mesa_cancelada=mesa
            mesa_cancelada["estado"] = "libre"
            mesa_cancelada["reserva"] = "sin reserva"
            mesa_cancelada["cantPersonas"] = 0
            print(f"Reserva de la Mesa {mesa_cancelada['idMesa']} cancelada.")
        else:
            pass
    else:
        print("No tiene reservas activas.")
        
    input("\nEnter para continuar")

def client_menu():
    limp()
    
    
    while True:
        try:
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
        except ValueError:
            print(f'>>Opcion ingresada no valida\n>>Ingrese una valida')
        except Exception as ms:
            ms=str(ms)
            print(f'>> Ha ocurrido un error ->{ms}')
        else:
            break
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

def cliente():#ahora la funcion crea pedidos con el atributo idmesa, luego ver como modificar la mesa,
    listaIds=[]
    while True:
        try:
            nombre = input("Ingrese su nombre:\n>>").capitalize()
            if nombre=='' or nombre.isspace():
                raise ValueError
            if not(nombre.isalpha()):
                raise ValueError
        except ValueError:
            print(f'>> Opcion ingresada no valida\n>> Ingrese una valida')    
        else:
            break
    while True:
        try:
            numeroMesa=input('>> Ingrese numero de mesa')
            int(numeroMesa)
            listaIds=[mesa['idMesa'] for mesa in mesas]
            if numeroMesa not in listaIds:
                raise ValueError
            for mesa in mesas:
                if mesa['idMesa']==numeroMesa and mesa['estado']!='libre':
                    raise ValueError
        except ValueError:
            print(f'>> Opcion no valida, Ingrese una valida')
            input('ENTER para continuar')    
        except:
            print('>> Ha ocurrido un error')
            input('ENTER para continuar')
        else:
            break 
    pedido={"nombre":nombre,
            "mesa":numeroMesa,
            "platos":[]}
    
    opcion = client_menu()
    limp()
    #EXCEPCION
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
    while True:
        try:
            opcion =int(input(f"""
╔════════════════════════════════════════╗
║                                        ║
║            🍽 RESTAURANTE🍽              ║
║               Bienvenido               ║
║                                        ║
╠════════════════════════════════════════╣
║ Ingrese opcion:                        ║
╠════════════════════════════════════════╣
║ 1 → Salon                              ║
║ 2 → Ver pedidos                        ║
║ 3 → Administrar pedidos                ║
║ 4 → Consultar recetas                  ║
║ 5 → Solicitar aumento de ingredientes  ║
║ 6 → Repriorizar Pedidos                ║
║ 7 → Salir                              ║
╚════════════════════════════════════════╝   
>>Ingrese numero de opcion
>>"""))
            if opcion<1 or opcion>7:
                raise ValueError
        except ValueError:
            print('>> Opcion ingresada no valida\n>> Ingrese una valida')
            input('>> Enter para continuar')
        except KeyboardInterrupt:
            print('\n>> Interrupción detectada..\n>> Terminando tareas..\n>> Finalizando..')
            sys.exit(0)
        except Exception as ms:
            ms=str(ms)
            print(f'>> Ha ocurrido un error -> {ms}')
            input('>> Enter para continuar')
        else:
            break

            
    return opcion

def verificador_disponibilidad(cantidad_comensales,mesas):
    """variables"""
    global id_mesa
    for elemento in mesas:
        if elemento["maxPersonas"]>=cantidad_comensales and elemento["estado"]=="libre":
            #"si hay disponibilidad de mesas"
            id_mesa= elemento["idMesa"]
            return True
            #devuelve true y modifica el id de la mesa
    return False


def menuOpcionesAdministracion():
    
    while True:
        try:
            opcion = int(input(f"""
╔═══════════════════════════════════════╗
║                                       ║
║           🍽 RESTAURANTE🍽              ║
║        Opciones de Administración     ║
║                                       ║
╠═══════════════════════════════════════╣
║ Seleccione el estado del pedido:      ║
╠═══════════════════════════════════════╣
║ [1] Sin hacer                         ║
║ [2] En preparación                    ║
║ [3] Listo                             ║
║ [4] Entregado                         ║
║ [5] Rechazado                         ║
╚═══════════════════════════════════════╝
>>Ingrese número de opción\n>>"""))
            if opcion<1 or opcion>5:
                raise ValueError
        except ValueError:
            print(f'>> Opcion invalida, Ingrese una opcion valida')
            input('>> ENTER para continuar')
        except KeyboardInterrupt:
            print(f'>> Interrupcion detectada!\n>> Finalizando..')
            sys.exit(0)
        except Exception as ms:
            ms=str(ms)
            print(f'>> Ha ocurrido un error -> {ms}')
        else:
            break
    return opcion
def administrarPedidos(pedidos):
    opcion=0
    contador=0
    for elemento in pedidos:
        contador+=1
        print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
        impresionPedidosIndividuales(elemento)
    #EXCEPCION
    while True:
        try:
            numPedido=int(input(">>Ingrese numero de pedido a modificar\n>> "))
            listaAuxiliarPedidos=list(range(1,len(pedidos)+1))
            if numPedido not in listaAuxiliarPedidos:
                raise ValueError    
            
        except ValueError:
            print('>> opcion ingresada no valida\n>> Ingrese una opcion valida')
        except KeyboardInterrupt:
            print(f'>> Interrupcion detectada\n>> Terminando tareas..\n>> Finalizando..')
            sys.exit(0)
        except Exception as ms:
            ms=str(ms)
            print('>> Ha ocurrido un error -> {ms}')
        else:
            break
    #EXCEPCION
    impresionPedidosIndividuales(pedidos[numPedido-1])
    while True:
        try:
            plato=int(input("ingrese numero de plato a modificar"))
            listaAuxiliar=list(range(1,len(pedidos[numPedido-1]["platos"])+1))
            if plato not in listaAuxiliar:
                #el valor ingresado como numero de plato no existe
                raise ValueError
        except ValueError:
            print('>> opcion ingresada no valida\n>> Ingrese numero de plato invalido')
        except KeyboardInterrupt:
            print(f'>> Interrupcion detectada\n>> Terminando tareas..\n>> Finalizando..')
            sys.exit(0)
        except Exception as ms:
            ms=str(ms)
            print('>> Ha ocurrido un error -> {ms}')
        else:
            break
    
    
    
    opcion=menuOpcionesAdministracion()
    #EXCEPCION EN CADA ACCESO
    if opcion==1:
        
        pedidos[numPedido-1]["platos"][plato-1][2]="Sin hacer"
        
    elif opcion==2:
        pedidos[numPedido-1]["platos"][plato-1][2]="En preparacion"
        
    elif opcion==3:
        pedidos[numPedido-1]["platos"][plato-1][2]="Listo"
    elif opcion==4:
        pedidos[numPedido-1]["platos"][plato-1][2]="Entregado"
    elif opcion==5:
        pedidos[numPedido-1]["platos"][plato-1][2]="Rechazado"
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
    contador=0
    for elemento in pedidos:
        contador+=1
        print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
        impresionPedidosIndividuales(elemento)
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
║ 2 → Reservas                           ║
║ 3 → Salir                              ║
║                                        ║
╚════════════════════════════════════════╝
>>""")
        if appState=="1":
            appState="operar"
        elif appState=="2":#m
            appState="reservar"
        elif appState=="3":
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
    elif userType=='cocinero':
        appState="pedidos"      
    elif userType=='mesero':
        appState=input("""
╔════════════════════════════════════════╗
║                                        ║
║            🍽 RESTAURANTE🍽              ║
║                Mesero                  ║
║                                        ║
╠════════════════════════════════════════╣
║ Ingrese opcion:                        ║
╠════════════════════════════════════════╣
║ 1 → Salon                              ║
║ 2 → Recepcion                          ║
║ 3 → Salir                              ║
║                                        ║
╚════════════════════════════════════════╝
>>""")    
        if appState=="1":
            appState="verMesas"
        elif appState=="2":
            appState="recepcion"
        elif appState=="3":
            appState="finalizado" 
    return appState
# Ejecucion
"""PROGRAMA"""
limp()
while(appState != possibleStatesTupla[-1]):
    # Inicializacion 
    while True:
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
║ 3 → Cocinero                           ║
║ 4 → Mesero                             ║
╚════════════════════════════════════════╝          
>>""")
            #DEBERIAMOS AGREGAR VALIDACION CON E.REGULARES COLO POR SI ESCRIBE CON CARACTERES
            
            if tipoIngresado=="1":
                tipoIngresado="cliente"
            elif tipoIngresado=="2":
                tipoIngresado="admin"
            elif tipoIngresado=="3":
                tipoIngresado="cocinero"
            elif tipoIngresado=="4":
                tipoIngresado="mesero"                
            limp()
        try:
            if verificarTipo(tipoIngresado)==False:
                raise ValueError
        except ValueError as ms:
            ms=str(ms)
            print(f'>> El usuario ingresado no existe, ingrese uno valido: {ms}')
        except Exception as error_mssg:
            error_mssg=str(error_mssg)
            print(f'Error : {error_mssg}')
        else:
            break
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
        
        while True:
            limp()
            idPerfil = input('>> Ingrese all para ver todos los perfiles o el nombre exacto del userType: ')
            try:
                perfil = getPerfiles(idPerfil)
                if perfil == None:
                    raise ValueError
            except ValueError as ms:
                ms=str(ms)
                print(f'>> El valor ingresado no es correcto, error -> {ms}')
                input('>>ENTER para continuar')
            except Exception as error_mssg:
                error_mssg=str(error_mssg)
                print(f'>> Ha ocurrido un error: {error_mssg}')
                input('>>ENTER para continuar')
            else:
                break
        mostrarUserTypes(perfil)
    # ---Funcionalidad verMesas
    # ------- Pendiente validacion de input
    if appState=="recepcion":
        nombre=input(">> ingrese nombre de cliente :")
        while True:
            try:
                cantidad_comensales=int(input("ingrese la cantidad de comensales:"))
            except KeyboardInterrupt:
                print(f'>> Interrupcion detectada\n>> Finalizando..')
            except:
                print(f'>> Opcion no valida\n>> Ingrese una opcion valida')
                input('>> ENTER para continuar')
            else:
                break
        
        if verificador_disponibilidad(cantidad_comensales,mesas):
            #entramos al if si solo la funcion verificador_disponibilidad devuelve true
            print(f"hay disponibilidad de mesas, la mesa es {id_mesa}")
            #modificamos el estado de la mesa buscandola por su id
            for elemento in mesas:
                if elemento["idMesa"]==id_mesa:
                    elemento["reserva"]=nombre
                    elemento["estado"]="reservado"
                    elemento["cantPersonas"]=cantidad_comensales
        else:
            print(">> No hay disponibilidad de mesas")       
        input('ENTER para continuar')
    if appState == 'verMesas':
        #EXCEPCION        
        while True:
            try:
                idMesa = input('>>Ingrese all para ver todas las mesas o el id de la mesa: ').lower()
                mesa= getMesas(idMesa)
                if mesa==None:
                    raise ValueError
            except ValueError:
                print('>> Valor ingresado incorrecto')
                input('>> Enter para continuar')
            except Exception as ms:
                ms=str(ms)
                print('>> Ha ocurrido un error -> {ms}')
                input('>> Enter para continuar')
            else:
                break
        impresionMesas(mesa)
    if appState == 'operar':
        cliente()
    if appState == 'reservar':
        while True:
            try:
                nombre = input("Ingrese su nombre:\n>>").capitalize()
                if nombre=='' or nombre.isspace():
                    raise ValueError
                if not(nombre.isalpha()):
                    raise ValueError
            except ValueError:
                print(f'>> Opcion ingresada no valida\n>> Ingrese una valida')    
            else:
                break
            
            
        while True:
            mensaje="""
╔════════════════════════════════════════╗
║                                        ║
║            🍽 RESTAURANTE🍽              ║
║               Reservas                 ║
║                                        ║
╠════════════════════════════════════════╣
║ Ingrese opción:                        ║
╠════════════════════════════════════════╣
║ 1 → Reservar                           ║
║ 2 → Ver reservas                       ║
║ 3 → Salir                              ║
╚════════════════════════════════════════╝          
>>"""
            opcion=excepcionNumeroEnteros(mensaje)
            while opcion<1 or opcion>3:
                opcion=excepcionNumeroEnteros(mensaje)
            if opcion==1:
                reservar(nombre)
            elif opcion==2:
                verReservas(nombre)
            elif opcion==3:
                appState='login'
                break
                


            

    if appState=="pedidos":
        condicion_general=1
        while condicion_general==1:
            condicion=1
            opcion=menuAdminPedidos()
            limp()
            if opcion==1:
                while True:
                    try:
                        idMesa = input('>>Ingrese all para ver todas las mesas o el id de la mesa: ').lower()
                        mesa= getMesas(idMesa)
                        if mesa==None:
                            raise ValueError
                    except ValueError:
                        print('>> Valor ingresado incorrecto')
                        input('>> Enter para continuar')
                    except Exception as ms:
                        ms=str(ms)
                        print('>> Ha ocurrido un error -> {ms}')
                        input('>> Enter para continuar')
                    else:
                        break
                impresionMesas(mesa)                
            elif opcion==2:#salon
                contador=0
                for elemento in pedidos:
                    contador+=1
                    print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
                    impresionPedidosIndividuales(elemento)
                limp()
            elif opcion==3:
                while condicion==1:
                    pedidos=administrarPedidos(pedidos)
                    #EXCEPCION
                    condicion=int(input("Seguir modificando pedidos 1/Si 2/No"))
                    limp()
            elif opcion==4:
                impresionRecetas(recetas)
                input("Enter para continuar")
                limp()
            elif opcion==5:
                inventario=solicitarIngredientes(inventario)
                input("Enter para continuar")
                limp()
            elif opcion==6:
                pedidos=repriorizarPedidos(pedidos)
                contador=0
                for elemento in pedidos:
                    contador+=1
                    print(f"{">>"}{("Pedido numero → "+str(contador)).center(55)}")
                    impresionPedidosIndividuales(elemento)  
                limp()
            elif opcion==7:
                condicion_general=0
                if (loggedUserType == 'cocinero' and appState == 'pedidos'):#solo para que el cocinero pueda salir al menu de perfiles
                    appState='login'
                    loggedUserType=''
                    loggedUserPermissions=None
    if (loggedUserType == 'mesero' and appState == 'finalizado'):#solo para que el mesero pueda salir al menu de perfiles
        appState='login'
        loggedUserType=''
        loggedUserPermissions=None
    # Finalizacion
    if(appState == possibleStatesTupla[-1]):
        appState='login'
        loggedUserType=''
        loggedUserPermissions=None
