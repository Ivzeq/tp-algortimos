import config as cnf
import funciones as fn

nombre = fn.charInput("\n\n\n\nBienvenido al restaurant. Por favor indique su nombre:\n>>")
numMesa = fn.intInput("Ingrese el número de mesa:\n>>")

while numMesa not in range (1, len(cnf.mesas)+1):
    numMesa = fn.intInput(f"Debe ingresar una mesa enrte 1 y {len(cnf.mesas)}.\n>>")

for mesa in cnf.mesas:
        if mesa["idMesa"] == str(numMesa):
            # Actualizar el estado y el cliente de la mesa
            mesa["estado"] = "Ocupada"
            mesa["cliente"] = nombre.capitalize()
            break
        cnf.guardarDatos(cnf.rutas["mesas"], cnf.mesas)

while True:
    opcion = fn.intInput(cnf.clienteUI)
    while opcion not in [1, 2, 3]:
        print("Opción inválida. Ingrese 1, 2 o 3.\n")
        opcion = fn.intInput(cnf.clienteUI)

    if opcion == 1:
        fn.impresionMenu()
            
    elif opcion == 2:
        fn.hacerPedido(nombre, numMesa)
        input("\nPresione Enter para continuar>>")
            
    else:
        fn.verPedido(nombre, numMesa)
        input("\nPresione Enter para continuar>>")
        