"""importaciones"""
"""variables"""
"""ESTABLECERE FORMATO DE MATRIZ DE PEDIDOS,RECETAS,INGREDIENTES,MENU"""
"""estados posiles del pedido
Sin hacer
en preparacion
listo
entregado
rechazado"""

PEDIDOS=[
    {'nombre': 'Michael',
     '1': [1,"EN PREPARACION"],
     '2': [1,"EN PREPARACION"],
     '3': [1,"EN PREPARACION"]},
    {'nombre': 'Juan',
     '1': [1,"EN PREPARACION"],
     '2': [1,"EN PREPARACION"],
     '3': [1,"EN PREPARACION"]},
    {'nombre': 'Martin',
     '1': [1,"EN PREPARACION"],
     '2': [1,"EN PREPARACION"],
     '3': [1,"EN PREPARACION"]
     }
        ]
"""MODIFIQUE LOS VALORES, AHORA SON LISTAS, CONTIENE CANTIDAD Y ESTADO"""
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
    }]
menu = [
    # Platos de carne
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
recetas = [
    {
        "nombre": "Bife de Chorizo",
        "ingredientes": [
            {"Bife de Chorizo": 1},
            {"Sal":"al gusto"},
            {"Pimienta" : "al gusto"}
        ],
        "tiempo_preparacion": "30 minutos",
        "instrucciones": "Sazonar el bife y asar a la parrilla."
    },
    {
        "nombre": "Ensalada Caesar",
        "ingredientes": [
            {"nombre": "Lechuga", "cantidad": "1 cabeza"},
            {"nombre": "Pollo", "cantidad": "200 g"},
            {"nombre": "Aderezo Caesar", "cantidad": "al gusto"},
            {"nombre": "Crutones", "cantidad": "al gusto"}
        ],
        "tiempo_preparacion": "15 minutos",
        "instrucciones": "Mezclar todos los ingredientes y servir."
    }
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
opcion=0
condicion_general=1
condicion=1
"""funciones"""
def menu():
    opcion=int(input("""
1.Ver pedidos
2.Administrar pedidos
3.Consultar recetas
4.Solicitar aumento de ingredientes
5.Repriorizar Pedidos
6.Salir"""))
    while opcion<1 or opcion>6:
        opcion=int(input("""
1.Ver pedidos
2.Administrar pedidos
3.Consultar recetas
4.Solicitar aumento de ingredientes
5.Repriorizar Pedidos
6.Salir"""))

    return opcion

def menu_administrar_pedidos():
    opcion=int(input("""
1.Ver pedidos
2.Administrar pedidos
3.Consultar recetas
4.Solicitar aumento de ingredientes
5.Repriorizar Pedidos
6.Salir"""))
    while opcion<1 or opcion>6:
        opcion=int(input("""
1.Ver pedidos
2.Administrar pedidos
3.Consultar recetas
4.Solicitar aumento de ingredientes
5.Repriorizar Pedidos
6.Salir"""))

    return opcion

def menu_opciones_administracion():
    
    opcion=int(input("""
1.Sin hacer
2.En preparacion
3.listo
4.Entregado
5.Rechazado
"""))
    while opcion<1 or opcion>6:
        opcion=int(input("""
1.Sin hacer
2.En preparacion
3.listo
4.Entregado
5.Rechazado
"""))
    return opcion

def impresion_pedidos(pedidos,bool,pos):
    if bool:
        print(f"\nPEDIDOS")
        for elemento in pedidos:
            for clave,valor in elemento.items():
                print(f"{clave} = {valor}")
    else:
        print(f"\nPedido de {pedidos[pos].get("nombre")}")
        for clave,valor in pedidos[pos].items():
            print(f"{clave} = {valor}")
    return
def administrar_pedidos(pedidos):
    opcion=0
    impresion_pedidos(pedidos,True,0)
    nom_pedido=input(f"ingrese nombre del pedido")
    nom_pedido=nom_pedido.lower()
    nom_pedido=nom_pedido.capitalize()
    i=0
    while i<len(pedidos) and pedidos[i].get("nombre")!=nom_pedido:
        i=i+1
    if i>=len(pedidos):
        print("no encontrado")
        return 
    else:
        """Si se encontro pedido"""
        print(f"Pedido encontrado")
        impresion_pedidos(pedidos,False,i)
        plato=input("ingrese plato a modificar")
        opcion=menu_opciones_administracion()
        if opcion==1:
            pedidos[i][plato][1]="Sin hacer"
            
        elif opcion==2:
            pedidos[i][plato][1]="En preparacion"
            
        elif opcion==3:
            pedidos[i][plato][1]="Listo"
            
        elif opcion==4:
            pedidos[i][plato][1]="Entregado"
            
        elif opcion==5:
            pedidos[i][plato][1]="Rechazado"
            
        """DEBERIAMOS HACER UN BUCLE PARA QUE MODIFIQUE CADA PLATO"""
        return pedidos
def impresion_recetas(recetas):
    i=0
    for elemento in recetas:
        print(f"{elemento.get("nombre")}")
    nombre=input("ingrese nombre de plato").capitalize()
    print(nombre)
    
    while i<len(recetas) and recetas[i].get("nombre")!=nombre:
        i=i+1
    if i>=len(recetas):
        print("nombre no encontrado")
    else:
        for clave,valor in recetas[i].items():
            if clave=="ingredientes":
                print("funcion para subimprimir esto")
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



"""programa"""
"""INGRESO COMO COCINERO"""

while condicion_general==1:
    opcion=menu()
    if opcion==1:
        """mostrar lista de diccionarios de pedidos"""
        impresion_pedidos(PEDIDOS,True,0)
    elif opcion==2:
        while condicion==1:
            pedidos=administrar_pedidos(PEDIDOS)
            condicion=int(input("Seguir modificando pedidos 1/Si 2/No"))
    elif opcion==3:
        impresion_recetas(recetas)
    elif opcion==4:
        inventario=solicitar_ingredientes(inventario)
    elif opcion==5:
        pedidos=repriorizar_pedidos(PEDIDOS)
    elif opcion==6:
        print("FIN ROL EMPLEADO.COCINERO")
        condicion_general=0
        
