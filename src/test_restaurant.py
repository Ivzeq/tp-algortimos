from funciones import *
from config import *
import json

pedidos =[
    {
        "nombre": "Michael",
        "mesa": 1,
        "estado": "en preparación",
        "platos": [
            [
                "milanesa de ternera",
                3,
                "MLT"
            ],
            [
                "ensalada Caesar",
                2,
                "ECA"
            ]
        ]
    },
    {
        "nombre": "Ale",
        "mesa": 2,
        "estado": "entregado",
        "platos": [
            [
                "asado de tira",
                1,
                "AST"
            ],
            [
                "ensalada caprese",
                2,
                "ECP"
            ]
        ]
    }
]
recetas = [
    {"id": 1, "ingredientes": [{"harina": 2}, {"azúcar": 1}, {"huevos": 2}]},
    {"id": 2, "ingredientes": [{"tomate": 5}, {"ajo": 2}]},
    {"id": 3, "ingredientes": []},  # Receta sin ingredientes
]

ingredientes = [
        {'id': 1, 'nombre': 'Tomate', 'cantidad': 10},
        {'id': 2,'nombre': 'Lechuga', 'cantidad': 0},
        {'id': 3,'nombre': 'Cebolla', 'cantidad': 5},
        {'id': 1,'nombre': 'Tomate', 'cantidad': 3},
        {'id': 5,'nombre': 'Ajo', 'cantidad': 8},
    ]
def test_conjuntoIngredientes():
    resultado = conjuntoIngredientes(ingredientes)
    esperado = {'tomate', 'cebolla', 'ajo'}
    assert resultado == esperado, f"Se esperaba {esperado}, pero se obtuvo {resultado}"

def test_conjuntoIngrReceta_casoValido():
    resultado = conjuntoIngrReceta(1, recetas)
    esperado = {"harina", "azúcar", "huevos"}
    assert resultado == esperado, f"Esperado {esperado}, obtenido {resultado}"

def test_conjuntoIngrReceta_sinIngredientes():
    resultado = conjuntoIngrReceta(3, recetas)
    esperado = set()
    assert resultado == esperado, f"Esperado {esperado}, obtenido {resultado}"

def test_conjuntoIngrReceta_formatoIncorrecto():
    recetas_mal_formateadas = [
        {"codigo": 1, "ingredientes": [{"harina": 2}]},
    ]
    resultado = conjuntoIngrReceta(1, recetas_mal_formateadas)
    esperado = set()
    assert resultado == esperado, f"Esperado {esperado}, obtenido {resultado}"

def test_cargaPedidos():
    cargarDatos(rutas["pedidos"])
    with open(rutas["pedidos"],'r') as archivo:
        contenido=archivo.read()
        assert pedidos==json.loads(contenido)

def test_cerrarMesa():
    cerrarMesa()
    
test_cerrarMesa()