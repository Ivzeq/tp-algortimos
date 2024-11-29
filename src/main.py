import config as cnf
import funciones as fn
import cliente
import cocina
import salon

def main():
    while True:
        opcion = fn.intInput(cnf.inicioUI)
        while opcion not in [1, 2, 3]:
            print(">> Opción inválida. Ingrese 1, 2 o 3.")
            opcion = fn.intInput(cnf.inicioUI)

        if opcion == 1:
            cliente.cliente()
                
        elif opcion == 2:
            cocina.cocina()
        
        elif opcion == 3:
            salon.salon()
            
main()