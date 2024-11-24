import config as cnf
import funciones as fn

def cocina():
    while True:
        opcion = fn.intInput(cnf.cocinaUI)
        while opcion not in [1, 2, 3, 4, 5, 6, 7]:
            print("Opción inválida. Ingrese entre 1 y 7.\n")
            opcion = fn.intInput(cnf.cocinaUI)

        if opcion == 1:
            fn.impresionPedidos(cnf.pedidos)
            input("\nPresione Enter para continuar>>")
                
        elif opcion == 2:
            fn.avanzarPedidoCocina()
            input("\nPresione Enter para continuar>>")
        
        elif opcion == 3:
            fn.consultarReceta()
            input("\nPresione Enter para continuar>>")
                
        elif opcion == 4:
            fn.impresionIngredientes(cnf.ingredientes)
            input("\nPresione Enter para continuar>>")
        
        elif opcion == 5:
            fn.pedirIngredientes(cnf.ingredientes, cnf.compras)
            input("\nPresione Enter para continuar>>")
        
        elif opcion == 6:
            fn.impresionCompras(cnf.compras)
            input("\nPresione Enter para continuar>>")
        
        else:
            return

#cocina()
        