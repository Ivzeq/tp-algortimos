#IMPORTS
import config
import funciones as fn
"""PROGRAMA"""
config.limp()
while(config.appState != config.possibleStatesTupla[-1]):
    # Inicializacion 
    while (config.loggedUserType == '' and config.appState == 'login'):
        try:
            tipoIngresado = input(config.ui[5])

            if fn.verificarNumero(tipoIngresado) == False:
                raise ValueError('El valor ingresado no es un numero,')

            if tipoIngresado=="1":
                tipoIngresado="cliente"
            elif tipoIngresado=="2":
                tipoIngresado="admin"
            elif tipoIngresado=="3":
                tipoIngresado="cocinero"
            elif tipoIngresado=="4":
                tipoIngresado="mesero"          

            if fn.verificarTipo(tipoIngresado)==False:
                raise ValueError('El usuario no existe,')
            
            config.limp()
            config.loggedUserType = tipoIngresado
        except ValueError as ms:
            config.limp()
            print(f'>> {ms} ingrese uno valido: ')
        except Exception as error_mssg:
            config.limp()
            print(f'Error : {error_mssg}')

    config.loggedUserPermissions = fn.getPermisos(config.loggedUserType)
    config.limp()
    config.appState=fn.impresionPermisos(tipoIngresado,config.appState)
    # Verificacion de state
    while (config.appState not in config.possibleStatesTupla) | (fn.verificarPermisos(config.appState,config.loggedUserPermissions) == False):
        config.limp()
        print('>>La opcion ingresada no es valida. Ingrese uno de los siguientes posibles')
        input(">>Enter para continuar")
        config.limp()
        config.appState=fn.impresionPermisos(tipoIngresado,config.appState)
    config.limp()
    # Manejo de funcionalidades en base al state
    # ---Funcionalidad verPerfiles
    # ------- Pendiente validacion de inpu
    if config.appState == 'verPerfiles':
        while True:
            config.limp()
            idPerfil = 'all'
            try:
                perfil = fn.getPerfiles(idPerfil)
                if perfil == None:
                    raise ValueError
            except ValueError as ms:
                print(f'>> El valor ingresado no es correcto, error -> {ms}')
                input('>>ENTER para continuar')
            except Exception as error_mssg:
                print(f'>> Ha ocurrido un error: {error_mssg}')
                input('>>ENTER para continuar')
            else:
                break
        fn.mostrarUserTypes(perfil)
        
    if config.appState=='cerrarOrden':
        fn.cerrarOrden()
        
            
        
    
    # ---Funcionalidad verMesas
    # ------- Pendiente validacion de input
    if config.appState=="recepcion":
        nombre=input(">> Ingrese nombre de cliente\n<< ")
        while True:
            try:
                cantidad_comensales=int(input(">> Ingrese la cantidad de comensales\n<< "))
            except KeyboardInterrupt:
                print(f'>> Fin..')
            except:
                print(f'>> Opcion no valida\n>> Ingrese una opcion valida')
                input('>> ENTER para continuar')
            else:
                break
        
        if fn.verificador_disponibilidad(cantidad_comensales,config.mesas):
            #entramos al if si solo la funcion verificador_disponibilidad devuelve true
            print(f">> Hay disponibilidad de mesas, la mesa es la numero: {config.id_mesa}")
            #modificamos el estado de la mesa buscandola por su id
            for elemento in config.mesas:
                if elemento["idMesa"]==config.id_mesa:
                    elemento["reserva"]=nombre
                    elemento["estado"]="ocupado"
                    elemento["cantPersonas"]=cantidad_comensales
                    fn.guardadoMesas(config.mesas)
        else:
            print(">> No hay disponibilidad de mesas")       
        input('ENTER para continuar')
    if config.appState == 'verMesas':       
        while True:
            try:
                idMesa = input('>>Ingrese el numero de la mesa o "all" para ver todas las mesas\n<< ').lower()
                mesa= fn.getMesas(idMesa)
                if mesa==None:
                    raise ValueError
            except ValueError:
                print('>> Valor ingresado incorrecto')
                input('>> Enter para continuar')
            except Exception as ms:
                print('>> Ha ocurrido un error -> {ms}')
                input('>> Enter para continuar')
            else:
                break
        fn.impresionMesas(mesa)
        input('>> Enter para continuar')
    if config.appState == 'operar':
        fn.cliente() 
    if config.appState == 'reservar':
        while True:
            try:
                nombre = input(">> Ingrese su nombre:\n<< ").capitalize()
                if nombre=='' or nombre.isspace():
                    raise ValueError
                if not(nombre.isalpha()):
                    raise ValueError
            except ValueError:
                print(f'>> Opcion ingresada no valida\n<< Ingrese una valida')    
            else:
                break
        while True:
            config.opcion=fn.excepcionNumeroEnteros(config.ui[7])
            while config.opcion<1 or config.opcion>3:
                config.opcion=fn.excepcionNumeroEnteros(config.ui[7])
            if config.opcion==1:
                config.limp()
                fn.reservar(nombre)
            elif config.opcion==2:
                config.limp()
                fn.verReservas(nombre)
                config.limp()
            elif config.opcion==3:
                appState='login'
                break
    if config.appState=="pedidos":
        config.condicion_general=1
        while config.condicion_general==1:
            config.condicion=1
            config.opcion=fn.menuAdminPedidos()
            config.limp()
            if config.opcion==1:
                while True:
                    try:
                        idMesa = input('>>Ingrese el numero de la mesa o "all" para ver todas las mesas\n<< ').lower()
                        mesa= fn.getMesas(idMesa)
                        if mesa==None:
                            raise ValueError
                    except ValueError:
                        print('>> Valor ingresado incorrecto')
                        input('>> Enter para continuar')
                    except Exception as ms:
                        print('>> Ha ocurrido un error -> {ms}')
                        input('>> Enter para continuar')
                    else:
                        break
                fn.impresionMesas(mesa)
                input('>> Enter para continuar')               
            elif config.opcion==2:
                contador=0
                if len(config.pedidos)>0:
                    for elemento in config.pedidos:
                        contador+=1
                        print(f"{'>> Pedido numero → ' + str(contador):^55}")
                        fn.impresionPedidosIndividuales(elemento)
                    input('>> Enter para continuar ')
                else:
                    print('>> No hay pedidos activos')
                    input('>> Enter para continuar ')
                config.limp()
            elif config.opcion==3:
                if len(config.pedidos)>0:
                    while config.condicion==1:
                        config.pedidos=fn.administrarPedidos(config.pedidos)
                        config.condicion=int(input("Seguir modificando pedidos 1/Si 2/No"))
                        config.limp()
                else:
                    print('>> No hay pedidos activos')
                    input('>> Enter para continuar ')
            elif config.opcion==4:
                fn.impresionRecetas(config.recetas)
                input("Enter para continuar")
                config.limp()
            elif config.opcion==5:
                recetaSeleccionada = fn.impresionRecetas(config.recetas)
                
                fn.consumirIngredientes(recetaSeleccionada,config.inventario)

                input("Enter para continuar")
                config.limp()
            elif config.opcion==6:
                if len(config.pedidos)>0:
                    config.pedidos=fn.repriorizarPedidos(config.pedidos)
                    contador=0
                    for elemento in config.pedidos:
                        contador+=1
                        print(f"{'>> Pedido numero → ' + str(contador):^55}")
                        fn.impresionPedidosIndividuales(elemento)  
                    input('>> Enter para continuar ')
                    config.limp()
                else:
                    print('>> No hay pedidos activos')
                    input('>> Enter para continuar ')
            elif config.opcion==7:
                config.condicion_general=0
                if (config.loggedUserType == 'cocinero' and config.appState == 'pedidos'):#solo para que el cocinero pueda salir al menu de perfiles
                    config.appState='login'
                    config.loggedUserType=''
                    config.loggedUserPermissions=None
    if (config.loggedUserType == 'mesero' and config.appState == 'finalizado'):#solo para que el mesero pueda salir al menu de perfiles
        config.appState='login'
        config.loggedUserType=''
        config.loggedUserPermissions=None
    # Finalizacion
    if(config.appState == config.possibleStatesTupla[-1]):
        config.appState='login'
        config.loggedUserType=''
        config.loggedUserPermissions=None

