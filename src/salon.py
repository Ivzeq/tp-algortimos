from funciones import mostrarMenuSalon, ejecutarOpcionSalon

def salon():
    #Controla el flujo completo del módulo de salón.
    print(">> Bienvenido al módulo de salón.")
    continuar = True
    while continuar:
        opcion = mostrarMenuSalon()  # Captura la opción seleccionada
        continuar = ejecutarOpcionSalon(opcion)  # Ejecuta la opción seleccionada

#salon() 