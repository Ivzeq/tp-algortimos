import re
import json
import config as cnf
import math
from copy import deepcopy
from functools import reduce

class IngredienteInsuficiente(Exception):
    pass

def registrarExcepcion(e):
    try:
        archivo = open('tp-algoritmos-ale\\src\\datos\\restaurant.log', 'a')
        try:
            error = f"Tipo: {type(e)} - Mensaje: {str(e)}\n"
            print(f"Ocurrió un error: {error}")
            archivo.write(error)
        finally:
            archivo.close()
    except Exception as logError:
        print(f"Error al escribir en el log: {logError}")

def intInput(prompt):
    while True:
        try:
            userInput = input(prompt)
            # Si la entrada no es un número entero no negativo
            while not re.match(r'^[0-9]+$', userInput):
                userInput = input("Entrada no válida. Por favor, ingrese un número.\n>>")
            return int(userInput)
        except ValueError:
            print("Entrada no válida. Se esperaba un número entero")
        except Exception as e:
            registrarExcepcion(e)
            print(e)

def charInput(prompt):
    while True:
        try:
            userInput = input(prompt)
            # Verifica que la entrada tenga solo letras y espacios, y no comience con espacio
            while not re.match(r'^[A-Za-z]+([ ]?[A-Za-z]+)*$', userInput):
                userInput = input("Entrada no válida. Por favor, ingrese uno o más caracteres alfabéticos. No puede comenzar con espacio.\n>>")
            return userInput
        except Exception as e:
            registrarExcepcion(e)
            print(e)

def codeInput(prompt):
    while True:
        try:
            userInput = input(prompt)
            # Verifica si el input son 3 caracteres alfabéticos
            while not re.match(r'^[A-Za-z]{3}$$', userInput):
                userInput = input("Código inválido. Ingrese un código de 3 caracteres.\n>>")
            return userInput.upper()
        except Exception as e:
            registrarExcepcion(e)
            print(e)

def confirmInput(prompt):
    while True:
        try:
            userInput = input(prompt)
            # Verifica si el input es s o n
            while not re.match(r'^[sn]{1}', userInput):
                userInput = input("Ingreso inválido. Ingrese s para confirmar, n para cancelar.\n>>")
            return userInput.lower()
        except Exception as e:
            registrarExcepcion(e)
            print(e)

def verifCodigo(lista, codigo):
    conjunto = conjuntoCodigo(lista)
    return codigo in conjunto

def cargarDatos(ruta):
    with open(ruta, 'r') as archivo:
        return json.load(archivo)

def guardarDatos(ruta, datos):
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def impresionMesas():
    mesas = cnf.mesas
    if len(mesas)%2==0:
        print(f"""
╔═════════════════════════════════════════════╗
║                                             ║
║              🍽 RESTAURANTE🍽                 ║
║                   Mesas                     ║
║                                             ║""")
        for i in range(0,len(mesas),2):
            print(f"""╠═════════════════════════════════════════════╣
{"║":<2}{"Mesa →":<17}{(mesas[i]["idMesa"]):>4}{"║":<2}{"Mesa →":<17}{(mesas[i+1]["idMesa"]):>4}║
╠----------------------║----------------------╣
{"║":<2}{"Estado →":<9}{(mesas[i]["estado"][0:12].capitalize()):>12}{"║":<2}{"Estado →":<9}{(mesas[i+1]["estado"][0:12].capitalize()):>12}║
{"║":<2}{"Cliente →":<9}{(mesas[i]["cliente"][0:12].capitalize()):>12}{"║":<2}{"Cliente →":<9}{(mesas[i+1]["cliente"][0:12].capitalize()):>12}║""")     
        print("╚═════════════════════════════════════════════╝")  
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
{"║":<2}{"Cliente →":<9}{(mesas[i]["cliente"][0:12].capitalize()):>12}{"║":<2}""")
       
        input(f"╚══════════════════════╝\n>>Enter para continuar")

def impresionMenu():#chk
    menu = cnf.menu
    print(f"""
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
║                      Menu de platos                   ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<4}║{'Plato':<28}║{'Precio':<10}║{'Categoría':<10}║
╠═══════════════════════════════════════════════════════╣""")
    for idx, plato in enumerate(menu, start=1):
        print(f"║{idx:<4}║{plato[1]:<28}║{plato[2]:<10}║{plato[3]:<9} ║")
    print("""╚═══════════════════════════════════════════════════════╝""")
    input("Presione Enter para continuar>>")

def impresionPedidos(pedidos):
    for idx, pedido in enumerate(pedidos, start=1):
        estado = pedido["estado"]
        print(f"""╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
{"║":<2}{idx}: Pedido de → {pedido["nombre"].capitalize():<29}Mesa → {pedido["mesa"]:<3}║                    
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<3}║{'Plato':<28}║{'Cant':<4}║{'Estado':<17}║
╠═══════════════════════════════════════════════════════╣""")
        for plato in pedido['platos']:
            print(f"║{(pedido['platos'].index(plato)+1):<3}║{plato[0]:<28}║{plato[1]:<4}║{estado.capitalize():<17}║")
        print("""╚═══════════════════════════════════════════════════════╝""")

def resumenPedido(nombre, mesa, pedido):
    total = totalCuenta(pedido)
    print(f"""╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
{"║":<2}Pedido de → {nombre.capitalize():<31}Mesa → {mesa:<3} ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<5}║{'Plato':<28}║{'Cant':<20}║
╠═══════════════════════════════════════════════════════╣""")
    
    # Mostrar los platos del pedido
    for idx, plato in enumerate(pedido['platos'], start=1):
        print(f"║{idx:<5}║{plato[0]:<28}║{plato[1]:<20}║")
    
    # Imprimir el total en un recuadro
    print(f"""╠═══════════════════════════════════════════════════════╣
