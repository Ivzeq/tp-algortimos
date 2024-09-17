"""importaciones"""

"""variables"""
mesas = [
    {
        "idMesa": '1',
        "estado": 'libre',
        "cantPersonas": 0,
        "limite_Personas":6
    },
    {
        "idMesa": '2',
        "estado": 'libre',
        "cantPersonas": 0,
        "limite_Personas":3
    },
    
]
id_mesa=""

"""funciones"""
def verificador_disponibilidad(cantidad_comensales,diccionario_mesas):
    """variables"""
    global id_mesa
    """"FORMATO DE MESAS UTILIZADO PARA LA FUNCION
    idMesa": '5',
    estado": 'abonado',libre,menu,esperando comida,comiendo,abonado(estods posibles)
    cantPersonas": 0
    limite_Personas:6
    """    
    for elemento in diccionario_mesas:
        if elemento["limite_Personas"]>=cantidad_comensales and elemento["estado"]=="libre":
            #"si hay disponibilidad de mesas"
            id_mesa= elemento["idMesa"]
            return True
            #devuelve true y modifica el id de la mesa
    return False

"""programa"""
print("el usuario ya ingreso")
input("ingrese nombre de cliente :")
cantidad_comensales=int(input("ingrese la cantidad de comensales:"))
if verificador_disponibilidad(cantidad_comensales,mesas):
    #entramos al if si solo la funcion verificador_disponibilidad devuelve true
    print(f"hay disponibilidad de mesas, la mesa es {id_mesa}")
    #modificamos el estado de la mesa buscandola por su id
    for elemento in mesas:
        if elemento["idMesa"]==id_mesa:
            elemento["estado"]="menu"
            elemento["cantPersonas"]=cantidad_comensales
else:
    print("no hay disponibilidad de mesas")    
