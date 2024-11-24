import config as cnf
import funciones as fn
import cliente
import cocina
import salon

def main():
    while True:
        fn.limp()
        opcion = fn.intInput(cnf.inicioUI)
        while opcion not in [1, 2, 3]:
            fn.limp()
            print(">> Opción inválida. Ingrese 1, 2 o 3.")
            opcion = fn.intInput(cnf.inicioUI)

        if opcion == 1:
            fn.limp()
            cliente.cliente()
            input("\n>> Presione Enter para continuar>>")
                
        elif opcion == 2:
            fn.limp()
            cocina.cocina()
            input("\n>> Presione Enter para continuar>>")
        
        elif opcion == 3:
            fn.limp()
            salon.salon()
            
main()