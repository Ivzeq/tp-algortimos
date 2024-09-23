# Funciones

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
            else: 
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
    print(f"{'Plato':<20} {'Precio':<10} {'Categoría':<10}")
    print("-" * 40)  # Línea divisoria

    # Imprimo cada plato en formato de tabla
    [print(plato[:3]) for plato in menu]
    

def hacerPedido(nombre):
    #Inicio el pedido (diccionario) con el nombre para usarlo luego
    pedido = {"nombre":nombre}
    #Asumo que ya vio el menu
    plato = input("Seleccione su plato (0 para terminar): ")
    #Todavia no confirmamos que el plato este efectivamente en el menu
    while plato != "0":
        cant = int(input("Seleccione una cantidad: "))
        if plato in pedido.keys(): #Permite sumar cantidades a un plato ya pedido
            pedido[plato] += cant
            plato = input("Seleccione su plato (0 para terminar): ")
        else:
            pedido[plato] = cant #Pide una cantidad para un nuevo plato
            plato = input("Seleccione su plato (0 para terminar): ")
    if len(pedido) >1: #pedido vacio tiene len 1 porque empieza con el elemento "nombre"
        pedidos.append(pedido)
        print("Gracias por su pedido!")
    else:
        print("Pedido vacio!")
        

def reservar(nombre):
    for mesa in mesas:
        if mesa["estado"] == "libre":
            print(f"Mesa {mesa["idMesa"]}: max {mesa["maxPersonas"]} personas")
    reserva = int(input("Que mesa quiere reservar?"))
    #queda verificar que la mesa reservada exista y poder cancelar el proceso
    comensales = int(input("Para cuantas personas es la reserva?"))
    '''if comensales > mesa[maxPersonas]:
        print(f"La mesa {reserva} tiene capacidad para {mesas} personas")
        reservar(nombre)''' #verificar que la cant de personas sea <= que maxPersonas
    for mesa in mesas: #Busco la mesa con el id seleccionado para modificarla
        if mesa["idMesa"] == reserva:
            mesa["estado"] = "reservado"
            mesa["cantPersonas"] = comensales
            print(f"Mesa {reserva} reservada para {comensales} personas.")
            break
    print(f"Gracias por su reserva, {nombre}")
    

def verPedidos(nombre):
    cant = 0
    for pedido in pedidos:
        if pedido["nombre"] == nombre: #Busco todos los pedidos de la persona
            print(pedido)
            cant += 1
    if cant > 0:
        print("Gracias por su pedido!")
    else:
        print("Usted no tiene ningun pedido activo")
    

def cliente():
    nombre = input("Ingrese su nombre: ")

    print("Bienvenido, ", nombre)

    opcion = int(input("Seleccione un numero de opcion:\n1. Ver Menu\n2. Pedidos\n3. Reservas\n4. Ver estado de su pedido\n0. Salir\n"))

    while opcion <0 or opcion >4:
        opcion = int(input("Opcion invalida.\nSeleccione un numero de opcion:\n1. Ver Menu\n2. Pedidos\n3. Reservas\n4. Ver estado de su pedido\n0. Salir\n"))

    while opcion !=0:    
        if opcion == 1:
            verMenu(menu)
        elif opcion == 2:
            hacerPedido(nombre)
        elif opcion == 3:
            reservar(nombre)
        elif opcion == 4:
            verPedidos(nombre)
        opcion = int(input("Seleccione un numero de opcion:\n1. Ver Menu\n2. Pedidos\n3. Reservas\n4. Ver estado de su pedido\n0. Salir\n"))
    print("Gracias!")
    

# Ejecucion
possibleStatesTupla = ('login', 'verPerfiles', 'verMesas', 'funcionCliente',  'finalizado')

userTypes = [
    {
       "userType": 'admin',
       "permisos": ['verPerfiles', 'verMesas', 'funcionCliente', 'finalizado']
    },
    {
       "userType": 'client',
       "permisos": ['verMesas', 'funcionCliente', 'finalizado']
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
        "cantPersonas": 0,
        "maxPersonas" : 4
    },
    {
        "idMesa": '2',
        "estado": 'menu',
        "cantPersonas": 0,
        "maxPersonas" : 2
    },
    {
        "idMesa": '3',
        "estado": 'esperando comida',
        "cantPersonas": 0,
        "maxPersonas" : 6
    },
    {
        "idMesa": '4',
        "estado": 'comiendo',
        "cantPersonas": 0,
        "maxPersonas" : 4
    },
    {
        "idMesa": '5',
        "estado": 'abonado',
        "cantPersonas": 0,
        "maxPersonas" : 8
    }
]

pedidos = []

appState = 'login'

loggedUser = ''
loggedPassword = ''
loggedUserType = ''
loggedUserPermissions = None

while(appState != possibleStatesTupla[-1]):
    # Inicializacion 

    if (loggedUserType == '' and appState == 'login'):
        tipoIngresado = input('Ingrese client o admin:')
        
        while verificarTipo(tipoIngresado) == False:
            print('El tipo de usuario ingresado no es valido. Ingrese uno de los siguientes posibles')
            for type in userTypes:
                print('-',type['userType'])
            tipoIngresado = input('Ingrese un tipo de usuario valido:')
        
        loggedUserType = tipoIngresado
        loggedUserPermissions = getPermisos(loggedUserType)
        
        printDivider()

    appState = input('Ingrese el proximo state: ')
    
    # Verificacion de state
    while (appState not in possibleStatesTupla) | (verificarPermisos(appState,loggedUserPermissions) == False):
        print('El state ingresado no es valido. Ingrese uno de los siguientes posibles')
        for state in loggedUserPermissions:
            print(loggedUserPermissions.index(state), '-', state)
        appState = input('Ingrese el proximo state: ')
    
    # Manejo de funcionalidades en base al state

    # ---Funcionalidad verPerfiles
    # ------- Pendiente validacion de input
    if appState == 'verPerfiles':
        idPerfil = input('Ingrese all para ver todos los perfiles o el nombre exacto del userType: ')
        
        perfil = getPerfiles(idPerfil)

        if perfil == None:
            print('El perfil no existe')
        else:
            print(perfil)

    # ---Funcionalidad verMesas
    # ------- Pendiente validacion de input
    if appState == 'verMesas':
        idMesa = input('Ingrese all para ver todas las mesas o el id de la mesa: ')
        
        mesa = getMesas(idMesa)

        if mesa == None:
            print('La mesa no existe')
        else:
            print(mesa)

    if appState == 'funcionCliente':
        cliente()

    # Finalizacion
    if(appState == possibleStatesTupla[-1]):
        print('La ejecucion finalizo')
    
    printDivider()