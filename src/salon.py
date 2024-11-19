import config as cnf
import funciones as fn

while True:
    opcion = fn.intInput(cnf.salonUI)
    while opcion not in [1, 2, 3, 4, 5]:
        print("Opción inválida. Ingrese 1, 2, 3, 4 o 5.\n")
        opcion = fn.intInput(cnf.salonUI)

    if opcion == 1:
        fn.impresionMesas()
        input("\nPresione Enter para continuar>>")
            
    elif opcion == 2:
        fn.impresionPedidos(cnf.pedidos)
        input("\nPresione Enter para continuar>>")
    
    elif opcion == 3:
        fn.avanzarPedidoSalon()
        input("\nPresione Enter para continuar>>")
            
    elif opcion == 4:
        fn.cerrarMesa()
        input("\nPresione Enter para continuar>>")
    
    else:
        fn.ingresoAdmin()
        