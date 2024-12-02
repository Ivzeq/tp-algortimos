import funciones as fn
import config as cnf

"""pedidos = cnf.pedidos

print(type(fn.impresionPedidos(pedidos)))

print(fn.impresionPedidos(pedidos))

for pedido in fn.impresionPedidos(pedidos):
    print(pedido)"""


print(fn.calcularStock("2001", cnf.recetas, cnf.ingredientes))
fn.restarStock("2001", cnf.recetas, cnf.ingredientes, 2)
fn.actualizarStock(cnf.menu, cnf.recetas, cnf.ingredientes)
print(fn.calcularStock("2001", cnf.recetas, cnf.ingredientes))