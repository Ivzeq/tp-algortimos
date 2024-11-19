from funciones import *
from config import *
import json


def test_config():
    with open(configPath,'r') as archivo:
        exec(archivo.read())
def test_guardadoPedidos():
    guardadoPedidos(pedidos)
    with open(pedidosPath,'r') as archivo:
        contenido=archivo.read()
        assert pedidos==json.loads(contenido)
def test_guardadoMesas():
    guardadoMesas(mesas)
    with open(mesasPath,'r') as archivo:
        contenido=archivo.read()
        assert mesas==json.loads(contenido)
def test_verificarType():
    assert verificarTipo('admin')==True
    assert verificarTipo('xx')==False
def test_returnPermisos():
    assert getPermisos('admin')==userTypes[0]['permisos']
def test_getMesas():
    assert getMesas('all')==mesas
    assert type(getMesas('1'))==list
    assert 1==len(getMesas('1'))
def test_cerrarOrden():
    cerrarOrden()
#PARA CUANDO UNA PRUEBA NECESItA UN INPUT DEBERIMAOS USAR MOCK PERO
#VAMOS A UTILIZAR UNA ETIQUETA Y LUEGO AL MOMENTO DE EJECUTAR LAS PRUBAS
#PONEMOS COMO CONDICION QUE EJECUTA SEGUN LA ETIQUETA
#CON MARCA pytest -s -m s_input SIN MARCA pytest -v -m "not s_input"
#MARCA=@pytest.mark.s_input

test_cerrarOrden()