║                    Total: {total:<25}   ║
╚═══════════════════════════════════════════════════════╝""")

def impresionRecetas():
    recetas = cnf.recetas
    ordenadas = sorted(recetas, key=lambda r: r['nombre'])
    print("Listado de recetas:")
    for receta in ordenadas:
        print(f"{receta['id']}: {receta['nombre']}")

"""def impresionIngredientes(ingredientes):
    ordenados = sorted(ingredientes, key=lambda r: r['nombre'])
    print("Listado de recetas:")
    for ingrediente in ordenados:
        print(f"{ingrediente['id']}: {ingrediente['nombre']}")"""

def impresionIngredientes(ingredientes, columnas=3):
    ordenados = sorted(ingredientes, key=lambda r: r['nombre'])
    filas = math.ceil(len(ordenados) / columnas)
    columnasIngredientes = [ordenados[i*filas:(i+1)*filas] for i in range(columnas)]
    print("Listado de Ingredientes:")
    
    for i in range(filas):
        fila = ""
        for col in range(columnas):
            if i < len(columnasIngredientes[col]):  # Si hay suficientes ingredientes para esta fila
                ingrediente = columnasIngredientes[col][i]
                fila += f"|{ingrediente['id']}: {ingrediente['nombre']:<20} ({ingrediente['cantidad']})|  "
        print(fila)

def verificarStock(codReceta, recetas,ingredientes):
    receta = list(filter(lambda r: r['id'] == codReceta, recetas))[0]
    for ingReceta in receta['ingredientes']:
        for nombreIngrediente, cantIngrediente in ingReceta.items():
            # Buscar el ingrediente en el stock
            ingredienteStock = next((i for i in ingredientes if i['nombre'].lower() == nombreIngrediente.lower()), None)
            # Verificar si hay suficiente cantidad en el stock
            if ingredienteStock['cantidad'] < cantIngrediente:
                return False
    
    return True


def restarIngredientes(codReceta, recetas, ingredientes):
    # Buscar la receta por código usando filter
    receta = list(filter(lambda r: r['id'] == codReceta, recetas))[0]

    try:
        # Verificar si los ingredientes están disponibles en la cantidad suficiente
        if verificarStock(ingredientes, receta):
            # Si los ingredientes son suficientes, restar las cantidades
            restarAuxIngredientes(codReceta, recetas, ingredientes)
            guardarDatos(cnf.rutas("ingredientes"), ingredientes)
        else:
            raise IngredienteInsuficiente("Cantidad de ingredientes insuficiente.\n")
    except IngredienteInsuficiente as e:
        registrarExcepcion(e)
    
#Resta ingredientes pero no modifica el json
def restarAuxIngredientes(codReceta, recetas, ingredientes):
    # Buscar la receta por código usando filter
    receta = list(filter(lambda r: r['id'] == codReceta, recetas))[0]

    for ingReceta in receta['ingredientes']:
        for nombreIngrediente, cantIngrediente in ingReceta.items():
            # Restar la cantidad del stock
            ingredienteStock = next(i for i in ingredientes if i['nombre'].lower() == nombreIngrediente.lower())
            ingredienteStock['cantidad'] -= cantIngrediente

def sumarAuxIngredientes(codReceta, recetas, ingredientes):
    # Buscar la receta por código usando filter
    receta = list(filter(lambda r: r['id'] == codReceta, recetas))[0]

    for ingReceta in receta['ingredientes']:
        for nombreIngrediente, cantIngrediente in ingReceta.items():
            # Restar la cantidad del stock
            ingredienteStock = next(i for i in ingredientes if i['nombre'].lower() == nombreIngrediente.lower())
            ingredienteStock['cantidad'] += cantIngrediente

def restarStock(codReceta, recetas, ingredientes, cant):
    for i in range(cant):
        restarAuxIngredientes(codReceta, recetas, ingredientes)
    guardarDatos(cnf.rutas["ingredientes"], ingredientes)

def devolverStock(codReceta, recetas, ingredientes, cant):
    for i in range(cant):
        sumarAuxIngredientes(codReceta, recetas, ingredientes)
    guardarDatos(cnf.rutas["ingredientes"], ingredientes)
    
def conjuntoIngredientes(ingredientes):
    return set(ingrediente['nombre'].lower() for ingrediente in ingredientes if ingrediente['cantidad']>0)

def conjuntoCodigo(lista):
    return set(diccionario['id'] for diccionario in lista)

def conjuntoIngrReceta(codReceta, recetas):
    receta = list(filter(lambda r: r['id'] == codReceta, recetas))[0]
    return set([list(ing.keys())[0].lower() for ing in receta['ingredientes']])

def calcularStock(codReceta, recetas, ingredientes):
    # Verificar si los ingredientes necesarios están disponibles en el stock
    if not conjuntoIngrReceta(codReceta, recetas).issubset(conjuntoIngredientes(ingredientes)):
        return 0
    
    # Crear una copia local de los ingredientes para evitar modificar el original
    ingredientesLocal = deepcopy(ingredientes)
    
    # Resta los ingredientes necesarios para preparar una unidad
    restarAuxIngredientes(codReceta, recetas, ingredientesLocal)
    
    # Llamada recursiva con la copia actualizada de ingredientes
    return 1 + calcularStock(codReceta, recetas, ingredientesLocal)


def pedirIngredientes(ingredientes, compras):
    while True:
        #Primero mostrar el stock actual
        impresionIngredientes(ingredientes)
        #Mostrar el pedido hasta ahora para poder verificar
        print("\nEl pedido actual es el siguiente:\n")
        print(f"{'ID':<10}{'Nombre':<20}{'Cantidad':<10}")
        print("="*40)
        for pedido in compras:
            print(f"{pedido['id']:<10}{pedido['nombre']:<20}{pedido['cantidad']:<10}")
        cod = codeInput("\n\nIngrese el código del ingrediente:\n>>")
        #Verificar que el codigo exista
        while not verifCodigo(ingredientes, cod):
            cod = codeInput("Código no válido. Ingrese un código existente.\n>>")
        cant = intInput("Ingrese la cantidad a pedir:\n>>")
        #Buscar el ingrediente
        ingrediente = next((ing for ing in ingredientes if ing["id"] == str(cod)), None)
        #ver si esta ya en el pedido
        enPedido = next((ing for ing in compras if ing["id"] == str(cod)), None)

        if enPedido:
            enPedido["cantidad"] += cant
        else:
            agregar = {"id": str(cod), "nombre": ingrediente["nombre"], "cantidad": cant}
            compras.append(agregar)
        
        seguir = input("¿Desea agregar más ingredientes? (s/n):\n>>").strip().lower()
        if seguir != "s":
            break
    #Actualizar archivo de pedido de ingredientes
    guardarDatos(cnf.rutas["compras"], compras)

def impresionCompras(compras):
    print("\nEl pedido actual es el siguiente:\n")
    print(f"{'ID':<10}{'Nombre':<20}{'Cantidad':<10}")
    print("="*40)
    for pedido in compras:
        print(f"{pedido['id']:<10}{pedido['nombre']:<20}{pedido['cantidad']:<10}")

def modificarCompras(compras):
    if len(compras) > 0:
        while True:
            impresionCompras(compras)
            cod = codeInput("\n\nIngrese el código del ingrediente:\n>>")
            while not verifCodigo(compras, cod):
                cod = codeInput("Código no válido. Ingrese un código existente.\n>>")
            cant = intInput("Ingrese la cantidad total deseada:\n>>") 

            enPedido = next((ing for ing in compras if ing["id"] == str(cod)), None)
            if enPedido:
                enPedido["cantidad"] = cant 
            
            seguir = input("¿Desea modificar más ingredientes del pedido? (s/n):\n>>").strip().lower()
            if seguir != "s":
                break
        guardarDatos(cnf.rutas["compras"], compras)
    else:
        print("No hay pedidos de ingredientes pendientes.")
        return

def actualizarStock(menu, recetas, ingredientes):
    for plato in menu:
        codReceta = plato[0]
        stock = calcularStock(codReceta, recetas, ingredientes)
        plato[4] = stock
        guardarDatos(cnf.rutas["menu"], menu)

def actualizarIngredientes(ingredientes, compras):
    agregadas = []
    for compra in compras:
        for ingrediente in ingredientes:
            if ingrediente["id"] == compra["id"]:
                ingrediente["cantidad"] += compra["cantidad"]
                agregadas.append(compra)
                break
    
    compras = [compra for compra in compras if compra not in agregadas]

    guardarDatos(cnf.rutas["ingredientes"], ingredientes)
    guardarDatos(cnf.rutas["compras"], compras)

def totalCuenta(pedido):
    precios = {plato[1].lower(): plato[2] for plato in cnf.menu}
    total = reduce(lambda subtotal, platoPedido: subtotal + precios[platoPedido[0].lower()] * platoPedido[1], pedido["platos"], 0)
    return total

def hacerPedido(nombre, mesa):#chk
    menu = cnf.menu
    recetas = cnf.recetas
    ingredientes = cnf.ingredientes
    pedidos = cnf.pedidos
    pedido={"nombre":nombre,
            "mesa":mesa,
            "estado": "Recibido",
            "platos":[]}
    impresionMenu()
    while True:
        try:
            plato = intInput("\nIngrese numero de plato (0 para terminar):\n>>")
            if plato not in range(1, len(menu) + 1) and plato != 0:
                raise ValueError
        except ValueError as e:
            registrarExcepcion(e)
            print(' >>Opcion ingresada no válida\n>> Ingrese una opción válida\n>>')
        else:
            break
    while plato != 0:
        nombrePlato=menu[plato-1][1].lower()
        codPlato = menu[plato-1][0]
        while True:
            try:
                cant = int(input(f"Seleccione una cantidad (disponible {menu[plato-1][4]}): "))
                if cant > menu[plato-1][4]:
                    raise ValueError
            except ValueError as e:
                registrarExcepcion(e)
                print(f'>> Opcion ingresada no válida\n>> Ingrese opción válida')
            except Exception as ms:
                registrarExcepcion(ms)
                ms=str(ms)
                print(f'>>Ha ocurrido un error -> {ms}')
            else:
                break
        if cant <= menu[plato-1][4]:  # Si hay suficiente stock
            # Si ya hay platos en el pedido
            platoExistente = False
            for elemento in pedido["platos"]:
                if elemento[0].lower() == nombrePlato.lower():
                    # Si el plato ya está en el pedido, solo actualiza la cantidad
                    elemento[1] += cant
                    platoExistente = True
                    break

            if not platoExistente:
                # Si el plato no está en el pedido, se agrega
                pedido['platos'].append([nombrePlato, cant, codPlato])

            #Resta la cantidad pedida al stock
            restarStock(codPlato, recetas, ingredientes, cant)
            #actualiza el stock total
            actualizarStock(menu, recetas, ingredientes)
            print(f"Has agregado {cant} de {nombrePlato} a tu pedido.")
        while True:
            try:
                plato = int(input("\nIngrese número de plato (0 para terminar):\n>>"))
                if plato not in range(1, len(cnf.menu) + 1) and plato != 0:
                    raise ValueError
            except ValueError as e:
                registrarExcepcion(e)
                print('>>Opción ingresada no válida\n>> Ingrese una opción válida')
            else:
                break
    resumenPedido(nombre, mesa, pedido)
    confirma = confirmInput("\nDesea confirmar su pedido? s/n\n>>")
    if confirma == 's':
        pedidos.append(pedido)
        guardarDatos(cnf.rutas['pedidos'], pedidos)
        print(f"Gracias {nombre}! Tu pedido fue confirmado.")
    else:
        if len(pedido["platos"]) > 0:
            for plato in pedido["platos"]:
                codPlato = plato[2]
                cant = plato[1]
                devolverStock(codPlato, recetas, ingredientes, cant)
                actualizarStock(menu, recetas, ingredientes)
        print("Pedido cancelado.")

def verPedido(nombre, mesa):
    pedidos = cnf.pedidos
    pedidosCliente = [pedido for pedido in pedidos if pedido['nombre'].lower() == nombre.lower() and pedido['mesa'] == mesa]
    impresionPedidos(pedidosCliente)
    if len(pedidosCliente) > 0:
        confirma = confirmInput("\nDesea cancelar algun pedido? s/n\n>>")
        if confirma == 's' and len(pedidosCliente) >1:
            cancelado = intInput(f"Qué número de pedido desea cancelar? entre 1 y {len(pedidosCliente)}\n>>")
            while cancelado not in range(1, len(pedidosCliente)+1):
                cancelado = intInput(f"Debe seleccionar un número entre 1 y {len(pedidosCliente)}\n>>")
            pedidos.remove(pedidosCliente[cancelado-1])
            guardarDatos(cnf.rutas["pedidos"], pedidos)
            print("Pedido eliminado exitosamente.\n")
        elif confirma == 's':
            pedidos.remove(pedidosCliente[0])
            guardarDatos(cnf.rutas['pedidos'], pedidos)
            print("Pedido eliminado exitosamente.\n")
    else:
        print("No se encontraron pedidos activos.")

def avanzarPedidoCocina():
    pedidos = cnf.pedidos
    comandas = [pedido for pedido in pedidos if pedido["estado"] in cnf.permisosEstadosCocina]

    if len(comandas) == 0:
        print("No hay comandas activas en este momento.")
        return
    
    impresionPedidos(comandas)
    avanzar = intInput(f"Qué pedido desea avanzar? entre 1 y {len(comandas)}. 0 para cancelar.\n>>")
    if avanzar == 0:
        return
    while avanzar not in range(1, len(comandas)+1):
        avanzar = intInput(f"Debe seleccionar un número entre 1 y {len(comandas)}\n>>")
    seleccionado = comandas[avanzar-1]
    actual = seleccionado["estado"]
    for avance in cnf.avanceEstados:
        if actual in avance:
            seleccionado["estado"] = avance[actual]
            print(f"El pedido de {seleccionado['nombre']} en la mesa {seleccionado['mesa']} ahora está {seleccionado['estado'].capitalize()}.")
            guardarDatos(cnf.rutas["pedidos"], pedidos)
            break

def avanzarPedidoSalon():
    pedidos = cnf.pedidos
    comandas = [pedido for pedido in pedidos if pedido["estado"] in cnf.permisosEstadosSalon]

    if len(comandas) == 0:
        print("No hay comandas activas en este momento.")
        return
    
    impresionPedidos(comandas)
    avanzar = intInput(f"Qué pedido desea avanzar? entre 1 y {len(comandas)}. 0 para cancelar\n>>")
    if avanzar == 0:
        return
    while avanzar not in range(1, len(comandas)+1):
        avanzar = intInput(f"Debe seleccionar un número entre 1 y {len(comandas)}\n>>")
    seleccionado = comandas[avanzar-1]
    actual = seleccionado["estado"]
    for avance in cnf.avanceEstados:
        if actual in avance:
            seleccionado["estado"] = avance[actual]
            print(f"El pedido de {seleccionado['nombre']} en la mesa {seleccionado['mesa']} ahora está {seleccionado['estado'].capitalize()}.")
            if seleccionado['estado'].lower() == "finalizado":
                finalizados = cnf.finalizados
                finalizados.append(seleccionado)
                guardarDatos(cnf.rutas["finalizados"], finalizados)
                pedidos.remove(seleccionado)
            guardarDatos(cnf.rutas["pedidos"], pedidos)
            break

def consultarReceta():
    recetas = cnf.recetas
    impresionRecetas()
    consulta = codeInput("Ingrese el código de la receta a consultar:\n>>")
    receta = next((r for r in recetas if r["id"] == consulta), None)
    
    nombre = receta["nombre"]
    tiempo = receta["tiempo"]
    instrucciones = receta["instrucciones"]
    ingredientes = receta["ingredientes"]

    print(f"\n{'=' * 40}")
    print(f"Receta: {nombre}")
    print(f"Tiempo de preparación: {tiempo}")
    print(f"\n{'Ingredientes':^40}")
    print(f"{'-' * 40}")

    for ingrediente in ingredientes:
        for nombreIngrediente, cantidad in ingrediente.items():
            print(f"{nombreIngrediente:<30} {cantidad:>5}")

    print(f"\n{'Instrucciones':^40}")
    print(f"{'-' * 40}")
    print(instrucciones)
    print(f"{'=' * 40}\n")

def cerrarMesa():
    impresionMesas()
    seleccionada = intInput("Qué mesa desea cerrar? 0 para salir\n>>")
    while seleccionada not in range(0, len(cnf.mesas)+1):
        seleccionada = intInput(f"Debe seleccionar una mesa entre 1 y {len(cnf.mesas)}, o 0 para salir.\n>>")
    if seleccionada == 0:
        return
    else:
        mesa = next((m for m in cnf.mesas if m["idMesa"] == str(seleccionada)), None)
        if mesa:
            mesa["estado"] = "Libre"
            mesa["cliente"] = "Sin reserva"
            print(f"La mesa {mesa['idMesa']} ha sido cerrada exitosamente.")

            guardarDatos(cnf.rutas["mesas"], cnf.mesas)

def ingresoAdmin():
    passwords = list(map(lambda item: list(item.keys())[0], cnf.admins))
    ingreso = charInput("Ingrese su contraseña:\n>>")
    if ingreso in passwords:
        adminDict = next(item for item in cnf.admins if list(item.keys())[0] == ingreso)
        user = list(adminDict.values())[0]
        print(f"Bienvenido, {user.capitalize()}.")
        administrarPedidos(cnf.pedidos)
    else:
        print("Contraseña incorrecta. Intente nuevamente.")

def cambiarEstados(pedidos):
    estadosDisponibles = cnf.estadosPedidos
    impresionPedidos(pedidos)
    seleccion = intInput(f"Seleccione un pedido entre 1 y {len(pedidos)}. 0 para salir.\n>>")
    if seleccion == 0:
        return
    while seleccion not in range(1, len(pedidos) + 1):
        seleccion = intInput(f"Debe seleccionar un número entre 1 y {len(pedidos)}. 0 para salir.\n>>")
        if seleccion == 0:
            return
    pedidoSeleccionado = pedidos[seleccion - 1]
                
    estadoSeleccionado = intInput(f"{cnf.estadosPedidosUI}")
    while estadoSeleccionado not in range(1, len(estadosDisponibles) + 1):
        estadoSeleccionado = intInput(f"Debe seleccionar un número entre 1 y {len(estadosDisponibles)}:. 0 para salir.\n>>")
    if seleccion == 0:
        return
        
    nuevoEstado = estadosDisponibles[estadoSeleccionado - 1]
    pedidoSeleccionado["estado"] = nuevoEstado
    print(f"El estado del pedido de {pedidoSeleccionado['nombre']} ha cambiado a: {nuevoEstado.capitalize()}")

def finalizarPedido(pedidos):
    impresionPedidos(pedidos)
    seleccion = intInput(f"Seleccione un pedido entre 1 y {len(pedidos)}. 0 para salir.\n>>")
    if seleccion == 0:
        return
    while seleccion not in range(1, len(pedidos) + 1):
        seleccion = intInput(f"Debe seleccionar un número entre 1 y {len(pedidos)}. 0 para salir.\n>>")
        if seleccion == 0:
            return
    pedidoSeleccionado = pedidos[seleccion - 1]
    cnf.finalizados.append(pedidoSeleccionado)
    pedidos.remove(pedidoSeleccionado)
    print(f"El pedido de {pedidoSeleccionado['nombre']} ha sido finalizado.")
    guardarDatos(cnf.rutas["finalizados"], cnf.finalizados)

def cancelarPedido(pedidos):
        impresionPedidos(pedidos)
        seleccion = intInput(f"Seleccione un pedido entre 1 y {len(pedidos)}. 0 para salir.\n>>")
        if seleccion == 0:
            return
        while seleccion not in range(1, len(pedidos) + 1):
            seleccion = intInput(f"Debe seleccionar un número entre 1 y {len(pedidos)}. 0 para salir.\n>>")
            if seleccion == 0:
                return
        pedidoSeleccionado = pedidos[seleccion - 1]
        pedidos.remove(pedidoSeleccionado)
        print(f"El pedido de {pedidoSeleccionado['nombre']} ha sido cancelado.")

def repriorizarPedidos(pedidos):
    impresionPedidos(pedidos)
    seleccion = intInput(f"Seleccione un pedido entre 1 y {len(pedidos)}. 0 para salir.\n>>")
    if seleccion == 0:
        return
    while seleccion not in range(1, len(pedidos) + 1):
        seleccion = intInput(f"Debe seleccionar un número entre 1 y {len(pedidos)}. 0 para salir.\n>>")
    if seleccion == 0:
        return
    seleccion -= 1
    nuevaPos = intInput("Ingrese la nueva posición (1 para la primera):\n>>") - 1
    pedidoSeleccionado = pedidos[seleccion]
    # Elimino el pedido de su posicion original
    pedidos[:] = pedidos[:seleccion] + pedidos[seleccion + 1:]
    # Si la nueva posicion excede la longitud de la lista, lo agrego al final
    if nuevaPos >= len(pedidos):
        pedidos.append(pedidoSeleccionado)
    # Si ingresa 0 o negativo, lo pone primero en la lista
    elif nuevaPos <= 0:
        pedidos[:0] = [pedidoSeleccionado]
    else:
        # Inserto el pedido en la nueva posicion usando rebanado
        pedidos[nuevaPos:nuevaPos] = [pedidoSeleccionado]
    print(f"El pedido de '{pedidoSeleccionado['nombre']}' ha sido movido a la posición {nuevaPos + 1}.")
    guardarDatos(cnf.rutas["pedidos"], pedidos)

def administrarPedidos(pedidos):
    if len(pedidos) == 0:
        print("No hay pedidos activos en este momento.")
        return
    
    while True:
        accion = intInput(f"{cnf.adminUI}")
        while accion not in [1, 2, 3, 4, 5, 6, 7]:
            accion = intInput("Debe seleccionar una acción válida (1 a 7):\n>>")
        
        if accion == 1:  # Cambiar estado
            cambiarEstados(pedidos)
        
        elif accion == 2:  # Finalizar pedido
            finalizarPedido(pedidos)
        
        elif accion == 3:  # Cancelar pedido
            cancelarPedido(pedidos)
        
        elif accion == 4: #Repriorizar pedidos
            repriorizarPedidos(pedidos)
        
        elif accion == 5: #Cambiar pedidos de ingredientes
            modificarCompras(cnf.compras)
        
        elif accion == 6: #Ingresar compras
            compras = cnf.compras
            impresionCompras(compras)
            ingreso = confirmInput("Desea ingresar estos ingredientes al stock? s/n\n>>")
            if ingreso == 's':
                actualizarIngredientes(cnf.ingredientes, compras)
                print("Ingredientes actualizados.")
            else:
                return
        
        else: #Salir
            return
        
        # Guardar cambios
        guardarDatos(cnf.rutas["pedidos"], pedidos)