import config as cnf
import funciones as fn
import cliente
import cocina
import salon

def main():
    while True:
        opcion = fn.intInput(cnf.inicioUI)
        while opcion not in [1, 2, 3]:
            print("Opción inválida. Ingrese 1, 2 o 3.\n")
            opcion = fn.intInput(cnf.inicioUI)

        if opcion == 1:
            cliente.cliente()
            input("\nPresione Enter para continuar>>")
                
        elif opcion == 2:
            cocina.cocina()
            input("\nPresione Enter para continuar>>")
        
        elif opcion == 3:
            salon.salon()
            input("\nPresione Enter para continuar>>")
main()