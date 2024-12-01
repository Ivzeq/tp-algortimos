from funciones import mostrarMenuCocina, ejecutarOpcionCocina

def cocina():
    """
    Controla el flujo completo del módulo de cocina.
    """
    print(">> Bienvenido al módulo de cocina.")
    continuar = True
    while continuar:
        opcion = mostrarMenuCocina()
        continuar = ejecutarOpcionCocina(opcion)

#cocina()
        