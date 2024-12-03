import re
import json
import config as cnf
import math
import inspect
from copy import deepcopy
from functools import reduce
from datetime import datetime

class IngredienteInsuficiente(Exception):
    #Excepción para cuando no hay suficiente stock de un ingrediente para un plato
    def __init__(self, nombreIngrediente, cantidadRequerida, cantidadDisponible):
        self.nombreIngrediente = nombreIngrediente
        self.cantidadRequerida = cantidadRequerida
        self.cantidadDisponible = cantidadDisponible
        super().__init__(f"Ingrediente insuficiente: {nombreIngrediente} (Requerido: {cantidadRequerida}, Disponible: {cantidadDisponible})")

class ArchivoInexistente(Exception):
    #Escepción para cuando la ruta no es correcta
    def __init__(self, ruta):
        self.ruta = ruta
        super().__init__(f"El archivo {ruta} no existe o no puede ser encontrado.")

class FormatoInvalido(Exception):
    #Excepción para datos que no cumplen con el formato esperado.
    def __init__(self, ruta, mensaje="Formato no válido"):
        self.ruta = ruta
        super().__init__(f"{mensaje} en el archivo: {ruta}")

class ConfirmacionCancelada(Exception):
    #Excepción para manejar cancelaciones explícitas por parte del usuario.
    def __init__(self, mensaje="El usuario canceló la operación."):
        super().__init__(mensaje)

class MesaOcupada(Exception):
    #Excepción para manejar el caso de mesas ocupadas. Evita que clientes accedan a mesas que no estén libres
    def __init__(self, idMesa, clienteActual):
        self.idMesa = idMesa
        self.clienteActual = clienteActual
        super().__init__(f"La mesa {idMesa} ya está ocupada.")



def registrarExcepcion(e,msg, ruta_log="tp-algoritmos\\src\\datos\\restaurant.log"):
    try:
        funcion = inspect.stack()[1].function

        archivo = open(ruta_log, 'a', encoding='utf-8')
        try:
            error = (
                f"\nFecha: {datetime.now()}\n"
                f"Función: {funcion}\n"
                f"Tipo: {type(e).__name__}\n"
                f"Mensaje: {str(e)}\n"
                f"\t{msg}"
            )
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
            msg=(f'Error durante la entrada de un entero\n\tContexto: {prompt}\n')
            registrarExcepcion(e,msg)


def charInput(prompt):
    while True:
        try:
            userInput = input(prompt)
            # Verifica que la entrada tenga solo letras y espacios, y no comience con espacio
            while not re.match(r'^[A-Za-z]+([ ]?[A-Za-z]+)*$', userInput):
                userInput = input("Entrada no válida. Por favor, ingrese uno o más caracteres alfabéticos. No puede comenzar con espacio.\n>>")
            return userInput
        except Exception as e:
            msg=(f'Error durante la entrada de un caracter\n\tContexto: {prompt}\n')
            registrarExcepcion(e,msg)
            raise


def codeInput(prompt):
    while True:
        try:
            userInput = input(prompt)
            # Verifica si el input son exactamente 4 dígitos numéricos
            while not re.match(r'^\d{4}$', userInput):
                userInput = input("Código inválido. Ingrese un código de 4 números.\n>>")
            return userInput
        except Exception as e:
            registrarExcepcion(e)
            print("Ocurrió un error. Por favor, intente nuevamente.")


def confirmInput(prompt):
    while True:
        try:
            userInput = input(prompt)
            # Verifica si el input es s o n
            while not re.match(r'^[sn]{1}', userInput.lower()):
                userInput = input("Ingreso inválido. Ingrese s para confirmar, n para cancelar.\n>>")
            return userInput.lower()
        except Exception as e:
            msg=(f'Error durante la entrada de un caracter\n\tContexto: {prompt}\n')
            registrarExcepcion(e,msg)
            print(e)

def verifCodigo(lista, codigo):
    conjunto = conjuntoCodigo(lista)
    return codigo in conjunto

