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
    "ingredientes": "tp-algoritmos-ale\\src\\datos\\ingredientes.json",
    "menu": "tp-algoritmos-ale\\src\\datos\\menu.json",
    "mesas": "tp-algoritmos-ale\\src\\datos\\mesas.json",
    "pedidos": "tp-algoritmos-ale\\src\\datos\\pedidos.json",
    "recetas": "tp-algoritmos-ale\\src\\datos\\recetas.json",
    "compras": "tp-algoritmos-ale\\src\\datos\\compras.json",
    "finalizados": "tp-algoritmos-ale\\src\\datos\\finalizados.json",
    "log": "tp-algoritmos-ale\\src\\datos\\restaurant.log",
    "estados": "tp-algoritmos-ale\\src\\UI\\estadosPedidos.txt",
    "admin": "tp-algoritmos-ale\\src\\UI\\menuAdministrador.txt",
    "cocina": "tp-algoritmos-ale\\src\\UI\\menuCocinero.txt",
    "cliente": "tp-algoritmos-ale\\src\\UI\\menuCliente.txt",
    "salon": "tp-algoritmos-ale\\src\\UI\\menuSalon.txt"
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