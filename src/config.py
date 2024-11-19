import sys
import json
import os        
directorio_base=os.path.dirname(os.path.abspath(__file__))
#c:\Users\MOB\Desktop\Programacion\Github\tp-algortimos\src
directorio_base=os.path.join(directorio_base,'datos')
#c:\Users\MOB\Desktop\Programacion\Github\tp-algortimos\src\datos
pedidosPath = os.path.join((directorio_base),'pedidos.json')
mesasPath=os.path.join((directorio_base),'mesas.json')
filesPath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'UI')
configPath=os.path.abspath(__file__)
ticketsPath=os.path.join((directorio_base),'tickets.txt')
while True:
    try:
        pedidos = []
        #print(os.path.exists(pedidos_path))#verificacion
        if os.path.exists(pedidosPath):
            with open(pedidosPath, 'r') as ar:
                contenido = ar.read()
                if contenido:
                    pedidos = json.loads(contenido)
        else:
            with open(pedidosPath, 'w') as ar:
                ar.write(json.dumps(pedidos))
    except FileNotFoundError:
        print('>>El archvio no existe o la direccion esta mal')
        input('>>ENTER para continuar')
        sys.exit(0)
    except Exception as er:
        print(f'>>Error->{er}')
        input('>>ENTER para continuar')
        sys.exit(0)
    else:
        break
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
    "Bife de Chorizo": {"cantidad": 10, "unidad": "pieza"},
    "Sal": {"cantidad": 5000, "unidad": "gramo"},
    "Pimienta": {"cantidad": 2000, "unidad": "gramo"},
    "Ternera": {"cantidad": 8, "unidad": "pieza"},
    "Pan rallado": {"cantidad": 3000, "unidad": "gramo"},
    "Huevo": {"cantidad": 20, "unidad": "pieza"},
    "Pollo": {"cantidad": 15, "unidad": "pieza"},
    "Aceite": {"cantidad": 5000, "unidad": "mililitro"},
    "Especias": {"cantidad": 1000, "unidad": "gramo"},
    "Pechuga de Pollo": {"cantidad": 10, "unidad": "pieza"},
    "Jamón": {"cantidad": 5000, "unidad": "gramo"},
    "Queso": {"cantidad": 5000, "unidad": "gramo"},
    "Limón": {"cantidad": 20, "unidad": "pieza"},
    "Salmón": {"cantidad": 5, "unidad": "pieza"},
    "Manteca": {"cantidad": 2000, "unidad": "gramo"},
    "Merluza": {"cantidad": 5, "unidad": "pieza"},
    "Arroz": {"cantidad": 10000, "unidad": "gramo"},
    "Mariscos": {"cantidad": 8000, "unidad": "gramo"},
    "Caldo de pescado": {"cantidad": 5000, "unidad": "mililitro"},
    "Pimiento": {"cantidad": 10, "unidad": "pieza"},
    "Guisantes": {"cantidad": 3000, "unidad": "gramo"},
    "Azafrán": {"cantidad": 100, "unidad": "gramo"},
    "Lechuga": {"cantidad": 10, "unidad": "pieza"},
    "Tomate": {"cantidad": 10, "unidad": "pieza"},
    "Cebolla": {"cantidad": 5, "unidad": "pieza"},
    "Vinagre": {"cantidad": 2000, "unidad": "mililitro"},
    "Mozzarella": {"cantidad": 5000, "unidad": "gramo"},
    "Albahaca": {"cantidad": 500, "unidad": "gramo"}
}

