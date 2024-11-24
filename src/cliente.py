import config as cnf
import funciones as fn

def cliente():
    nombre = fn.charInput("\n\n\n\nBienvenido al restaurant. Por favor indique su nombre:\n>>")
    numMesa = fn.intInput("Ingrese el número de mesa:\n>>")

    while numMesa not in range (1, len(cnf.mesas)+1):
        numMesa = fn.intInput(f"Debe ingresar una mesa entre 1 y {len(cnf.mesas)}.\n>>")

    for mesa in cnf.mesas:
            print(numMesa, mesa)
            if mesa["idMesa"] == numMesa:
                # Actualizar el estado y el cliente de la mesa
                mesa["estado"] = "Ocupada"
                mesa["cliente"] = nombre.capitalize()
                break
    cnf.guardarDatos(cnf.rutas["mesas"], cnf.mesas)

    while True:
        opcion = fn.intInput(cnf.clienteUI)
        while opcion not in [1, 2, 3, 4]:
            print("Opción inválida. Ingrese 1, 2, 3 o 4.\n")
            opcion = fn.intInput(cnf.clienteUI)

        if opcion == 1:
            fn.impresionMenu()
                
        elif opcion == 2:
            fn.hacerPedido(nombre, numMesa)
            input("\nPresione Enter para continuar>>")
                
        elif opcion == 3:
            fn.verPedido(nombre, numMesa)
            input("\nPresione Enter para continuar>>")

        else:
            return

#cliente()           