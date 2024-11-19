import config as cnf
import funciones as fn

while True:
    opcion = fn.intInput(cnf.cocinaUI)
    while opcion not in [1, 2, 3, 4, 5, 6]:
        print("Opción inválida. Ingrese entre 1 y 6.\n")
        opcion = fn.intInput(cnf.salonUI)

    if opcion == 1:
        fn.impresionPedidos(cnf.pedidos)
        input("\nPresione Enter para continuar>>")
            
    elif opcion == 2:
        fn.avanzarPedidoCocina()
        input("\nPresione Enter para continuar>>")
    
    elif opcion == 3:
        fn.impresionRecetas
        input("\nPresione Enter para continuar>>")
            
    elif opcion == 4:
        fn.impresionIngredientes()
        input("\nPresione Enter para continuar>>")
    
    elif opcion == 5:
        fn.pedirIngredientes(cnf.ingredientes, cnf.compras)
        input("\nPresione Enter para continuar>>")
    
    else:
        fn.impresionCompras(cnf.compras)
        input("\nPresione Enter para continuar>>")
        