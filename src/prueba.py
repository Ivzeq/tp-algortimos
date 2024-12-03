import funciones as fn
import config as cnf
recetas_simuladas = [
            {"id": "2000",
 "nombre": "Bife de chorizo",
 "ingredientes": [{"Bife de Chorizo": 1},
 {"Sal": 1},
 {"Pimienta": 1}],
 "tiempo": "30 minutos",
 "instrucciones": "Sazonar el bife y asar a la parrilla."},

    {"id": "2001",
 "nombre": "Asado de tira",
 "ingredientes": [{"Asado de Tira": 1},
 {"Sal": 2},
 {"Pimienta": 1}],
 "tiempo": "45 minutos",
 "instrucciones": "Sazonar y asar a la parrilla."}
        ]
fn.impresionRecetas(recetas_simuladas)
fn.impresionRecetas(cnf.recetas)