def cargarDatos(ruta):
    try:    
        with open(ruta, encoding = 'utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError as e:
        registrarExcepcion(e, f"Archivo no encontrado: {ruta}.")
        print(f"Error: El archivo {ruta} no existe.")
    except json.JSONDecodeError as e:
        registrarExcepcion(e, f"Error al decodificar JSON en el archivo: {ruta}.")
        print(f"Error: El archivo {ruta} contiene datos no válidos.")
    except Exception as e:
        registrarExcepcion(e, f"Error inesperado al cargar datos desde {ruta}.")
        print(f"Error inesperado al cargar datos desde {ruta}.")

def guardarDatos(ruta, datos):
    try:    
        with open(ruta, 'w', encoding= 'utf-8') as archivo:
            json.dump(datos, archivo, indent=4)
    except PermissionError as e:
        registrarExcepcion(e, f"Permiso denegado para guardar en el archivo: {ruta}.")
        print(f"Error: No se tienen permisos para guardar en {ruta}.")
        raise
    except TypeError as e:
        registrarExcepcion(e, f"Error al serializar datos para guardar en {ruta}.")
        print(f"Error: Los datos proporcionados no son serializables.")
        raise
    except Exception as e:
        registrarExcepcion(e, f"Error inesperado al guardar datos en {ruta}.")
        print(f"Error inesperado al guardar datos en {ruta}.")
        raise

def impresionMesas(mesas):
    if len(mesas)%2==0:
        output = f"""
╔═════════════════════════════════════════════╗
║                                             ║
║              🍽 RESTAURANTE🍽                 ║
║                   Mesas                     ║
║                                             ║"""
        for i in range(0,len(mesas),2):
            output += f"""\n╠═════════════════════════════════════════════╣
{"║":<2}{"Mesa →":<17}{(mesas[i]["idMesa"]):>4}{"║":<2}{"Mesa →":<17}{(mesas[i+1]["idMesa"]):>4}║
╠----------------------║----------------------╣
{"║":<2}{"Estado →":<9}{(mesas[i]["estado"][0:12].capitalize()):>12}{"║":<2}{"Estado →":<9}{(mesas[i+1]["estado"][0:12].capitalize()):>12}║
{"║":<2}{"Cliente →":<9}{(mesas[i]["cliente"][0:12].capitalize()):>12}{"║":<2}{"Cliente →":<9}{(mesas[i+1]["cliente"][0:12].capitalize()):>12}║""" 
        output += "\n╚═════════════════════════════════════════════╝"
        return output
    else:
        output = f"""
╔══════════════════════╗
║                      ║
║   🍽 RESTAURANTE🍽     ║
║         Mesas        ║
║                      ║"""
        for i in range(0,len(mesas)):
            output += f"""\n╠══════════════════════╣
{"║":<5}{"Mesa → ".center(12)}{mesas[i]["idMesa"]:<6}║
╠══════════════════════╣
{"║":<2}{"Estado →":<9}{(mesas[i]["estado"][0:12].capitalize()):>12}{"║":<2}
{"║":<2}{"Cliente →":<9}{(mesas[i]["cliente"][0:12].capitalize()):>12}{"║":<2}"""
       
        output += f"\n╚══════════════════════╝"
        return output

def impresionMenu(menu):
    output = f"""
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
║                      Menu de platos                   ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<4}║{'Plato':<28}║{'Precio':<10}║{'Categoría':<10}║
╠═══════════════════════════════════════════════════════╣"""
    for idx, plato in enumerate(menu, start=1):
        output += f"\n║{idx:<4}║{plato[1]:<28}║{plato[2]:<10}║{plato[3]:<9} ║"
    output += """\n╚═══════════════════════════════════════════════════════╝"""
    return output

def impresionStockMenu(menu):
    output = f"""
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
║                      Menu de platos                   ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<4}║{'Plato':<28}║{'Precio':<10}║{'Categoría':<10}║
╠═══════════════════════════════════════════════════════╣"""
    for idx, plato in enumerate(menu, start=1):
        if plato[4] > 0: #No muestra platos sin stock
            output += f"\n║{idx:<4}║{plato[1]:<28}║{plato[2]:<10}║{plato[3]:<9} ║"
    output += """\n╚═══════════════════════════════════════════════════════╝"""
    return output

def impresionPedidos(pedidos):
    lista = []
    for idx, pedido in enumerate(pedidos, start=1):
        estado = pedido["estado"]
        output = f"""╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
{"║":<2}{idx}: Pedido de → {pedido["nombre"].capitalize():<29}Mesa → {pedido["mesa"]:<3}║                    
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<3}║{'Plato':<28}║{'Cant':<4}║{'Estado':<17}║
╠═══════════════════════════════════════════════════════╣"""
        for plato in pedido['platos']:
            output += f"\n║{(pedido['platos'].index(plato)+1):<3}║{plato[0]:<28}║{plato[1]:<4}║{estado.capitalize():<17}║"
        output += """\n╚═══════════════════════════════════════════════════════╝"""
        lista.append(output)
    return lista

def resumenPedido(nombre, mesa, pedido):
    total = totalCuenta(pedido)
    output = f"""╔═══════════════════════════════════════════════════════╗
║                                                       ║
║                     🍽 RESTAURANTE🍽                    ║
{"║":<2}Pedido de → {nombre.capitalize():<31}Mesa → {mesa:<3} ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║{'Num':<5}║{'Plato':<28}║{'Cant':<20}║
╠═══════════════════════════════════════════════════════╣"""
    
    # Mostrar los platos del pedido
    for idx, plato in enumerate(pedido['platos'], start=1):
        output += f"\n║{idx:<5}║{plato[0]:<28}║{plato[1]:<20}║"
    
    # Imprimir el total en un recuadro
    output += f"""\n╠═══════════════════════════════════════════════════════╣
║                    Total: {total:<25}   ║
╚═══════════════════════════════════════════════════════╝"""
    return output

def impresionRecetas(recetas):
    ordenadas = sorted(recetas, key=lambda r: r['id'])
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
    maxCant = max(len(str(ingrediente['cantidad'])) for ingrediente in ingredientes)
    filas = math.ceil(len(ordenados) / columnas)
    columnasIngredientes = [ordenados[i*filas:(i+1)*filas] for i in range(columnas)]
    print("Listado de Ingredientes:")
    
    for i in range(filas):
        fila = ""
        for col in range(columnas):
            if i < len(columnasIngredientes[col]):  # Si hay suficientes ingredientes para esta fila
                ingrediente = columnasIngredientes[col][i]
                fila += f"|{ingrediente['id']}: {ingrediente['nombre']:<20} ({ingrediente['cantidad']:<{maxCant}})|  "
        print(fila)

def verificarStock(codReceta, recetas,ingredientes):
    receta = list(filter(lambda r: r['id'] == codReceta, recetas))[0]
    for ingReceta in receta['ingredientes']:
        for nombreIngrediente, cantIngrediente in ingReceta.items():
            # Buscar el ingrediente en el stock
            ingredienteStock = next((i for i in ingredientes if i['nombre'].lower() == nombreIngrediente.lower()), None)
            # Verificar si hay suficiente cantidad en el stock
            if not ingredienteStock or ingredienteStock['cantidad'] < cantIngrediente:
                return False
    
    return True


def restarIngredientes(codReceta, recetas, ingredientes):
    # Buscar la receta por código usando filter
    receta = list(filter(lambda r: r['id'] == codReceta, recetas))[0]

    try:
        # Verificar si los ingredientes están disponibles en la cantidad suficiente
        if verificarStock(codReceta, recetas,ingredientes):
            # Si los ingredientes son suficientes, restar las cantidades
            restarAuxIngredientes(codReceta, recetas, ingredientes)
            guardarDatos(cnf.rutas["ingredientes"], ingredientes)
        else:
            for ingReceta in receta['ingredientes']:
                for nombreIngrediente, cantIngrediente in ingReceta.items():
                    ingredienteStock = next((i for i in ingredientes if i['nombre'].lower() == nombreIngrediente.lower()), None)
                    if not ingredienteStock or ingredienteStock['cantidad'] < cantIngrediente:
                        raise IngredienteInsuficiente(
                            nombreIngrediente,
                            cantIngrediente,
                            ingredienteStock['cantidad'] if ingredienteStock else 0
                        )
    except IngredienteInsuficiente as e:
        msg=(f'Error ingredientes insuficientes\n')
        registrarExcepcion(e,msg)
        raise
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
    
def conjuntoCodigo(lista):
    return set(diccionario['id'] for diccionario in lista)

def calcularStock(codReceta, recetas, ingredientes):
    try:
        receta = next((r for r in recetas if r['id'] == codReceta), None)
        if not receta:
            return 0
        # Verificar si los ingredientes necesarios están disponibles en el stock
        for ingReceta in receta['ingredientes']:
                for nombreIngrediente, cantidadNecesaria in ingReceta.items():
                    ingredienteStock = next((i for i in ingredientes if i['nombre'].lower() == nombreIngrediente.lower()), None)
                    if not ingredienteStock or ingredienteStock['cantidad'] < cantidadNecesaria:
                        return 0
    except StopIteration as e:
        registrarExcepcion(e, f"Error en calcularStock: Ingrediente no encontrado en la receta {codReceta}.")
        print(f"Error: No se encontró un ingrediente necesario en la receta {codReceta}.")
        return 0
    except KeyError as e:
        registrarExcepcion(e, f"Error en calcularStock: Clave faltante {e} en la estructura de datos.")
        print(f"Error: Falta la clave {e} en las estructuras de datos.")
        return 0
    except TypeError as e:
        registrarExcepcion(e, f"Error en calcularStock: Tipo de dato incorrecto en recetas o ingredientes.")
        print("Error: Tipo de dato incorrecto en recetas o ingredientes.")
        return 0
    except ValueError as e:
        registrarExcepcion(e, f"Error en calcularStock: Valor no válido encontrado al procesar recetas o ingredientes.")
        print("Error: Valor no válido encontrado al procesar recetas o ingredientes.")
        return 0
    except IngredienteInsuficiente as e:
        registrarExcepcion(e, f"Error en calcularStock: Ingredientes insuficientes para la receta {codReceta}.")
        print(f"Error: Ingredientes insuficientes para la receta {codReceta}.")
        return 0
    except Exception as e:
        registrarExcepcion(e, "Error inesperado en calcularStock.")
        print("Error inesperado en calcularStock.")
        return 0
    
    ingredientesLocal = deepcopy(ingredientes)
    
    restarAuxIngredientes(codReceta, recetas, ingredientesLocal)
    
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
    
    compras[:] = [compra for compra in compras if compra["id"] not in {c["id"] for c in agregadas}]

    guardarDatos(cnf.rutas["ingredientes"], ingredientes)
    guardarDatos(cnf.rutas["compras"], compras)

def totalCuenta(pedido):
    precios = {plato[1].lower(): plato[2] for plato in cnf.menu}
    total = reduce(lambda subtotal, platoPedido: subtotal + precios[platoPedido[0].lower()] * platoPedido[1], pedido["platos"], 0)
    return total

def cargarDatosBasicos():
    return cnf.menu, cnf.recetas, cnf.ingredientes, cnf.pedidos

def inicializarPedido(nombre, mesa):
    return {
        "nombre": nombre,
        "mesa": mesa,
        "estado": "recibido",
        "platos": []
    }

def seleccionarPlato(menu):
    while True:
        try:
            plato = intInput(">> Ingrese número de plato o 0 para terminar:\n<< ")
            if plato in range(1, len(menu) + 1) or plato == 0:
                return plato
            else:
                raise ValueError
        except ValueError:
            print(">> Opción no válida. Ingrese un número válido.")

def agregarAlPedido(pedido, nombrePlato, cantidad, codPlato):
    """Agrega un plato al pedido o actualiza la cantidad si ya existe."""
    for elemento in pedido["platos"]:
        if elemento[0].lower() == nombrePlato:
            elemento[1] += cantidad
            return
    pedido["platos"].append([nombrePlato, cantidad, codPlato])

def procesarPlato(menu, recetas, ingredientes, pedido, platoSeleccionado):
    #Procesa la selección de un plato, incluyendo cantidad y actualización de stock.
    platoInfo = menu[platoSeleccionado - 1]
    nombrePlato, codPlato, stockDisponible = platoInfo[1].lower(), platoInfo[0], platoInfo[4]

    if stockDisponible < 1:
        print(f">> No hay stock disponible para {nombrePlato}.\n")
        return

    while True:
        try:
            cantidad = intInput(f">> Ingrese cantidad (disponible: {stockDisponible}):\n<< ")
            if cantidad < 1 or cantidad > stockDisponible:
                raise ValueError
            agregarAlPedido(pedido, nombrePlato, cantidad, codPlato)
            restarStock(codPlato, recetas, ingredientes, cantidad)
            actualizarStock(menu, recetas, ingredientes)
            print(f">> Has agregado {cantidad} de {nombrePlato} a tu pedido.\n")
            break
        except ValueError:
            print(">> Cantidad no válida. Intente nuevamente.")

def eliminarPedido(pedido, recetas, ingredientes, menu):
    #Cancela un pedido, devolviendo los ingredientes al stock.
    for plato in pedido["platos"]:
        codPlato, cantidad = plato[2], plato[1]
        devolverStock(codPlato, recetas, ingredientes, cantidad)
    actualizarStock(menu, recetas, ingredientes)

def terminarPedido(pedido, pedidos, recetas, ingredientes, menu, nombre, mesa):
    #Finaliza y confirma el pedido, actualizando los datos si es necesario.
    print(resumenPedido(nombre, mesa, pedido))
    confirmacion = confirmInput(">> Confirmar pedido (s=si, n=no):\n<< ")

    if confirmacion == 's':
        pedidos.append(pedido)
        guardarDatos(cnf.rutas['pedidos'], pedidos)
        print(f">> Gracias {nombre}! Tu pedido fue confirmado.")
    else:
        eliminarPedido(pedido, recetas, ingredientes, menu)
        print(">> Pedido cancelado.")

def hacerPedido(nombre, mesa):
    #Función principal para gestionar un pedido.
    menu, recetas, ingredientes, pedidos = cargarDatosBasicos()
    pedido = inicializarPedido(nombre, mesa)

    actualizarStock(menu, recetas, ingredientes)  # Asegurar que el stock esté actualizado al inicio
    print(impresionStockMenu(cnf.menu))  # Mostrar el menú

    while True:
        platoSeleccionado = seleccionarPlato(menu)
        if platoSeleccionado == 0:  # Finalizar pedido
            break

        procesarPlato(menu, recetas, ingredientes, pedido, platoSeleccionado)

    if len(pedido["platos"]) > 0:
        terminarPedido(pedido, pedidos, recetas, ingredientes, menu, nombre, mesa)
    else:
        print(">> No se agregaron platos al pedido.")

        
def verPedido(nombre, mesa, pedidos):
    pedidosCliente = [pedido for pedido in pedidos if pedido['nombre'].lower() == nombre.lower() and pedido['mesa'] == mesa]
    menu, recetas, ingredientes, pedidos = cargarDatosBasicos()
    actualizarStock(menu, recetas, ingredientes)
    for pedido in impresionPedidos(pedidosCliente):
        print(pedido)
    if len(pedidosCliente) > 0:
        confirma = confirmInput(">> Desea cancelar algun pedido? s/n\n<< ")
        if confirma == 's' and len(pedidosCliente) >1:
            cancelado = intInput(f">> Qué número de pedido desea cancelar? entre 1 y {len(pedidosCliente)}\n<< ")
            while cancelado not in range(1, len(pedidosCliente)+1):
                cancelado = intInput(f">> Debe seleccionar un número entre 1 y {len(pedidosCliente)}\n<< ")
            pedidos.remove(pedidosCliente[cancelado-1])
            guardarDatos(cnf.rutas["pedidos"], pedidos)
            print(">> Pedido eliminado exitosamente.")
            for elemento in pedidosCliente:
                eliminarPedido(elemento,recetas,ingredientes,menu)
        elif confirma == 's':
            pedidos.remove(pedidosCliente[0])
            eliminarPedido(pedidosCliente[0],recetas,ingredientes,menu)
            guardarDatos(cnf.rutas['pedidos'], pedidos)
            print(">> Pedido eliminado exitosamente.")
            #input(">> Enter para continuar\n<< ")   
    else:
        print(">> No se encontraron pedidos activos")

def avanzarPedidoCocina(pedidos, ruta_pedidos):
    comandas = [pedido for pedido in pedidos if (pedido["estado"].lower()) in cnf.permisosEstadosCocina]
    if len(comandas) == 0:
        print(">> No hay comandas activas en este momento.")
        return
    for pedido in impresionPedidos(comandas):
        print(pedido)
    avanzar = intInput(f">> Qué pedido desea avanzar? entre 1 y {len(comandas)} o 0 para cancelar.\n<< ")
    while avanzar not in range(0, len(comandas)+1):
        avanzar = intInput(f">> Debe seleccionar un número entre 1 y {len(comandas)} o 0 para cancelar.\n<< ")
    if avanzar == 0:
        return
    seleccionado = comandas[avanzar-1]
    actual = seleccionado["estado"]
    for avance in cnf.avanceEstados:
        if actual in avance:
            seleccionado["estado"] = avance[actual]
            print(f">> El pedido de {seleccionado['nombre']} en la mesa {seleccionado['mesa']} ahora está {seleccionado['estado'].capitalize()}.")
            guardarDatos(ruta_pedidos, pedidos)
            break

def avanzarPedidoSalon(pedidos, ruta_pedidos):
    comandas = [pedido for pedido in pedidos if (pedido["estado"].lower()) in cnf.permisosEstadosSalon]
    if len(comandas) == 0:
        print(">> No hay comandas activas en este momento.")
        return
    for pedido in impresionPedidos(comandas):
        print(pedido)
    avanzar = intInput(f"Qué pedido desea avanzar? entre 1 y {len(comandas)}. 0 para cancelar\n>>")
    while avanzar not in range(0, len(comandas)+1):
        avanzar = intInput(f">> Debe seleccionar un número entre 1 y {len(comandas)} o 0 para cancelar.\n<< ")
    if avanzar == 0:
        return
    seleccionado = comandas[avanzar-1]
    actual = seleccionado["estado"]
    for avance in cnf.avanceEstados:
        if actual in avance:
            seleccionado["estado"] = avance[actual]
            print(f"El pedido de {seleccionado['nombre']} en la mesa {seleccionado['mesa']} ahora está {seleccionado['estado'].capitalize()}.")
            if seleccionado['estado'].lower() == "finalizado":
                cnf.mesas[int(seleccionado["mesa"])-1]['estado']= "Libre"
                cnf.mesas[int(seleccionado["mesa"])-1]['cliente']= "Sin reserva"
                guardarDatos(cnf.rutas["mesas"], cnf.mesas)
                finalizados = cnf.finalizados
                finalizados.append(seleccionado)
                guardarDatos(cnf.rutas["finalizados"], finalizados)
                pedidos.remove(seleccionado)
            guardarDatos(ruta_pedidos, pedidos)
            break

def consultarReceta(recetas):
    impresionRecetas(recetas)
    consulta = codeInput("Ingrese el código de la receta a consultar:\n>>")
    #Verificar que el codigo exista
    while not verifCodigo(recetas, consulta):
        consulta = codeInput("Código no válido. Ingrese un código existente.\n>>")
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
    print(impresionMesas(cnf.mesas))
    seleccionada = intInput(">>Ingrese numero de mesa a cerrar o 0 para salir\n<<")
    while seleccionada not in range(0, len(cnf.mesas)+1):
        seleccionada = intInput(f">>Debe seleccionar una mesa entre 1 y {len(cnf.mesas)}, o 0 para salir.\n<<")
    if seleccionada == 0:
        return
    else:
        mesa = next((m for m in cnf.mesas if m["idMesa"] == int(seleccionada)), None)
        if mesa:
            mesa["estado"] = "Libre"
            mesa["cliente"] = "Sin reserva"
            print(f"La mesa {mesa['idMesa']} ha sido cerrada exitosamente.")
            guardarDatos(cnf.rutas["mesas"], cnf.mesas)
        else:
            msg='Error al modificar mesa\n\tFuncion() = cerrarMesa()/mesa=NONE'
            print('>> Error al modificar mesa')
            registrarExcepcion(ValueError,msg)

def ingresoAdmin():
    passwords = list(map(lambda item: list(item.keys())[0], cnf.admins))
    ingreso = charInput("Ingrese su contraseña:\n>>")
    if ingreso in passwords:
        adminDict = next(item for item in cnf.admins if list(item.keys())[0] == ingreso)
        user = list(adminDict.values())[0]
        administrarPedidos(cnf.pedidos)
    else:
        print("Contraseña incorrecta. Intente nuevamente.")

def cambiarEstados(pedidos):
    estadosDisponibles = cnf.estadosPedidos
    for pedido in impresionPedidos(pedidos):
        print(pedido)
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
    for pedido in impresionPedidos(pedidos):
        print(pedido)
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
        for pedido in impresionPedidos(pedidos):
            print(pedido)
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
    for pedido in impresionPedidos(pedidos):
        print(pedido)
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

def ingresarCompras(compras, ingredientes):
    impresionCompras(compras)
    ingreso = confirmInput("Desea ingresar estos ingredientes al stock? s/n\n>>")
    if ingreso == 's':
        actualizarIngredientes(ingredientes, compras)
        print("Ingredientes actualizados.")
    else:
        return

def administrarPedidos(pedidos):


    while True:

        accion = intInput(f"{cnf.adminUI}")
        while accion not in [1, 2, 3, 4, 5, 6, 7]:
            accion = intInput("Debe seleccionar una acción válida (1 a 7):\n>>")
        
        if accion == 1:  # Cambiar estado
            if len(pedidos) != 0:
                cambiarEstados(pedidos)
            else:
                input(">> No hay pedidos activos en el momento!\n>> Enter para continuar")
        elif accion == 2:  # Finalizar pedido
            if len(pedidos) != 0:
                finalizarPedido(pedidos)
            else:
                input(">> No hay pedidos activos en el momento!\n>> Enter para continuar")
        elif accion == 3:  # Cancelar pedido
            if len(pedidos) != 0:
                cancelarPedido(pedidos)
            else:
                input(">> No hay pedidos activos en el momento!\n>> Enter para continuar")
        elif accion == 4: #Repriorizar pedidos
            if len(pedidos) != 0:
                repriorizarPedidos(pedidos)
            else:
                input(">> No hay pedidos activos en el momento!\n>> Enter para continuar")
        elif accion == 5: #Cambiar pedidos de ingredientes
            modificarCompras(cnf.compras)
        
        elif accion == 6: #Ingresar compras
            ingresarCompras(cnf.compras, cnf.ingredientes)
        else: #Salir
            return
        
        # Guardar cambios
        guardarDatos(cnf.rutas["pedidos"], pedidos)

def reservarMesa(idMesa, cliente, ruta = "tp-algoritmos\\src\\datos\\mesas.json"):
    try:
        # Buscar la mesa en la lista
        mesa = next(m for m in cnf.mesas if m['idMesa'] == idMesa)

        # Verificar el estado de la mesa
        if mesa['estado'].lower() != 'libre':
            raise MesaOcupada(idMesa, mesa['cliente'])

        # Reservar la mesa
        mesa['estado'] = 'Ocupada'
        mesa['cliente'] = cliente
        cnf.guardarDatos(ruta, cnf.mesas)

    except StopIteration as e:
        registrarExcepcion(e, f"No se encontró la mesa con ID {idMesa} en la lista.")
        raise  # Relanza la excepción para manejarla en niveles superiores.

    except KeyError as e:
        registrarExcepcion(e, f"La mesa con ID {idMesa} no tiene una clave requerida.")
        raise

    except MesaOcupada as e:
        registrarExcepcion(e, f"Intento de reservar mesa ocupada: {idMesa}. Cliente actual: {e.clienteActual}.")
        raise

    except Exception as e:
        registrarExcepcion(e, f"Error inesperado al intentar reservar la mesa {idMesa}.")
        raise

def gestionarReserva():
    """
    Maneja la lógica de reserva de mesas para un cliente.
    Reintenta el flujo en caso de errores específicos.
    """
    # Solicitar el nombre del cliente
    nombre = charInput(">> Bienvenido al restaurante, Por favor ingrese su nombre:\n<< ")
    
    while True:
        try:
            # Solicitar el número de mesa y validar el rango
            numMesa = intInput(">> Ingrese el número de mesa:\n<< ")
            while numMesa not in range(1, len(cnf.mesas) + 1):
                numMesa = intInput(f"Debe ingresar una mesa entre 1 y {len(cnf.mesas)}.\n>>")

            # Intentar reservar la mesa
            reservarMesa(numMesa, nombre.capitalize())

            # Confirmar reserva exitosa
            print(f">> La mesa {numMesa} ha sido reservada exitosamente para {nombre.capitalize()}.")
            return nombre.capitalize(), numMesa  # Retorna el cliente y su mesa

        except MesaOcupada as e:
            registrarExcepcion(e, f"Intento de reservar una mesa ocupada: Mesa {e.idMesa}.")
            print(e)
            print("Por favor, seleccione otra mesa.")

        except StopIteration as e:
            registrarExcepcion(e, "Error: La mesa no existe en la lista.")
            print("Error: No se encontró la mesa especificada. Por favor, intente nuevamente.")

        except KeyError as e:
            registrarExcepcion(e, "Error en la estructura de datos de la mesa.")
            print("Error: Problema con los datos de la mesa. Por favor, contacte al administrador.")

        except Exception as e:
            registrarExcepcion(e, "Error inesperado al gestionar la reserva de cliente.")
            print("Error inesperado. Por favor, intente nuevamente.")


"""def mostrarMenuCliente(nombre, numMesa):
    while True:
        opcion = intInput(cnf.clienteUI)
        while opcion not in [1, 2, 3, 4]:
            print("Opción inválida. Ingrese 1, 2, 3 o 4.\n")
            opcion = intInput(cnf.clienteUI)

        if opcion == 1:
            print(impresionMenu(cnf.menu))
            input('>> Enter para continuar\n<< ')

        elif opcion == 2:
            hacerPedido(nombre, numMesa)
            input(">> Enter para continuar\n<< ")

        elif opcion == 3:
            verPedido(nombre, numMesa)

        else:
            print(f">> Gracias, {nombre}!")
            input(">> Enter para continuar\n<< ")
            return"""

def mostrarMenuCliente():
    #Muestra el menú interactivo para el cliente y devuelve una opción válida seleccionada.
    while True:
        try:
            opcion = intInput(cnf.clienteUI)
            if opcion in [1, 2, 3, 4]:  # Verifica que la opción esté en el rango permitido
                return opcion
            print("Opción inválida. Ingrese un número entre 1 y 4.\n")
        except Exception as e:
            registrarExcepcion(e, "Error al capturar la opción del menú del cliente.")
            print("Error inesperado. Por favor, intente nuevamente.")
            raise

def ejecutarOpcionCliente(opcion, nombre, numMesa):
    #Ejecuta la opción seleccionada en el menú del cliente.
    try:
        if opcion == 1:
            print(impresionMenu(cnf.menu))
            input('>> Enter para continuar\n<< ')

        elif opcion == 2:
            hacerPedido(nombre, numMesa)
            input(">> Enter para continuar\n<< ")

        elif opcion == 3:
            verPedido(nombre, numMesa, cnf.pedidos)
            input(">> Enter para continuar\n<< ")

        elif opcion == 4:
            print(f">> Gracias, {nombre}.")
            return False  # Indica que el bucle principal debe terminar

    except Exception as e:
        registrarExcepcion(e, f"Error al ejecutar la opción {opcion} en el menú del cliente.")
        print("Error inesperado al procesar la opción. Por favor, intente nuevamente.")
    return True  # Continuar en el menú principal

def mostrarMenuCocina():
    #Muestra el menú interactivo para la cocina y devuelve una opción válida seleccionada.
    while True:
        try:
            opcion = intInput(cnf.cocinaUI)
            if opcion in range(1, 8):  # Verifica que la opción esté en el rango permitido
                return opcion
            print("Opción inválida. Ingrese un número entre 1 y 7.\n")
        except Exception as e:
            registrarExcepcion(e, "Error al capturar la opción del menú de cocina.")
            print("Error inesperado. Por favor, intente nuevamente.")
            raise

def ejecutarOpcionCocina(opcion):
    #Ejecuta la opción seleccionada en el menú de cocina.
    try:
        if opcion == 1:
            for pedido in impresionPedidos(cnf.pedidos):
                print(pedido)
            input("\nPresione Enter para continuar>>")

        elif opcion == 2:
            avanzarPedidoCocina(cnf.pedidos, cnf.rutas["pedidos"])
            input("\nPresione Enter para continuar>>")

        elif opcion == 3:
            consultarReceta(cnf.recetas)
            input("\nPresione Enter para continuar>>")

        elif opcion == 4:
            impresionIngredientes(cnf.ingredientes)
            input("\nPresione Enter para continuar>>")

        elif opcion == 5:
            pedirIngredientes(cnf.ingredientes, cnf.compras)
            input("\nPresione Enter para continuar>>")

        elif opcion == 6:
            impresionCompras(cnf.compras)
            input("\nPresione Enter para continuar>>")

        elif opcion == 7:
            print(">> Cerrando módulo de cocina.")
            return False  # Indica que el bucle principal debe terminar

    except Exception as e:
        registrarExcepcion(e, f"Error al ejecutar la opción {opcion} en el menú de cocina.")
        print("Error inesperado al procesar la opción. Por favor, intente nuevamente.")
    return True  # Continuar en el menú principal

def mostrarMenuSalon():
    #Muestra el menú interactivo para el salón y devuelve una opción válida seleccionada.
    while True:
        try:
            opcion = intInput(cnf.salonUI)
            if opcion in [1, 2, 3, 4, 5, 6]:  # Verifica que la opción esté en el rango permitido
                return opcion
            print(">> Opción inválida. Ingrese un número entre 1 y 6.\n")
        except Exception as e:
            registrarExcepcion(e, "Error al capturar la opción del menú del salón.")
            print("Error inesperado. Por favor, intente nuevamente.")
            raise

def ejecutarOpcionSalon(opcion):
    #Ejecuta la opción seleccionada en el menú del salón.
    try:
        if opcion == 1:
            print(impresionMesas(cnf.mesas))
            input("\nPresione Enter para continuar>>")

        elif opcion == 2:
            if len(cnf.pedidos)>0: 
                for pedido in impresionPedidos(cnf.pedidos):
                    print(pedido)
            else:
                print(">> No hay pedidos.")
            input("\nPresione Enter para continuar>>")

        elif opcion == 3:
            avanzarPedidoSalon(cnf.pedidos, cnf.rutas["pedidos"])
            input("\nPresione Enter para continuar>>")

        elif opcion == 4:
            cerrarMesa()
            input("\nPresione Enter para continuar>>")

        elif opcion == 5:
            ingresoAdmin()
            input("\nPresione Enter para continuar>>")

        elif opcion == 6:
            print(">> Cerrando módulo de salón.")
            return False  # Indica que el bucle principal debe terminar

    except Exception as e:
        registrarExcepcion(e, f"Error al ejecutar la opción {opcion} en el menú del salón.")
        print("Error inesperado al procesar la opción. Por favor, intente nuevamente.")
    return True  # Continuar en el menú principal
