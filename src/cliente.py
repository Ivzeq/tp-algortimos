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

menu = [
    #Matriz con columnas: Plato, Precio, Categoría, Stock

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
    #Inicio el pedido (diccionario) con el nombre para usarlo luego
    pedido = {"nombre":nombre}
    #Asumo que ya vio el menu
    plato = input("Seleccione su plato (0 para terminar): ")

    while plato != "0": #El input me da 0 en formato string
        encontrado = False #Variable para chequear que el plato elegido este en el menu
        for item in menu:
            if item[0].lower() == plato.lower(): #Toma el plato sin importar las mayusculas
                encontrado = True
                cant = int(input(f"Seleccione una cantidad (disponible {item[3]}): "))
                if cant <= item[3]: #Si hay suficiente stock
                    if plato in pedido.keys(): #Permite sumar cantidades a un plato ya pedido
                        pedido[plato] += cant
                    else:
                        pedido[plato] = cant #Pide una cantidad para un nuevo plato
                    item[3] -= cant #Resta la cantidad pedida al stock
                    print(f"Has agregado {cant} de {plato} a tu pedido.")
                else:
                    print("No hay suficiente stock para esa cantidad.")
                break
        if encontrado == False:
            print("Ese plato no se encuentra en el menú.")
        
        plato = input("Seleccione su plato (0 para terminar): ")

    if len(pedido) >1: #pedido vacio tiene len 1 porque empieza con el elemento "nombre"
        pedidos.append(pedido) #Agrego el nuevo pedido a la lista de todos los pedidos
        print("Gracias por su pedido!")
    else:
        print("Pedido vacio!")
        

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
    nombre = input("Ingrese su nombre: ")

    print("Bienvenido, ", nombre)

    opcion = int(input("Seleccione un numero de opcion:\n1. Ver Menu\n2. Pedidos\n3. Reservas\n4. Ver estado de su pedido\n5. Ver estado de su reserva\n0. Salir\n"))

    while opcion <0 or opcion >5:
        opcion = int(input("Opcion invalida.\nSeleccione un numero de opcion:\n1. Ver Menu\n2. Pedidos\n3. Reservas\n4. Ver estado de su pedido\n5. Ver estado de su reserva\n0. Salir\n"))

    while opcion !=0:    
        if opcion == 1:
            verMenu(menu)
        elif opcion == 2:
            hacerPedido(nombre)
        elif opcion == 3:
            reservar(nombre)
        elif opcion == 4:
            verPedidos(nombre)
        else:
            verReservas(nombre)
        opcion = int(input("Seleccione un numero de opcion:\n1. Ver Menu\n2. Pedidos\n3. Reservas\n4. Ver estado de su pedido\n5. Ver estado de su reserva\n0. Salir\n"))
    print("Gracias!")
    
cliente()
            
