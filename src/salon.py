import config as cnf
import funciones as fn

def salon():
    while True:
        opcion = fn.intInput(cnf.salonUI)
        while opcion not in [1, 2, 3, 4, 5, 6]:
            print(">> Opción inválida. Ingrese entre 1 y 6.")
            opcion = fn.intInput(cnf.salonUI)

        if opcion == 1:
            print(fn.impresionMesas())
            input("\nPresione Enter para continuar>>")
                
        elif opcion == 2:
            for pedido in fn.impresionPedidos(cnf.pedidos):
                print(pedido)
            input("\nPresione Enter para continuar>>")
        
        elif opcion == 3:
            fn.avanzarPedidoSalon()
            input("\nPresione Enter para continuar>>")
                
        elif opcion == 4:
            fn.cerrarMesa()
            input("\nPresione Enter para continuar>>")
        
        elif opcion == 5:
            fn.ingresoAdmin()
        else:
            return

salon() 