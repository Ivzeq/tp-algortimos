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

pedidos = []



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
    
cliente()
            
