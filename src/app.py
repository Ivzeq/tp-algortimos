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

# Ejecucion
possibleStatesTupla = ('login', 'verPerfiles', 'verMesas', 'finalizado')

userTypes = [
    {
       "userType": 'admin',
       "permisos": ['verPerfiles', 'verMesas', 'finalizado']
    },
    {
       "userType": 'client',
       "permisos": ['verMesas', 'finalizado']
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
        "cantPersonas": 0
    },
    {
        "idMesa": '2',
        "estado": 'menu',
        "cantPersonas": 0
    },
    {
        "idMesa": '3',
        "estado": 'esperando comida',
        "cantPersonas": 0
    },
    {
        "idMesa": '4',
        "estado": 'comiendo',
        "cantPersonas": 0
    },
    {
        "idMesa": '5',
        "estado": 'abonado',
        "cantPersonas": 0
    },
]

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

    appState = input('Ingrese el proximo state: ')
    
    # Verificacion de state
    while (appState not in possibleStatesTupla) | (verificarPermisos(appState,loggedUserPermissions) == False):
        print('El state ingresado no es valido. Ingrese uno de los siguientes posibles')
        for state in loggedUserPermissions:
            print(loggedUserPermissions.index(state), '-', state)
        appState = input('Ingrese el proximo state: ')
    
    # Manejo de funcionalidades en base al state
    
    printDivider()

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

    # Finalizacion
    if(appState == possibleStatesTupla[-1]):
        print('La ejecucion finalizo')