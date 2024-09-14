possibleStatesList = ('ejecutando', 'finalizado')
state = 'ejecutando'

while(state != possibleStatesList[1]):
    # Inicializacion 
    print('El programa se inicializo')
    proximoStatus = input('Ingrese el proximo state: ')
   
    # Verificacion de state
    while proximoStatus not in possibleStatesList:
        print('El state ingresado no es valido. Ingrese uno de los siguientes posibles')
        for state in possibleStatesList:
            print(possibleStatesList.index(state), '-', state)
        proximoStatus = input('Ingrese el proximo state:')
    
    # Finalizacion
    if(state == possibleStatesList[1]):
        print('La ejecucion finalizo')