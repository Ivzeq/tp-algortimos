import json

def cargarDatos(ruta):
    with open(ruta, encoding = 'utf-8') as archivo:
        return json.load(archivo)

def cargarUI(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def guardarDatos(ruta, datos):
    with open(ruta, 'w', encoding= 'utf-8') as archivo:
        json.dump(datos, archivo, indent=4)

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