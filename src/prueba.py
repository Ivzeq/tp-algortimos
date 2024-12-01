import funciones as fn
import config as cnf

"""pedidos = cnf.pedidos

print(type(fn.impresionPedidos(pedidos)))

print(fn.impresionPedidos(pedidos))

for pedido in fn.impresionPedidos(pedidos):
    print(pedido)"""

print(fn.calcularStock("AST", cnf.recetas, cnf.ingredientes, limite=60, profundidad=0))