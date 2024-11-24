import json
import funciones as fn


def cargarDatos(ruta):
    try:    
        with open(ruta, encoding = 'utf-8') as archivo:
            return json.load(archivo)
    except Exception as e:
        #si ocurre un error deberiamos acceder mediante librerias so para verificar si existe y sino, debemos crear un archivo
        msg=(f'Error al abrir archivo con ruta precargada\n\tContexto:CargarDatos(ruta)')
        fn.registrarExcepcion(e,msg)
        
def cargarUI(ruta):    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as e:
        msg=(f'Error al abrir archivo con ruta precargada\n\tContexto:CargarUI(ruta)')
        fn.registrarExcepcion(e,msg)
def guardarDatos(ruta, datos):
    try:    
        with open(ruta, 'w', encoding= 'utf-8') as archivo:
            json.dump(datos, archivo, indent=4)
    except Exception as e:
        msg=(f'Error al abrir archivo con ruta precargada\n\tContexto:guardarDatos(ruta,datos)')
        fn.registrarExcepcion(e,msg)
estadosPedidos = ("recibido", "en preparación", "listo","entregado", "pagado", "finalizado")

avanceEstados = [
    {"recibido": "en preparación"},
    {"en preparación": "listo"},
    {"listo": "entregado"},
    {"entregado": "pagado"},
    {"pagado": "finalizado"}
]

permisosEstadosCocina = ("recibido", "en preparación", "listo")
permisosEstadosSalon = ("entregado", "pagado")
admins = ({"admin": "ale"}, {"osyubdf": "michael"}, {"hsocne": "ivan"})

rutas = {
    "ingredientes": "tp-algoritmos\\src\\datos\\ingredientes.json",
    "menu": "tp-algoritmos\\src\\datos\\menu.json",
    "mesas": "tp-algoritmos\\src\\datos\\mesas.json",
    "pedidos": "tp-algoritmos\\src\\datos\\pedidos.json",
    "recetas": "tp-algoritmos\\src\\datos\\recetas.json",
    "compras": "tp-algoritmos\src\datos\compras.json",
    "finalizados": "tp-algoritmos\\src\\datos\\finalizados.json",
    "log": "tp-algoritmos\\src\\datos\\restaurant.log",
    "estados": "tp-algoritmos\\src\\UI\\estadosPedidos.txt",
    "admin": "tp-algoritmos\\src\\UI\\menuAdministrador.txt",
    "cocina": "tp-algoritmos\\src\\UI\\menuCocinero.txt",
    "cliente": "tp-algoritmos\\src\\UI\\menuCliente.txt",
    "salon": "tp-algoritmos\\src\\UI\\menuSalon.txt",
    "inicio": "tp-algoritmos\\src\\UI\\menuInicio.txt"
}

ingredientes = cargarDatos(rutas["ingredientes"])
menu = cargarDatos(rutas["menu"])
mesas = cargarDatos(rutas["mesas"])
pedidos = cargarDatos(rutas["pedidos"])
recetas = cargarDatos(rutas["recetas"])
compras = cargarDatos(rutas["compras"])
finalizados = cargarDatos(rutas["finalizados"])
estadosPedidosUI = cargarUI(rutas["estados"])
adminUI = cargarUI(rutas["admin"])
cocinaUI = cargarUI(rutas["cocina"])
clienteUI = cargarUI(rutas["cliente"])
salonUI = cargarUI(rutas["salon"])
inicioUI = cargarUI(rutas["inicio"])