recetas = [
    {
        "nombre": "Bife de chorizo",
        "ingredientes": [
            {"Bife de Chorizo": 1},
            {"Sal": 25},  # al gusto en gramos
            {"Pimienta": 50}  # al gusto en gramos
        ],
        "tiempo_preparacion": "30 minutos",
        "instrucciones": "Sazonar el bife y asar a la parrilla."
    },
    {
        "nombre": "Asado de tira",
        "ingredientes": [
            {"Asado de Tira": 1},
            {"Sal": 25},  # al gusto en gramos
            {"Pimienta": 50}  # al gusto en gramos
        ],
        "tiempo_preparacion": "45 minutos",
        "instrucciones": "Sazonar y asar a la parrilla."
    },
    {
        "nombre": "Milanesa de ternera",
        "ingredientes": [
            {"Ternera": 1},
            {"Pan rallado": 50},  # al gusto en gramos
            {"Huevo": 1},
            {"Sal": 25},  # al gusto en gramos
            {"Pimienta": 50}  # al gusto en gramos
        ],
        "tiempo_preparacion": "20 minutos",
        "instrucciones": "Empanar la ternera y freír hasta dorar."
    },
    {
        "nombre": "Pollo al horno",
        "ingredientes": [
            {"Pollo": 1},
            {"Aceite": 50},  # al gusto en mililitros
            {"Sal": 25},  # al gusto en gramos
            {"Pimienta": 50},  # al gusto en gramos
            {"Especias": 50}  # al gusto en gramos
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
            {"Pan rallado": 50},  # al gusto en gramos
            {"Huevo": 1},
            {"Sal": 25},  # al gusto en gramos
            {"Pimienta": 50}  # al gusto en gramos
        ],
        "tiempo_preparacion": "30 minutos",
        "instrucciones": "Empanar y hornear con jamón y queso."
    },
    {
        "nombre": "Pollo a la parrilla",
        "ingredientes": [
            {"Pollo": 1},
            {"Sal": 25},  # al gusto en gramos
            {"Pimienta": 50},  # al gusto en gramos
            {"Limón": 1}  # al gusto en piezas
        ],
        "tiempo_preparacion": "25 minutos",
        "instrucciones": "Sazonar y asar a la parrilla."
    },
    {
        "nombre": "Salmón a la manteca",
        "ingredientes": [
            {"Salmón": 1},
            {"Manteca": 50},  # al gusto en gramos
            {"Sal": 25},  # al gusto en gramos
            {"Pimienta": 50}  # al gusto en gramos
        ],
        "tiempo_preparacion": "20 minutos",
        "instrucciones": "Cocinar en sartén con manteca."
    },
    {
        "nombre": "Merluza al horno",
        "ingredientes": [
            {"Merluza": 1},
            {"Aceite": 50},  # al gusto en mililitros
            {"Limón": 1},  # al gusto en piezas
            {"Sal": 25},  # al gusto en gramos
            {"Pimienta": 50}  # al gusto en gramos
        ],
        "tiempo_preparacion": "30 minutos",
        "instrucciones": "Sazonar y hornear hasta que esté cocido."
    },
    {
        "nombre": "Paella de mariscos",
        "ingredientes": [
            {"Arroz": 400},  # 2 tazas equivalen a 400 gramos
            {"Mariscos": 50},  # al gusto en gramos
            {"Caldo de pescado": 500},  # 4 tazas equivalen a 1000 mililitros
            {"Pimiento": 1},
            {"Guisantes": 50},  # al gusto en gramos
            {"Azafrán": 50},  # al gusto en gramos
            {"Sal": 25}  # al gusto en gramos
        ],
        "tiempo_preparacion": "40 minutos",
        "instrucciones": "Cocinar todos los ingredientes en una paellera."
    },
    {
        "nombre": "Ensalada caesar",
        "ingredientes": [
            {"Lechuga": 1},
            {"Pollo": 200},  # 200 gramos
            {"Aderezo Caesar": 50},  # al gusto en gramos
            {"Crutones": 50}  # al gusto en gramos
        ],
        "tiempo_preparacion": "15 minutos",
        "instrucciones": "Mezclar todos los ingredientes y servir."
    },
    {
        "nombre": "Ensalada mixta",
        "ingredientes": [
            {"Lechuga": 1},
            {"Tomate": 1},
            {"Cebolla": 1},
            {"Aceite": 50},  # al gusto en mililitros
            {"Vinagre": 50},  # al gusto en mililitros
            {"Sal": 25}  # al gusto en gramos
        ],
        "tiempo_preparacion": "10 minutos",
        "instrucciones": "Mezclar todos los ingredientes y servir."
    },
    {
        "nombre": "Ensalada caprese",
        "ingredientes": [
            {"Tomate": 1},
            {"Mozzarella": 1},
            {"Albahaca": 50},  # al gusto en gramos
            {"Aceite de oliva": 50},  # al gusto en mililitros
            {"Sal": 25}  # al gusto en gramos
        ],
        "tiempo_preparacion": "10 minutos",
        "instrucciones": "Alternar capas de tomate y mozzarella, agregar albahaca."
    }
]

possibleStatesTupla = ('login', 'verPerfiles', 'verMesas','pedidos','operar','reservar','recepcion','cerrarOrden','finalizado')

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
       "permisos": ['verMesas', 'recepcion','cerrarOrden','finalizado']
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
mesasB = [
    {
        "idMesa": '1',
        "estado": 'libre',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 2
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
        "maxPersonas" : 4
    },
    {
        "idMesa": '4',
        "estado": 'libre',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 4
    },
    {
        "idMesa": '5',
        "estado": 'libre',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 6
    },
    {
        "idMesa": '6',
        "estado": 'libre',
        "reserva": 'sin reserva',
        "cantPersonas": 0,
        "maxPersonas" : 6
    }
]

try:
    if os.path.exists(mesasPath):
        with open(mesasPath, 'r+') as archivo:
            contenido = archivo.read()
            if contenido!='':
                mesas = json.loads(contenido)
            else:
                archivo.seek(0)
                archivo.write(json.dumps(mesasB))
                archivo.truncate()
                archivo.seek(0)
                contenido=archivo.read()
                mesas=json.loads(contenido)
    else:
        with open(mesasPath, 'w') as ar:
            ar.write(json.dumps(mesasB))
except FileNotFoundError:
    print('>>El archvio no existe o la direccion esta mal')
    input('>>ENTER para continuar')
    sys.exit(0)
except Exception as er:
    print(f'>>Error->{er}')
    input('>>ENTER para continuar')
    sys.exit(0)
ui=[]
appState = 'login'
loggedUser = ''
loggedPassword = ''
loggedUserType = ''
loggedUserPermissions = None
id_mesa={}
opcion=0
condicion_general=1
condicion=1

files=[f for f in os.listdir(filesPath)]
for file in files:        
    with open(os.path.join(filesPath,file),'r',encoding='utf-8') as archivo:
        auxiliar=archivo.read()
    ui.append(auxiliar)
def limp(): 
    print('\n' * 50)