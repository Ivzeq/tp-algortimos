import json
import funciones as fn
import os

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
        
estadosPedidos = ("recibido", "en preparacion", "listo","entregado", "pagado", "finalizado")
avanceEstados = [
    {"recibido": "en preparacion"},
    {"en preparacion": "listo"},
    {"listo": "entregado"},
    {"entregado": "pagado"},
    {"pagado": "finalizado"}
]

permisosEstadosCocina = ("recibido", "en preparacion", "listo")
permisosEstadosSalon = ("entregado", "pagado")
admins = ({"admin": "ale"}, {"osyubdf": "michael"}, {"hsocne": "ivan"})

direccion_UI=os.path.join(os.path.dirname(os.path.abspath(__file__)),'UI')
direccion_datos=os.path.join(os.path.dirname(os.path.abspath(__file__)),'datos')

rutas = {
    "ingredientes": os.path.join(direccion_datos,'ingredientes.json'),
    "menu": os.path.join(direccion_datos,"menu.json"),
    "mesas": os.path.join(direccion_datos,'mesas.json'),
    "pedidos": os.path.join(direccion_datos,'pedidos.json'),
    "recetas": os.path.join(direccion_datos,'recetas.json'),
    "compras": os.path.join(direccion_datos,'compras.json'),
    "finalizados": os.path.join(direccion_datos,'finalizados.json'),
    "log": os.path.join(direccion_datos,'restaurant.log'),
    "estados": os.path.join(direccion_UI,'estadosPedidos.txt'),
    "admin": os.path.join(direccion_UI,'menuAdministrador.txt'),
    "cocina": os.path.join(direccion_UI,'menuCocinero.txt'),
    "cliente": os.path.join(direccion_UI,'menuCliente.txt'),
    "salon": os.path.join(direccion_UI,'menuSalon.txt'),
    "inicio": os.path.join(direccion_UI,'menuInicio.txt')


}

ingredientes = cargarDatos(rutas["ingredientes"])
menu = cargarDatos(rutas["menu"])
mesas = cargarDatos(rutas["mesas"])
if mesas=='' or mesas is None:
    mesas=[
    {
        "idMesa": 1,
        "estado": "Libre",
        "cliente": "Sin reserva"
    },
    {
        "idMesa": 2,
        "estado": "Libre",
        "cliente": "Sin reserva"
    },
    {
        "idMesa": 3,
        "estado": "Libre",
        "cliente": "Sin reserva"
    },
    {
        "idMesa": 4,
        "estado": "Libre",
        "cliente": "Sin reserva"
    },
    {
        "idMesa": 5,
        "estado": "Libre",
        "cliente": "Sin reserva"
    },
    {
        "idMesa": 6,
        "estado": "libre",
        "cliente": "sin reserva"
    }
]
    fn.guardarDatos(rutas["mesas"],mesas)
pedidos = cargarDatos(rutas["pedidos"])
if pedidos=='' or pedidos is None:
    pedidos=[]
    fn.guardarDatos(rutas["pedidos"],pedidos)
recetas = cargarDatos(rutas["recetas"])
compras = cargarDatos(rutas["compras"])
finalizados = cargarDatos(rutas["finalizados"])
estadosPedidosUI = cargarUI(rutas["estados"])
adminUI = cargarUI(rutas["admin"])
cocinaUI = cargarUI(rutas["cocina"])
clienteUI = cargarUI(rutas["cliente"])
salonUI = cargarUI(rutas["salon"])
inicioUI = cargarUI(rutas["inicio"])
