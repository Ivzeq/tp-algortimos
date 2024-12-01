from funciones import gestionarReserva, mostrarMenuCliente, ejecutarOpcionCliente, registrarExcepcion

def cliente():
    #Controla el flujo completo de interacción con el cliente.
    try:
        nombre, numMesa = gestionarReserva()  # Gestiona la reserva de la mesa

        continuar = True
        while continuar:
            opcion = mostrarMenuCliente()  # Captura la opción seleccionada
            continuar = ejecutarOpcionCliente(opcion, nombre, numMesa)  # Ejecuta la opción seleccionada
    except Exception as e:
        registrarExcepcion(e, "Error inesperado en el flujo del cliente.")
        print("Ocurrió un error inesperado. Por favor, intente nuevamente.")

#cliente()           