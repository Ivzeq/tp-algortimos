"""imporatciones"""
"""variables"""
pedidos=[
    {'nombre': 'Tomas',
     'plato 1': ["bife de chorizo","1","En preparacion"],
     'plato 2': ["asado de tira","1","En preparacion"]},
    {'nombre': 'Juan',
     'plato 1': ["bife de chorizo","1","En preparacion"],
     'plato 2': ["asado de tira","2","En preparacion"]}
        ]

menu = [
    # Platos de carne"""elultimo es stock
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
possibleStatesTupla = ('login', 'verPerfiles', 'verMesas', 'Pedir',"pedidos",'finalizado')

userTypes = [
    {
       "userType": 'admin',
       "permisos": ['verPerfiles', 'verMesas',"pedidos",'finalizado']
    },
    {
       "userType": 'cliente',
       "permisos": ['verMesas', 'Pedir', 'finalizado']
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
    {
        "idMesa": '1',
        "estado": 'libre',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 4
    },
    {
        "idMesa": '2',
        "estado": 'menu',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 2
    },
    {
        "idMesa": '3',
        "estado": 'esperando comida',
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
    
def printDivider ():
    print('''
            ===============================================================================================
          ''')

def verMenu(menu):
    # Imprimo el encabezado de la tabla
    print(f"{'Plato':<25} {'Precio':<10} {'Categoría':<10}")
    print("-" * 40)  # Línea divisoria

    for plato in menu:
        # Creo una lista solo con los 3 primeros elementos
        detalles = plato[:3]

        # Imprimo los elementos de la lista con formato "tabla"
        print(f"{detalles[0]:<25} {detalles[1]:<10} {detalles[2]:<10}")

    '''otra opcion: 
    [print(plato[:3]) for plato in menu]'''
    
    '''Si podemos meter rebanado y comprension de listas en otro lado, esto queda mas lindo:
    for plato in menu:
        print(f"{plato[0]:<20} {plato[1]:<10} {plato[2]:<10}")'''
    

def hacerPedido(nombre):
    """se modifico EL CODIGO PARA QUE SEA COMPATIBLE CON LAS DEMAS FUNCIONES."""
    lista_auxiliar=[]
    
    #Inicio el pedido (diccionario) con el nombre para usarlo luego
    pedido = {"nombre":nombre}
    #Asumo que ya vio el menu
    plato = input("Ingrese nombre de plato (0 para terminar): ")

    while plato != "0": #El input me da 0 en formato string
        encontrado = False #Variable para chequear que el plato elegido este en el menu
        for item in menu:
            if item[0].lower() == plato.lower(): #Toma el plato sin importar las mayusculas
                encontrado = True
                cant = int(input(f"Seleccione una cantidad (disponible {item[3]}): "))
                if cant <= item[3]: #Si hay suficiente stock
                    
                    lista_auxiliar.clear()
                    i=len(pedido)-1
                    """es un indice auxiliar para poder agregar platos con id segun los que existan"""
                    if len(pedido)>1:
                        lista_platos=list(pedido.keys())
                        

                        
                        for i in range(1,len(pedido)):
                            print("ingresamos a LA VERIFICACION DE 2UNIDAD")
                            print(pedido[lista_platos[i]])
                            if plato==pedido[lista_platos[i]][0]:
                                pedido[lista_platos[i]][1]+=cant
                    else:
                        i=i+1
                        lista_auxiliar.append(plato)
                        lista_auxiliar.append(cant)
                        lista_auxiliar.append("En preparacion")
                        pedido["plato "+str(i)] =lista_auxiliar.copy()
                    item[3] -= cant #Resta la cantidad pedida al stock                   
                    print(f"Has agregado {cant} de {plato} a tu pedido.")
                else:
                    print("No hay suficiente stock para esa cantidad.")
                break
        if encontrado == False:
            print("Ese plato no se encuentra en el menú.")

        plato = input("Seleccione su plato (0 para terminar): ")
        
    print("Gracias por su pedido!")
    if len(pedido)>1:
        pedidos.append(pedido)
    input("enter para continuar")
    

def reservar(nombre):
    for mesa in mesas: #Muestro las mesas que estan libres
        if mesa["estado"] == "libre":
            print(f"Mesa {mesa["idMesa"]}: max {mesa["maxPersonas"]} personas")
    reserva = (input("Que mesa quiere reservar?"))
    comensales = int(input("Para cuantas personas es la reserva?"))
    mesa_encontrada = False
    reservado = False
    for mesa in mesas:
        #Verifico que la mesa sea valida y que haya elegido una libre
        if mesa["idMesa"] == reserva and mesa["estado"] == "libre":
            mesa_encontrada = True
            if comensales <= mesa["maxPersonas"]:
                #Si todo es correcto, actualizo la info de la mesa
                reservado = True
                mesa["estado"] = "reservado"
                mesa["reserva"] = nombre
                mesa["cantPersonas"] = comensales
                print(f"Mesa {reserva} reservada para {comensales} personas.")
            else:
                #Si quiere reservar para mas personas que la capacidad de la mesa
                print(f"La mesa {reserva} tiene capacidad para {mesa['maxPersonas']} personas.")
            break
    
    if mesa_encontrada == False:
        #Se selecciono una mesa que no existe o que no esta libre
        print("No se encontró la mesa solicitada o no se encuentra disponible.")
    elif reservado == True:
        #Se realizo correctamente la reserva
        print(f"Gracias por su reserva, {nombre}")
    else:
        #Se intento reservar para mas personas que la capacidad de la mesa
        print("Reserva no realizada.")

    
def verPedidos(nombre):
    pedidos_cliente = [pedido for pedido in pedidos if pedido["nombre"] == nombre]
    if len(pedidos_cliente) > 0:
        print(f"Pedidos de {nombre}:")
        i = 1
        for pedido in pedidos_cliente:
            print(f"Pedido {i}: {pedido}")
            i += 1
        
        opcion = input("¿Desea cancelar algún pedido? (s/n): ").lower()
        if opcion == 's':
            num_pedido = int(input("Ingrese el número de pedido que desea cancelar: ")) - 1
            if 0 <= num_pedido < len(pedidos_cliente):
                pedidos.remove(pedidos_cliente[num_pedido])
                print("Pedido cancelado.")
            else:
                print("Número de pedido inválido.")
    else:
        print("Usted no tiene pedidos activos.")
        
def verReservas(nombre):
    reservas_cliente = [mesa for mesa in mesas if mesa["reserva"] == nombre]
    if len(reservas_cliente) > 0:
        print(f"Reservas de {nombre}:")
        i = 1
        for mesa in reservas_cliente:
            print(f"Reserva {i}: Mesa {mesa['idMesa']} para {mesa['cantPersonas']} personas")
            i += 1

        opcion = input("¿Desea cancelar alguna reserva? (s/n): ").lower()
        if opcion == 's':
            num_reserva = int(input("Ingrese el número de la reserva que desea cancelar: ")) - 1
            if 0 <= num_reserva < len(reservas_cliente):
                mesa_cancelada = reservas_cliente[num_reserva]
                mesa_cancelada["estado"] = "libre"
                mesa_cancelada["reserva"] = "sin reserva"
                mesa_cancelada["cantPersonas"] = 0
                print(f"Reserva de la Mesa {mesa_cancelada['idMesa']} cancelada.")
            else:
                print("Número de reserva inválido.")
    else:
        print("No tiene reservas activas.")

def cliente():
    pedidos=[]
    nombre = input("Ingrese su nombre: ")
    limp()
    print("Bienvenido, ", nombre)

    opcion = int(input("Seleccione un numero de opcion:\n1. Ver Menu\n2. Pedidos\n3. Reservas\n4. Ver estado de su pedido\n5. Ver estado de su reserva\n0. Salir\n"))

    while opcion <0 or opcion >5:
        limp()
        opcion = int(input("Opcion invalida.\nSeleccione un numero de opcion:\n1. Ver Menu\n2. Pedidos\n3. Reservas\n4. Ver estado de su pedido\n5. Ver estado de su reserva\n0. Salir\n"))
    
    limp()
    while opcion !=0:    
        if opcion == 1:
            verMenu(menu)
            input("Enter para continuar")
        elif opcion == 2:
            limp()
            verMenu(menu)            
            hacerPedido(nombre)
        elif opcion == 3:
            reservar(nombre)
        elif opcion == 4:
            verPedidos(nombre)
        else:
            verReservas(nombre)
        limp()
        opcion = int(input("Seleccione un numero de opcion:\n1. Ver Menu\n2. Pedidos\n3. Reservas\n4. Ver estado de su pedido\n5. Ver estado de su reserva\n0. Salir\n"))
    print("Gracias!")

def menu_admin_pedidos():
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

def menu_administrar_pedidos():
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

def menu_opciones_administracion():
    
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

def impresion_pedidos(pedidos,bool,pos):
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
        for elemento in pedidos:
            largo=len(elemento)
            claves=list(elemento.keys())
            """creo un alista con los nombres de las keys del diccionario para usarla como indice"""
            print(f"Nombre:{elemento["nombre"]}")
            for i in range(1,largo):
                print(f"plato {i}:{elemento[claves[i]]}")
            
    else:
        print(f"\nPedido de {pedidos[pos].get("nombre")}")
        largo=len(pedidos[pos])
        claves=list(pedidos[pos].keys())
        """creo un alista con los nombres de las keys del diccionario para usarla como indice"""
        for i in range(1,largo):
            print(f"plato {i}:{pedidos[pos][claves[i]]}")

    return
def administrar_pedidos(pedidos):
    opcion=0
    impresion_pedidos(pedidos,True,0)
    nom_pedido=input(f"Ingrese nombre del comensal")
    nom_pedido=nom_pedido.lower()
    nom_pedido=nom_pedido.capitalize()
    i=0
    limp()
    while i<len(pedidos) and pedidos[i].get("nombre")!=nom_pedido:
        i=i+1
    if i>=len(pedidos):
        print("no encontrado")
        return 
    else:
        impresion_pedidos(pedidos,False,i)
        plato=input("ingrese numero de plato a modificar")
        opcion=menu_opciones_administracion()
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
def impresion_recetas(recetas):
    i=0
    for elemento in recetas:
        print(f"{elemento.get("nombre")}")
    nombre=input("Ingrese nombre de plato=").capitalize()
    limp()
    while i<len(recetas) and recetas[i].get("nombre")!=nombre:
        i=i+1
    if i>=len(recetas):
        print("nombre no encontrado")
    else:
        for clave,valor in recetas[i].items():
            if clave=="ingredientes":
                largo=len(recetas[i]["ingredientes"])
                for j in range(largo):
                    print(f"Ingrediente \"{j}\"={recetas[i+1]["ingredientes"][j]}")
            else:
                print(f"{clave} : {valor}")
                
def impresion_inventario(inventario):
    for clave,valor in inventario.items():
        print(f"{clave}:{valor}")
def solicitar_ingredientes(inventario):
    impresion_inventario(inventario)
    nombre=input("ingrese nombre del producto a agregar").capitalize()
    cantidad=int(input("ingrese cantidad a pedir"))
    """modificar ingredientes"""
    return inventario
def repriorizar_pedidos(pedidos):
    impresion_pedidos(pedidos,True,0)
    num_pedido=int(input("Ingrese numero de pedido"))
    num_pedidob=int(input("ingrese numero de pedido para intercambiar"))
    aux=pedidos[num_pedido-1]
    pedidos[num_pedido-1]=pedidos[num_pedidob-1]
    pedidos[num_pedidob-1]=aux
    print("intercambio hecho")
    impresion_pedidos(pedidos,True,0)
    return pedidos

def impresion_permisos(lista):
    print("Opciones:")
    for elemento  in lista:
        print(f"{elemento}")
def muestra_mesas_perfiles(dato):
    if type(dato)==list:
        for elemento in dato:
            for clave,valor in elemento.items():
                print(f"\n{clave}:{valor}")
            input("Enter para continuar")
    else:
        for clave,valor in dato.items():
            print(f"{clave}:{valor}")
        input("Enter para continuar")

# Ejecucion
"""PROGRAMA"""
limp()
while(appState != possibleStatesTupla[-1]):
    # Inicializacion 

    if (loggedUserType == '' and appState == 'login'):
        tipoIngresado = input('Ingrese "cliente" o "admin":')
        
        while verificarTipo(tipoIngresado) == False:
            print('El tipo de usuario ingresado no es valido. Ingrese uno de los siguientes posibles')
            for type in userTypes:
                print('-',type['userType'])
            tipoIngresado = input('Ingrese un tipo de usuario valido:')
        
        loggedUserType = tipoIngresado
        loggedUserPermissions = getPermisos(loggedUserType)
        
    limp()
    impresion_permisos(loggedUserPermissions)
    appState = input('Ingrese opcion (cadena de caracteres): ')

            
    # Verificacion de state

    while (appState not in possibleStatesTupla) | (verificarPermisos(appState,loggedUserPermissions) == False):
        print('La opcion ingresada no es valido. Ingrese uno de los siguientes posibles')
        for state in loggedUserPermissions:
            print(loggedUserPermissions.index(state), '-', state)
        appState = input('Ingrese opcion (cadena de caracteres): ')
    
    
    
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
            muestra_mesas_perfiles(perfil)
            
    # ---Funcionalidad verMesas
    # ------- Pendiente validacion de input
    if appState == 'verMesas':
        idMesa = input('Ingrese all para ver todas las mesas o el id de la mesa: ')
        limp()
        mesa = getMesas(idMesa)
        if mesa == None:
            print('La mesa no existe')
        else:
            muestra_mesas_perfiles(mesa)
            
    if appState == 'Pedir':
        cliente()
    if appState=="pedidos":
        condicion_general=1
        while condicion_general==1:
            opcion=menu_admin_pedidos()
            limp()
            if opcion==1:
                """mostrar lista de diccionarios de pedidos"""
                impresion_pedidos(pedidos,True,0)
                input("Enter para conitnuar")
                limp()
            elif opcion==2:
                while condicion==1:
                    pedidos=administrar_pedidos(pedidos)
                    condicion=int(input("Seguir modificando pedidos 1/Si 2/No"))
                    limp()
            elif opcion==3:
                impresion_recetas(recetas)
                input("Enter para continuar")
                limp()
            elif opcion==4:
                inventario=solicitar_ingredientes(inventario)
                input("Enter para continuar")
                limp()
            elif opcion==5:
                pedidos=repriorizar_pedidos(pedidos)
                input("Enter para continuar")
                limp()
            elif opcion==6:
                print("FIN ROL EMPLEADO.COCINERO")
                condicion_general=0
                
    # Finalizacion
    if(appState == possibleStatesTupla[-1]):
        print('La ejecucion finalizo')
