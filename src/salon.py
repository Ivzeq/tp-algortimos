import config as cnf
import funciones as fn

def salon():
    while True:
        fn.limp()
        opcion = fn.intInput(cnf.salonUI)
        while opcion not in [1, 2, 3, 4, 5, 6]:
            fn.limp()
            print(">> Opción inválida. Ingrese entre 1 y 6.")
            opcion = fn.intInput(cnf.salonUI)

        if opcion == 1:
            fn.limp()
            fn.impresionMesas()
            input("\nPresione Enter para continuar>>")
                
        elif opcion == 2:
            fn.limp()
            fn.impresionPedidos(cnf.pedidos)
            input("\nPresione Enter para continuar>>")
        
        elif opcion == 3:
            fn.limp()
            fn.avanzarPedidoSalon()
            input("\nPresione Enter para continuar>>")
                
        elif opcion == 4:
            fn.limp()
            fn.cerrarMesa()
            input("\nPresione Enter para continuar>>")
        
        elif opcion == 5:
            fn.limp()
            fn.ingresoAdmin()
        else:
            return

#salon() 