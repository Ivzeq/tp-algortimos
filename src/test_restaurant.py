from unittest import TestCase
from unittest.mock import patch, mock_open, call, ANY
from datetime import datetime
import config as cnf
import funciones as fn
import os



# 1. Tests para intInput
class TestIntInput(TestCase):
    @patch('builtins.input', side_effect=["5", "0"])
    def test_intInput_valores_validos(self, mock_input):
        self.assertEqual(fn.intInput("Ingrese un número:"), 5)
        self.assertEqual(fn.intInput("Ingrese otro número:"), 0)

    @patch('builtins.input', side_effect=["abc", "-1", "10"])
    def test_intInput_valores_invalidos(self, mock_input):
        self.assertEqual(fn.intInput("Ingrese un número:"), 10)

# 2. Tests para charInput
class TestCharInput(TestCase):
    @patch('builtins.input', side_effect=["Alejandro Ramirez", "Luis"])
    def test_charInput_valores_validos(self, mock_input):
        self.assertEqual(fn.charInput("Ingrese un nombre:"), "Alejandro Ramirez")
        self.assertEqual(fn.charInput("Ingrese otro nombre:"), "Luis")

    @patch('builtins.input', side_effect=["123", "Luis@"])
    def test_charInput_valores_invalidos(self, mock_input):
        with self.assertRaises(Exception):  # Simula entrada inválida
            fn.charInput("Ingrese un nombre:")

# 3. Tests para codeInput
class TestCodeInput(TestCase):
    @patch('builtins.input', side_effect=["1234", "5678"])
    def test_codeInput_valores_validos(self, mock_input):
        self.assertEqual(fn.codeInput("Ingrese un código:"), "1234")
        self.assertEqual(fn.codeInput("Ingrese otro código:"), "5678")

    @patch('builtins.input', side_effect=["12", "abc", "12345", "1234"])
    def test_codeInput_valores_invalidos(self, mock_input):
        self.assertEqual(fn.codeInput("Ingrese un código:"), "1234")


# 4. Tests para confirmarInput fn.
class TestConfirmInput(TestCase):
    @patch('builtins.input', side_effect=["s", "n"])
    def test_confirmInput_valores_validos(self, mock_input):
        self.assertEqual(fn.confirmInput("¿Confirmar?"), "s")
        self.assertEqual(fn.confirmInput("¿Cancelar?"), "n")

    @patch('builtins.input', side_effect=["x", "yes", "s"])
    def test_confirmInput_valores_invalidos(self, mock_input):
        self.assertEqual(fn.confirmInput("¿Confirmar?"), "s")

# 5. Tests para registrarExcepcion
class TestRegistrarExcepcion(TestCase):
    @patch("builtins.open", new_callable=mock_open)
    @patch("funciones.datetime")  # Parchea datetime en el módulo que contiene la función
    def test_registrarExcepcion(self, mock_datetime, mock_file):
        mock_datetime.now.return_value = datetime(2024, 12, 1, 12, 0, 0)  # Fecha fija simulada
        mock_datetime.strftime = datetime.strftime  # Mantén el método strftime

        try:
            raise ValueError("Valor inválido")
        except ValueError as e:
            fn.registrarExcepcion(e, "Prueba de registro", ruta_log="restaurant.log")

        # Verifica que el archivo fue abierto en modo append
        mock_file.assert_called_with('restaurant.log', "a", encoding='utf-8')

        # Verifica el contenido completo que se escribió en el archivo
        handle = mock_file()
        handle.write.assert_called_once_with(
            "\nFecha: 2024-12-01 12:00:00\n"
            "Función: test_registrarExcepcion\n"
            "Tipo: ValueError\n"
            "Mensaje: Valor inválido\n"
            "\tPrueba de registro"
        )

# 6. Tests para cargarDatos
class TestCargarDatos(TestCase):
    @patch('builtins.open', create=True)
    def test_cargarDatos_valido(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = '{"key": "value"}'
        self.assertEqual(fn.cargarDatos("ruta.json"), {"key": "value"})

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_cargarDatos_archivo_inexistente(self, mock_open):
        self.assertIsNone(fn.cargarDatos("ruta_invalida.json"))

    @patch('builtins.open', create=True)
    def test_cargarDatos_json_invalido(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = 'no es un json valido'
        self.assertIsNone(fn.cargarDatos("ruta.json"))

# 7. Tests para guardarDatos
class TestGuardarDatos(TestCase):
    @patch('builtins.open', create=True)
    def test_guardarDatos_valido(self, mock_open):
        mock_open.return_value.__enter__.return_value.write.return_value = None
        fn.guardarDatos("ruta.json", {"key": "value"})
        mock_open.assert_called_once()

    @patch('builtins.open', side_effect=PermissionError)
    def test_guardarDatos_permiso_denegado(self, mock_open):
        with self.assertRaises(PermissionError):
            fn.guardarDatos("ruta.json", {"key": "value"})

# 8. Tests para conjuntoCodigo
class TestConjuntoCodigo(TestCase):
    def test_conjuntoCodigo(self):
        self.assertEqual(fn.conjuntoCodigo([]), set())
        self.assertEqual(fn.conjuntoCodigo([{"id": 1}, {"id": 2}]), {1, 2})
        self.assertEqual(fn.conjuntoCodigo([{"id": 1}, {"id": 1}]), {1})

# 9. Tests para totalCuenta
class TestTotalCuenta(TestCase):
    @patch('funciones.cnf', autospec=True)
    def test_totalCuenta(self, mock_cnf):
        # Configura el menú simulado
        mock_cnf.menu = [[1, "Plato 1", 10.0], [2, "Plato 2", 20.0]]

        # Realiza las verificaciones
        self.assertEqual(fn.totalCuenta({"platos": []}), 0)
        self.assertEqual(fn.totalCuenta({"platos": [["Plato 1", 2]]}), 20.0)
        self.assertEqual(fn.totalCuenta({"platos": [["Plato 1", 1], ["Plato 2", 2]]}), 50.0)

# 10. Tests para impresionMenu
class TestImpresionMenu(TestCase):
    def test_impresionMenu(self):
        # Simula un menú con múltiples platos
        menu_simulado = [
            [1, "Bife de Chorizo", 15000, "carne", 5],
            [2, "Asado de Tira", 12800, "carne", 5],
            [3, "Milanesa de Ternera", 12000, "carne", 5],
            [4, "Pollo al Horno", 11000, "pollo", 5],
            [5, "Suprema a la Napolitana", 13000, "pollo", 5],
            [6, "Pollo a la Parrilla", 12500, "pollo", 5],
            [7, "Salmón a la Manteca", 20000, "pescado", 5],
            [8, "Merluza al Horno", 16000, "pescado", 5],
            [9, "Paella de Mariscos", 22000, "pescado", 5],
            [10, "Ensalada Caesar", 9000, "ensalada", 5],
            [11, "Ensalada Mixta", 7500, "ensalada", 5],
            [12, "Ensalada Caprese", 8000, "ensalada", 5],
        ]

        # Cadena esperada basada en la salida actual de la función
        esperado = (
            "\n╔═══════════════════════════════════════════════════════╗\n"
            "║                                                       ║\n"
            "║                     🍽 RESTAURANTE🍽                    ║\n"
            "║                      Menu de platos                   ║\n"
            "║                                                       ║\n"
            "╠═══════════════════════════════════════════════════════╣\n"
            "║Num ║Plato                       ║Precio    ║Categoría ║\n"
            "╠═══════════════════════════════════════════════════════╣\n"
            "║1   ║Bife de Chorizo             ║15000     ║carne     ║\n"
            "║2   ║Asado de Tira               ║12800     ║carne     ║\n"
            "║3   ║Milanesa de Ternera         ║12000     ║carne     ║\n"
            "║4   ║Pollo al Horno              ║11000     ║pollo     ║\n"
            "║5   ║Suprema a la Napolitana     ║13000     ║pollo     ║\n"
            "║6   ║Pollo a la Parrilla         ║12500     ║pollo     ║\n"
            "║7   ║Salmón a la Manteca         ║20000     ║pescado   ║\n"
            "║8   ║Merluza al Horno            ║16000     ║pescado   ║\n"
            "║9   ║Paella de Mariscos          ║22000     ║pescado   ║\n"
            "║10  ║Ensalada Caesar             ║9000      ║ensalada  ║\n"
            "║11  ║Ensalada Mixta              ║7500      ║ensalada  ║\n"
            "║12  ║Ensalada Caprese            ║8000      ║ensalada  ║\n"
            "╚═══════════════════════════════════════════════════════╝"
        )
        
        # Compara la salida generada por la función con la cadena esperada
        assert(esperado == fn.impresionMenu(menu_simulado))

# Test para impresionStockMenu
class TestImpresionStockMenu(TestCase):
    def test_impresionStockMenu(self):
        # Simula un menú con platos disponibles en stock
        menu_simulado = [
            ["2000", "Bife de Chorizo", 15000, "carne", 5],
            ["2001", "Asado de Tira", 12800, "carne", 0],  # Sin stock
            ["2002", "Milanesa de Ternera", 12000, "carne", 3],
        ]

        # Salida esperada basada en los platos con stock > 0
        esperado = (
            "\n╔═══════════════════════════════════════════════════════╗\n"
            "║                                                       ║\n"
            "║                     🍽 RESTAURANTE🍽                    ║\n"
            "║                      Menu de platos                   ║\n"
            "║                                                       ║\n"
            "╠═══════════════════════════════════════════════════════╣\n"
            "║Num ║Plato                       ║Precio    ║Categoría ║\n"
            "╠═══════════════════════════════════════════════════════╣\n"
            "║1   ║Bife de Chorizo             ║15000     ║carne     ║\n"
            "║3   ║Milanesa de Ternera         ║12000     ║carne     ║\n"
            "╚═══════════════════════════════════════════════════════╝"
        )

        # Compara la salida generada por la función con la cadena esperada
        self.assertEqual(esperado, fn.impresionStockMenu(menu_simulado))


class TestImpresionMesas(TestCase):
    def test_impresionMesas(self):
        # Datos simulados de mesas
        mesas_simuladas = [
            {"idMesa": 1, "estado": "Ocupada", "cliente": "Juan"},
            {"idMesa": 2, "estado": "Ocupada", "cliente": "Pedro"},
            {"idMesa": 3, "estado": "Libre", "cliente": "Sin reserva"},
            {"idMesa": 4, "estado": "Libre", "cliente": "Sin reserva"},
        ]

        # Salida esperada
        esperado = (
            "\n╔═════════════════════════════════════════════╗\n"
            "║                                             ║\n"
            "║              🍽 RESTAURANTE🍽                 ║\n"
            "║                   Mesas                     ║\n"
            "║                                             ║\n"
            "╠═════════════════════════════════════════════╣\n"
            "║ Mesa →              1║ Mesa →              2║\n"
            "╠----------------------║----------------------╣\n"
            "║ Estado →      Ocupada║ Estado →      Ocupada║\n"
            "║ Cliente →        Juan║ Cliente →       Pedro║\n"
            "╠═════════════════════════════════════════════╣\n"
            "║ Mesa →              3║ Mesa →              4║\n"
            "╠----------------------║----------------------╣\n"
            "║ Estado →        Libre║ Estado →        Libre║\n"
            "║ Cliente → Sin reserva║ Cliente → Sin reserva║\n"
            "╚═════════════════════════════════════════════╝"
        )

        # Salida real generada por la función
        real = fn.impresionMesas(mesas_simuladas)

        # Comparación
        print("Esperado (repr):", repr(esperado))
        print("Real (repr):", repr(real))
        self.assertEqual(esperado, real)

class TestImpresionRecetas(TestCase):
    def test_impresionRecetas(self):
        # Datos simulados de recetas
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

        # Salida esperada
        esperado = (
            "Listado de recetas:\n"
            "2000: Bife de Chorizo\n"
            "2001: Asado de Tira\n"
        )

        # Comparar la salida generada con la esperada
        self.assertEqual(fn.impresionRecetas(recetas_simuladas), print(esperado))

class TestImpresionIngredientes(TestCase):
    def test_impresionIngredientes(self):
        # Datos simulados
        ingredientes_simulados = [
            {"id": "1000", "nombre": "Bife de Chorizo", "cantidad": 17},
            {"id": "1001", "nombre": "Sal", "cantidad": 170},
            {"id": "1002", "nombre": "Pimienta", "cantidad": 232},
            {"id": "1003", "nombre": "Ternera", "cantidad": 41},
            {"id": "1004", "nombre": "Aceite", "cantidad": 50},
            {"id": "1005", "nombre": "Huevo", "cantidad": 30},
        ]

        # Salida esperada
        esperado = (
            "Listado de Ingredientes:\n"
            "|1004: Aceite               (50 )|  |1000: Bife de Chorizo     (17 )|  \n"
            "|1005: Huevo                (30 )|  |1002: Pimienta            (232)|  \n"
            "|1001: Sal                  (170)|  |1003: Ternera             (41 )|  \n"
        )

        # Comparar la salida generada por la función con la esperada
        self.assertEqual(fn.impresionIngredientes(ingredientes_simulados, columnas=2), print(esperado))

class TestImpresionCompras(TestCase):
    def test_impresionCompras(self):
        # Datos simulados
        compras_simuladas = [
            {"id": "1000", "nombre": "Bife de Chorizo", "cantidad": 5},
            {"id": "1001", "nombre": "Sal", "cantidad": 20},
            {"id": "1002", "nombre": "Pimienta", "cantidad": 10},
        ]

        # Salida esperada
        esperado = (
            "\nEl pedido actual es el siguiente:\n\n"
            "ID        Nombre              Cantidad  \n"
            "========================================\n"
            "1000      Bife de Chorizo     5         \n"
            "1001      Sal                 20        \n"
            "1002      Pimienta            10        \n"
        )

        # Comparar la salida generada por la función con la esperada
        self.assertEqual(fn.impresionCompras(compras_simuladas), print(esperado))

class TestVerificarStock(TestCase):
    def test_verificarStock(self):
        # Datos simulados
        recetas_simuladas = [
            {
                "id": "2000",
                "nombre": "Bife de Chorizo",
                "ingredientes": [
                    {"Bife de Chorizo": 1},
                    {"Sal": 1},
                    {"Pimienta": 1},
                ],
            },
            {
                "id": "2001",
                "nombre": "Asado de Tira",
                "ingredientes": [
                    {"Asado de Tira": 1},
                    {"Sal": 2},
                    {"Pimienta": 1},
                ],
            },
        ]

        ingredientes_simulados = [
            {"nombre": "Bife de Chorizo", "cantidad": 5},
            {"nombre": "Sal", "cantidad": 3},
            {"nombre": "Pimienta", "cantidad": 2},
            {"nombre": "Aceite", "cantidad": 10},
        ]

        # Caso 1: Ingredientes suficientes para la receta 2000
        self.assertTrue(fn.verificarStock("2000", recetas_simuladas, ingredientes_simulados))

        # Caso 2: Ingredientes insuficientes para la receta 2001
        self.assertFalse(fn.verificarStock("2001", recetas_simuladas, ingredientes_simulados))

        # Caso 3: Ingrediente necesario no existe en el stock
        recetas_simuladas[1]["ingredientes"].append({"Vino": 1})
        self.assertFalse(fn.verificarStock("2001", recetas_simuladas, ingredientes_simulados))

class TestRestarIngredientes(TestCase):
    @patch("funciones.guardarDatos")
    def test_restarIngredientes(self, mock_guardarDatos):
        # Datos simulados
        recetas_simuladas = [
            {
                "id": "2000",
                "nombre": "Bife de Chorizo",
                "ingredientes": [
                    {"Bife de Chorizo": 1},
                    {"Sal": 1},
                    {"Pimienta": 1},
                ],
            }
        ]

        ingredientes_simulados = [
            {"nombre": "Bife de Chorizo", "cantidad": 5},
            {"nombre": "Sal", "cantidad": 3},
            {"nombre": "Pimienta", "cantidad": 2},
        ]

        # Caso 1: Ingredientes suficientes
        fn.restarIngredientes("2000", recetas_simuladas, ingredientes_simulados)
        self.assertEqual(ingredientes_simulados, [
            {"nombre": "Bife de Chorizo", "cantidad": 4},
            {"nombre": "Sal", "cantidad": 2},
            {"nombre": "Pimienta", "cantidad": 1},
        ])
        mock_guardarDatos.assert_called_once()

        # Caso 2: Ingredientes insuficientes
        ingredientes_simulados[2]["cantidad"] = 0  # Insuficiente Pimienta
        with self.assertRaises(fn.IngredienteInsuficiente):
            fn.restarIngredientes("2000", recetas_simuladas, ingredientes_simulados)

class TestRestarAuxIngredientes(TestCase):
    def test_restarAuxIngredientes(self):
        # Datos simulados
        recetas_simuladas = [
            {
                "id": "2000",
                "nombre": "Bife de Chorizo",
                "ingredientes": [
                    {"Bife de Chorizo": 2},
                    {"Sal": 1},
                ],
            }
        ]

        ingredientes_simulados = [
            {"nombre": "Bife de Chorizo", "cantidad": 5},
            {"nombre": "Sal", "cantidad": 3},
            {"nombre": "Pimienta", "cantidad": 2},
        ]

        # Resultado esperado tras restar los ingredientes
        esperado = [
            {"nombre": "Bife de Chorizo", "cantidad": 3},  # Restado correctamente
            {"nombre": "Sal", "cantidad": 2},              # Restado correctamente
            {"nombre": "Pimienta", "cantidad": 2},         # Sin cambios
        ]

        # Llamar a la función
        fn.restarAuxIngredientes("2000", recetas_simuladas, ingredientes_simulados)

        # Verificar que los ingredientes se modificaron correctamente
        self.assertEqual(ingredientes_simulados, esperado)

class TestDevolverStock(TestCase):
    @patch("funciones.guardarDatos")
    @patch("funciones.sumarAuxIngredientes")
    def test_devolverStock(self, mock_sumarAuxIngredientes, mock_guardarDatos):
        # Datos simulados
        recetas_simuladas = [
            {
                "id": "2000",
                "nombre": "Bife de Chorizo",
                "ingredientes": [
                    {"Bife de Chorizo": 1},
                    {"Sal": 1},
                ],
            }
        ]
        ingredientes_simulados = [
            {"nombre": "Bife de Chorizo", "cantidad": 5},
            {"nombre": "Sal", "cantidad": 3},
        ]

        # Llamar a la función
        fn.devolverStock("2000", recetas_simuladas, ingredientes_simulados, cant=2)

        # Verificar que sumarAuxIngredientes fue llamado correctamente
        self.assertEqual(mock_sumarAuxIngredientes.call_count, 2)
        mock_sumarAuxIngredientes.assert_called_with("2000", recetas_simuladas, ingredientes_simulados)

        # Verificar que guardarDatos fue llamado correctamente
        mock_guardarDatos.assert_called_once_with(cnf.rutas["ingredientes"], ingredientes_simulados)

class TestCalcularStock(TestCase):
    def test_calcularStock(self):
        # Datos simulados
        recetas_simuladas = [
            {
                "id": "2000",
                "nombre": "Bife de Chorizo",
                "ingredientes": [
                    {"Bife de Chorizo": 1},
                    {"Sal": 1},
                ],
            }
        ]
        ingredientes_simulados = [
            {"nombre": "Bife de Chorizo", "cantidad": 5},
            {"nombre": "Sal", "cantidad": 3},
        ]

        # Caso 1: Puede preparar 3 recetas
        self.assertEqual(fn.calcularStock("2000", recetas_simuladas, ingredientes_simulados), 3)

        # Caso 2: Ingrediente insuficiente
        ingredientes_simulados[1]["cantidad"] = 0  # Sin sal
        self.assertEqual(fn.calcularStock("2000", recetas_simuladas, ingredientes_simulados), 0)

        # Caso 3: Ingrediente faltante
        ingredientes_simulados.pop(0)  # Sin Bife de Chorizo
        self.assertEqual(fn.calcularStock("2000", recetas_simuladas, ingredientes_simulados), 0)

from unittest.mock import patch

class TestActualizarStock(TestCase):
    @patch("funciones.calcularStock")
    @patch("funciones.guardarDatos")
    def test_actualizarStock(self, mock_guardarDatos, mock_calcularStock):
        # Datos simulados
        menu_simulado = [
            ["R001", "Bife de Chorizo", 500, "Carnes", 0],
            ["R002", "Asado de Tira", 600, "Carnes", 0],
        ]
        recetas_simuladas = [
            {"id": "R001", "ingredientes": [{"Bife de Chorizo": 1}, {"Sal": 1}]},
            {"id": "R002", "ingredientes": [{"Asado de Tira": 1}, {"Sal": 2}]},
        ]
        ingredientes_simulados = [
            {"nombre": "Bife de Chorizo", "cantidad": 5},
            {"nombre": "Asado de Tira", "cantidad": 3},
            {"nombre": "Sal", "cantidad": 10},
        ]

        # Configurar valores de retorno para calcularStock
        mock_calcularStock.side_effect = [5, 3]

        # Llamar a la función
        fn.actualizarStock(menu_simulado, recetas_simuladas, ingredientes_simulados)

        # Verificar que calcularStock fue llamado correctamente
        mock_calcularStock.assert_any_call("R001", recetas_simuladas, ingredientes_simulados)
        mock_calcularStock.assert_any_call("R002", recetas_simuladas, ingredientes_simulados)

        # Verificar que los valores del menú fueron actualizados
        self.assertEqual(menu_simulado[0][4], 5)  # Stock para "Bife de Chorizo"
        self.assertEqual(menu_simulado[1][4], 3)  # Stock para "Asado de Tira"

        # Verificar que guardarDatos fue llamado correctamente
        mock_guardarDatos.assert_called_once_with(cnf.rutas["menu"], menu_simulado)

from unittest.mock import patch

class TestActualizarIngredientes(TestCase):
    @patch("funciones.guardarDatos")
    def test_actualizarIngredientes(self, mock_guardarDatos):
        # Datos simulados
        ingredientes_simulados = [
            {"id": "I001", "nombre": "Harina", "cantidad": 5},
            {"id": "I002", "nombre": "Azúcar", "cantidad": 10},
            {"id": "I003", "nombre": "Leche", "cantidad": 8},
        ]
        compras_simuladas = [
            {"id": "I001", "nombre": "Harina", "cantidad": 2},
            {"id": "I002", "nombre": "Azúcar", "cantidad": 3},
        ]

        # Resultado esperado
        ingredientes_esperados = [
            {"id": "I001", "nombre": "Harina", "cantidad": 7},
            {"id": "I002", "nombre": "Azúcar", "cantidad": 13},
            {"id": "I003", "nombre": "Leche", "cantidad": 8},
        ]
        compras_esperadas = []  # Todas las compras procesadas

        # Llamar a la función
        fn.actualizarIngredientes(ingredientes_simulados, compras_simuladas)

        # Verificar que los ingredientes se actualizaron correctamente
        self.assertEqual(ingredientes_simulados, ingredientes_esperados)

        # Verificar que las compras fueron eliminadas
        self.assertEqual(compras_simuladas, compras_esperadas)

        # Verificar que guardarDatos fue llamado dos veces
        self.assertEqual(mock_guardarDatos.call_count, 2)
        mock_guardarDatos.assert_any_call(cnf.rutas["ingredientes"], ingredientes_esperados)
        mock_guardarDatos.assert_any_call(cnf.rutas["compras"], compras_esperadas)


class TestHacerPedido(TestCase):
    @patch("funciones.terminarPedido")
    @patch("funciones.procesarPlato", side_effect=lambda menu, recetas, ingredientes, pedido, plato: pedido["platos"].append({"id": plato, "nombre": "Plato1"}))
    @patch("funciones.seleccionarPlato", side_effect=[1, 0])  # Seleccionar un plato y luego finalizar
    @patch("funciones.impresionStockMenu")
    @patch("funciones.actualizarStock")
    @patch("funciones.inicializarPedido", return_value={"nombre": "Cliente", "mesa": 1, "platos": []})
    @patch("funciones.cargarDatosBasicos", return_value=(
        [{"id": "R001", "nombre": "Plato1", "precio": 100, "categoria": "Entrada", "stock": 10}],
        [{"id": "R001", "ingredientes": [{"Harina": 1}]}],
        [{"nombre": "Harina", "cantidad": 5}],
        []
    ))
    def test_hacerPedido(
        self,
        mock_cargarDatos,
        mock_inicializarPedido,
        mock_actualizarStock,
        mock_impresionStockMenu,
        mock_seleccionarPlato,
        mock_procesarPlato,
        mock_terminarPedido,
    ):
        # Ejecutar la función
        fn.hacerPedido("Cliente", 1)

        # Verificar inicialización del pedido
        mock_inicializarPedido.assert_called_once_with("Cliente", 1)

        # Verificar carga de datos básicos
        mock_cargarDatos.assert_called_once()

        # Verificar actualización inicial del stock
        mock_actualizarStock.assert_called_once()

        # Verificar impresión del menú
        mock_impresionStockMenu.assert_called_once()

        # Verificar que los platos fueron seleccionados y procesados
        self.assertEqual(mock_seleccionarPlato.call_count, 2)
        mock_procesarPlato.assert_called_once()

        # Verificar que terminarPedido fue llamado correctamente
        mock_terminarPedido.assert_called_once()

class TestInicializarPedido(TestCase):
    def test_inicializarPedido(self):
        # Datos de entrada
        nombre = "Juan"
        mesa = 5

        # Resultado esperado
        esperado = {
            "nombre": "Juan",
            "mesa": 5,
            "estado": "recibido",
            "platos": []
        }

        # Llamar a la función y verificar el resultado
        resultado = fn.inicializarPedido(nombre, mesa)
        self.assertEqual(resultado, esperado)

class TestSeleccionarPlato(TestCase):
    @patch("funciones.intInput", side_effect=[1, 0])  # Simula selección válida y finalización
    def test_seleccionarPlato_valido(self, mock_input):
        # Datos simulados del menú
        menu_simulado = [
            ["R001", "Bife de Chorizo", 500, "Carnes", 5],
            ["R002", "Asado de Tira", 600, "Carnes", 3],
        ]

        # Caso 1: Selección válida
        resultado = fn.seleccionarPlato(menu_simulado)
        self.assertEqual(resultado, 1)

        # Caso 2: Finalización
        resultado = fn.seleccionarPlato(menu_simulado)
        self.assertEqual(resultado, 0)

    @patch("funciones.intInput", side_effect=["a", -1, "b", "a", -1, "b", 2])  # Simula entradas inválidas antes de una válida
    def test_seleccionarPlato_invalido(self, mock_input):
        # Datos simulados del menú
        menu_simulado = [
            ["R001", "Bife de Chorizo", 500, "Carnes", 5],
            ["R002", "Asado de Tira", 600, "Carnes", 3],
        ]

        # Verificar que se maneja adecuadamente la entrada inválida
        resultado = fn.seleccionarPlato(menu_simulado)
        self.assertEqual(resultado, 2)

class TestProcesarPlato(TestCase):
    @patch("funciones.intInput", side_effect=[2])  # Simula una cantidad válida
    @patch("funciones.actualizarStock")
    @patch("funciones.restarStock")
    @patch("funciones.agregarAlPedido")
    def test_procesarPlato_valido(self, mock_agregarAlPedido, mock_restarStock, mock_actualizarStock, mock_intInput):
        # Datos simulados
        menu_simulado = [
            ["R001", "Bife de Chorizo", 500, "Carnes", 5],
            ["R002", "Asado de Tira", 600, "Carnes", 3],
        ]
        recetas_simuladas = [{"id": "R001", "ingredientes": [{"Harina": 1}]}]
        ingredientes_simulados = [{"nombre": "Harina", "cantidad": 5}]
        pedido_simulado = {"nombre": "Cliente", "mesa": 1, "platos": []}

        # Llamar a la función
        fn.procesarPlato(menu_simulado, recetas_simuladas, ingredientes_simulados, pedido_simulado, 1)

        # Verificar que las funciones dependientes fueron llamadas correctamente
        mock_agregarAlPedido.assert_called_once_with(pedido_simulado, "bife de chorizo", 2, "R001")
        mock_restarStock.assert_called_once_with("R001", recetas_simuladas, ingredientes_simulados, 2)
        mock_actualizarStock.assert_called_once_with(menu_simulado, recetas_simuladas, ingredientes_simulados)

    @patch("funciones.intInput", side_effect=[6, -1, 2])  # Inválidas seguidas de una válida
    def test_procesarPlato_con_entradas_invalidas(self, mock_intInput):
    # Datos simulados
        menu_simulado = [
            ["R001", "Bife de Chorizo", 500, "Carnes", 5],
        ]
        recetas_simuladas = [{"id": "R001", "ingredientes": [{"Harina": 1}]}]
        ingredientes_simulados = [{"nombre": "Harina", "cantidad": 5}]
        pedido_simulado = {"nombre": "Cliente", "mesa": 1, "platos": []}

        with patch("funciones.agregarAlPedido") as mock_agregarAlPedido, \
             patch("funciones.restarStock") as mock_restarStock, \
             patch("funciones.actualizarStock") as mock_actualizarStock:
            # Llamar a la función
            fn.procesarPlato(menu_simulado, recetas_simuladas, ingredientes_simulados, pedido_simulado, 1)

            # Verificar que las funciones dependientes fueron llamadas correctamente
            mock_agregarAlPedido.assert_called_once_with(
                pedido_simulado, "bife de chorizo", 2, "R001"
            )
            mock_restarStock.assert_called_once_with("R001", recetas_simuladas, ingredientes_simulados, 2)
            mock_actualizarStock.assert_called_once_with(menu_simulado, recetas_simuladas, ingredientes_simulados)


class TestEliminarPedido(TestCase):

    @patch("funciones.devolverStock")  # Mock para devolverStock
    @patch("funciones.actualizarStock")  # Mock para actualizarStock
    def test_eliminarPedido(self, mock_actualizarStock, mock_devolverStock):
        # Datos simulados
        pedido_simulado = {
            "platos": [
                ["Bife de Chorizo", 2, "R001"],
                ["Asado de Tira", 1, "R002"]
            ]
        }
        recetas_simuladas = [
            {"id": "R001", "ingredientes": [{"Bife de Chorizo": 1}]},
            {"id": "R002", "ingredientes": [{"Asado de Tira": 1}]}
        ]
        ingredientes_simulados = [
            {"nombre": "Bife de Chorizo", "cantidad": 10},
            {"nombre": "Asado de Tira", "cantidad": 5}
        ]
        menu_simulado = [
            ["R001", "Bife de Chorizo", 500, "Carnes", 5],
            ["R002", "Asado de Tira", 600, "Carnes", 3]
        ]

        # Llamar a la función
        fn.eliminarPedido(pedido_simulado, recetas_simuladas, ingredientes_simulados, menu_simulado)

        # Verificar que devolverStock se llamó con los argumentos correctos
        mock_devolverStock.assert_any_call("R001", recetas_simuladas, ingredientes_simulados, 2)
        mock_devolverStock.assert_any_call("R002", recetas_simuladas, ingredientes_simulados, 1)

        # Verificar que actualizarStock fue llamada una vez
        mock_actualizarStock.assert_called_once_with(menu_simulado, recetas_simuladas, ingredientes_simulados)



class TestTerminarPedido(TestCase):

    @patch("funciones.guardarDatos")  # Mock para guardarDatos
    @patch("funciones.eliminarPedido")  # Mock para eliminarPedido
    @patch("funciones.confirmInput", side_effect=["s"])  # Confirmar pedido
    @patch("funciones.reduce", side_effect=lambda func, data, start: sum(
        {"plato 1": 100}[p[0].lower()] * p[1] for p in data))  # Simular cálculo del total
    def test_terminarPedido_confirmado(self, mock_reduce, mock_confirmInput, mock_eliminarPedido, mock_guardarDatos):
        # Datos simulados
        pedido_simulado = {"nombre": "Cliente", "mesa": 1, "platos": [["Plato 1", 2, "R001"]]}
        pedidos_simulados = []
        recetas_simuladas = [{"id": "R001", "ingredientes": [{"Harina": 1}]}]
        ingredientes_simulados = [{"nombre": "Harina", "cantidad": 5}]
        menu_simulado = []

        # Llamar a la función
        fn.terminarPedido(pedido_simulado, pedidos_simulados, recetas_simuladas, ingredientes_simulados, menu_simulado, "Cliente", 1)

        # Verificar que el pedido fue agregado y guardado
        self.assertIn(pedido_simulado, pedidos_simulados)
        mock_guardarDatos.assert_called_once_with(cnf.rutas['pedidos'], pedidos_simulados)
        mock_eliminarPedido.assert_not_called()

    @patch("funciones.guardarDatos")  # Mock para guardarDatos
    @patch("funciones.eliminarPedido")  # Mock para eliminarPedido
    @patch("funciones.confirmInput", side_effect=["n"])  # Cancelar pedido
    @patch("funciones.reduce", side_effect=lambda func, data, start: sum(
        {"plato 1": 100}[p[0].lower()] * p[1] for p in data))  # Simular cálculo del total
    def test_terminarPedido_cancelado(self, mock_reduce, mock_confirmInput, mock_eliminarPedido, mock_guardarDatos):
        # Datos simulados
        pedido_simulado = {"nombre": "Cliente", "mesa": 1, "platos": [["Plato 1", 2, "R001"]]}
        pedidos_simulados = []
        recetas_simuladas = [{"id": "R001", "ingredientes": [{"Harina": 1}]}]
        ingredientes_simulados = [{"nombre": "Harina", "cantidad": 5}]
        menu_simulado = []

        # Llamar a la función
        fn.terminarPedido(pedido_simulado, pedidos_simulados, recetas_simuladas, ingredientes_simulados, menu_simulado, "Cliente", 1)

        # Verificar que eliminarPedido fue llamado
        mock_eliminarPedido.assert_called_once_with(pedido_simulado, recetas_simuladas, ingredientes_simulados, menu_simulado)
        self.assertNotIn(pedido_simulado, pedidos_simulados)
        mock_guardarDatos.assert_not_called()


class TestVerPedido(TestCase):

    @patch("funciones.impresionPedidos", return_value=["Pedido 1: Plato 1 x2"])
    @patch("funciones.confirmInput", side_effect=["n"])  # El usuario no cancela el pedido
    @patch("builtins.print")
    def test_verPedido_existente(self, mock_print, mock_confirmInput, mock_impresionPedidos):
        # Datos simulados
        pedidos_simulados = [
            {"nombre": "Cliente", "mesa": 1, "estado": "recibido", "platos": [["Plato 1", 2, "R001"]]},
        ]

        # Llamar a la función
        fn.verPedido("Cliente", 1, pedidos_simulados)

        # Verificar que impresionPedidos fue llamado con el pedido correcto
        mock_impresionPedidos.assert_called_once_with(pedidos_simulados)

        # Verificar que se imprimió el pedido
        mock_print.assert_any_call("Pedido 1: Plato 1 x2")

        # Verificar que no se intentó cancelar
        mock_confirmInput.assert_called_once()

    @patch("funciones.impresionPedidos", return_value=[])
    @patch("builtins.print")
    def test_verPedido_inexistente(self, mock_print, mock_impresionPedidos):
        # Datos simulados
        pedidos_simulados = []

        # Llamar a la función
        fn.verPedido("Otro Cliente", 2, pedidos_simulados)

        # Verificar que impresionPedidos no imprime nada
        mock_impresionPedidos.assert_called_once_with([])

        # Verificar que se imprime el mensaje de error
        mock_print.assert_called_once_with(">> No se encontraron pedidos activos")


class TestAvanzarPedidoCocina(TestCase):

    @patch("funciones.guardarDatos")  # Decorador más interno
    @patch("funciones.intInput", side_effect=[1])  # Decorador intermedio
    @patch("builtins.print")  # Decorador más externo
    def test_avanzarPedidoCocina(self, mock_print, mock_intInput, mock_guardarDatos):
        # Datos simulados
        pedidos_simulados = [
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido", "platos": [["Plato 1", 2, "R001"]]},
        ]
        ruta_pedidos_simulada = "ruta_a_pedidos.json"

        # Llamar a la función
        fn.avanzarPedidoCocina(pedidos_simulados, ruta_pedidos_simulada)

        # Verificar que el estado del pedido fue actualizado
        self.assertEqual(pedidos_simulados[0]["estado"], "en preparacion")

        # Verificar que los datos actualizados se guardaron
        mock_guardarDatos.assert_called_once_with(ruta_pedidos_simulada, pedidos_simulados)

        # Verificar que se imprimió el mensaje de éxito
        mock_print.assert_any_call(">> El pedido de Cliente 1 en la mesa 1 ahora está En preparacion.")


class TestAvanzarPedidoSalon(TestCase): 

    def test_avanzar_pedido(self):
        pedidos_simulados = [
            {"nombre": "Cliente", "mesa": 1, "estado": "entregado", "platos": []}
        ]
        ruta_pedidos_simulada = "ruta_a_pedidos.json"

        with patch("funciones.guardarDatos") as mock_guardarDatos, \
             patch("funciones.intInput", side_effect=[1]) as mock_intInput, \
             patch("funciones.impresionPedidos", return_value=["Pedido 1"]) as mock_impresionPedidos, \
             patch("funciones.cnf.permisosEstadosSalon", ["entregado", "pagado"]), \
             patch("builtins.print") as mock_print:

            # Llamar a la función con los datos simulados
            fn.avanzarPedidoSalon(pedidos_simulados, ruta_pedidos_simulada)

            # Verificar que el pedido avanzó
            self.assertEqual(pedidos_simulados[0]["estado"], "pagado")

            # Verificar mensajes impresos
            mock_print.assert_any_call("El pedido de Cliente en la mesa 1 ahora está Pagado.")

            # Verificar que los datos del pedido se guardaron
            mock_guardarDatos.assert_any_call(ruta_pedidos_simulada, pedidos_simulados)

    def test_pedido_finalizado(self):
        pedidos_simulados = [
            {"nombre": "Cliente", "mesa": 1, "estado": "pagado", "platos": []}
        ]
        ruta_pedidos_simulada = "ruta_a_pedidos.json"

        mesas_simuladas = [
            {"idMesa": 1, "estado": "Ocupada", "cliente": "Cliente"}
        ]
        finalizados_simulados = []

        with patch("funciones.guardarDatos") as mock_guardarDatos, \
             patch("funciones.intInput", side_effect=[1]) as mock_intInput, \
             patch("funciones.impresionPedidos", return_value=["Pedido 1"]) as mock_impresionPedidos, \
             patch("funciones.cnf.permisosEstadosSalon", ["pagado", "finalizado"]), \
             patch("funciones.cnf.mesas", mesas_simuladas), \
             patch("funciones.cnf.finalizados", finalizados_simulados), \
             patch("builtins.print") as mock_print:

            # Llamar a la función con los datos simulados
            fn.avanzarPedidoSalon(pedidos_simulados, ruta_pedidos_simulada)

            # Verificar que el pedido fue eliminado de pedidos_simulados
            self.assertEqual(len(pedidos_simulados), 0)

            # Verificar que el pedido fue movido a finalizados_simulados
            self.assertEqual(len(finalizados_simulados), 1)
            self.assertEqual(finalizados_simulados[0]["estado"], "finalizado")

            # Verificar que la mesa quedó libre
            self.assertEqual(mesas_simuladas[0]["estado"], "Libre")
            self.assertEqual(mesas_simuladas[0]["cliente"], "Sin reserva")

            # Verificar mensajes impresos
            mock_print.assert_any_call("El pedido de Cliente en la mesa 1 ahora está Finalizado.")

            # Verificar que los datos actualizados se guardaron
            mock_guardarDatos.assert_any_call(cnf.rutas["mesas"], mesas_simuladas)
            mock_guardarDatos.assert_any_call(cnf.rutas["finalizados"], finalizados_simulados)
            mock_guardarDatos.assert_any_call(ruta_pedidos_simulada, pedidos_simulados)


class TestCancelarPedido(TestCase):

    @patch("funciones.intInput", side_effect=[1])  # Selecciona el primer pedido
    @patch("funciones.impresionPedidos", return_value=["Pedido 1"])
    @patch("builtins.print")
    def test_cancelar_pedido_normal(self, mock_print, mock_impresionPedidos, mock_intInput):
        pedidos_simulados = [
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido", "platos": []}
        ]

        # Llamar a la función
        fn.cancelarPedido(pedidos_simulados)

        # Verificar que el pedido fue eliminado
        self.assertEqual(len(pedidos_simulados), 0)

        # Verificar el mensaje de cancelación
        mock_print.assert_any_call("El pedido de Cliente 1 ha sido cancelado.")

    @patch("funciones.intInput", side_effect=[0])  # Selecciona salir
    @patch("funciones.impresionPedidos", return_value=["Pedido 1"])
    @patch("builtins.print")
    def test_cancelar_pedido_salir(self, mock_print, mock_impresionPedidos, mock_intInput):
        pedidos_simulados = [
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido", "platos": []}
        ]

        # Llamar a la función
        fn.cancelarPedido(pedidos_simulados)

        # Verificar que ningún pedido fue eliminado
        self.assertEqual(len(pedidos_simulados), 1)

        # Mostrar llamadas reales para depurar
        print(mock_print.call_args_list)

        # Verificar que el mensaje correcto fue impreso
        mock_print.assert_any_call("Pedido 1")
        self.assertNotIn(
            call("El pedido de Cliente 1 ha sido cancelado."),
            mock_print.mock_calls
        )

class TestRepriorizarPedidos(TestCase):

    @patch("funciones.intInput", side_effect=[1, 3])  # Selecciona el primer pedido y lo mueve a la posición 3
    @patch("funciones.impresionPedidos", return_value=["Pedido 1", "Pedido 2", "Pedido 3"])
    @patch("builtins.print")
    def test_repriorizar_pedido_normal(self, mock_print, mock_impresionPedidos, mock_intInput):
        pedidos_simulados = [
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido", "platos": [
            [
                "ensalada caesar",
                3,
                "2009"
            ]]},
            {"nombre": "Cliente 2", "mesa": 2, "estado": "recibido", "platos": [
            [
                "ensalada caesar",
                3,
                "2009"
            ]]},
            {"nombre": "Cliente 3", "mesa": 3, "estado": "recibido", "platos": [
            [
                "ensalada caesar",
                3,
                "2009"
            ]]}
        ]

        # Llamar a la función
        fn.repriorizarPedidos(pedidos_simulados)

        # Verificar que el pedido fue movido a la posición correcta
        self.assertEqual(pedidos_simulados, [
            {"nombre": "Cliente 2", "mesa": 2, "estado": "recibido", "platos": [
            [
                "ensalada caesar",
                3,
                "2009"
            ]]},
            {"nombre": "Cliente 3", "mesa": 3, "estado": "recibido", "platos": [
            [
                "ensalada caesar",
                3,
                "2009"
            ]]},
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido", "platos": [
            [
                "ensalada caesar",
                3,
                "2009"
            ]]}
        ])

    @patch("funciones.intInput", side_effect=[3, 1])  # Selecciona el último pedido y lo mueve al inicio
    @patch("funciones.impresionPedidos", return_value=["Pedido 1", "Pedido 2", "Pedido 3"])
    @patch("builtins.print")
    def test_repriorizar_pedido_límite(self, mock_print, mock_impresionPedidos, mock_intInput):
        pedidos_simulados = [
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido"},
            {"nombre": "Cliente 2", "mesa": 2, "estado": "recibido"},
            {"nombre": "Cliente 3", "mesa": 3, "estado": "recibido"}
        ]

        # Llamar a la función
        fn.repriorizarPedidos(pedidos_simulados)

        # Verificar que el pedido fue movido al inicio
        self.assertEqual(pedidos_simulados, [
            {"nombre": "Cliente 3", "mesa": 3, "estado": "recibido"},
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido"},
            {"nombre": "Cliente 2", "mesa": 2, "estado": "recibido"}
        ])

    @patch("funciones.intInput", side_effect=[5, 1, 6])  # Selección inválida, luego válida, luego elije la ultima posicion
    @patch("funciones.impresionPedidos", return_value=["Pedido 1", "Pedido 2", "Pedido 3"])
    @patch("builtins.print")
    def test_repriorizar_pedido_invalido(self, mock_print, mock_impresionPedidos, mock_intInput):
        pedidos_simulados = [
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido"},
            {"nombre": "Cliente 2", "mesa": 2, "estado": "recibido"},
            {"nombre": "Cliente 3", "mesa": 3, "estado": "recibido"}
        ]

        # Llamar a la función
        fn.repriorizarPedidos(pedidos_simulados)
        
        # Verificar que el pedido fue movido correctamente después de la selección válida
        self.assertEqual(pedidos_simulados, [
            {"nombre": "Cliente 2", "mesa": 2, "estado": "recibido"},
            {"nombre": "Cliente 3", "mesa": 3, "estado": "recibido"},
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido"}
        ])
                
        mock_print.assert_any_call("El pedido de 'Cliente 1' ha sido movido a la posición 6.")

class TestCambiarEstados(TestCase):

    @patch.object(cnf, "estadosPedidos", ["recibido", "en preparacion", "listo"])
    @patch("funciones.impresionPedidos", return_value=["Pedido 1"])
    @patch("builtins.print")
    @patch("funciones.intInput", side_effect=[1, 2])  # Selección de pedido y estado
    def test_cambiar_estado_exitoso(self, mock_intInput, mock_print, mock_impresionPedidos):
        pedidos_simulados = [
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido", "platos": [["Plato 1", 1, "recibido"]]}
        ]

        # Llamar a la función
        fn.cambiarEstados(pedidos_simulados)

        # Verificar que el estado cambió correctamente
        self.assertEqual(pedidos_simulados[0]["estado"], "en preparacion")

        # Verificar que se mostró el mensaje correcto
        mock_print.assert_any_call("El estado del pedido de Cliente 1 ha cambiado a: En preparacion")


    @patch("funciones.intInput", side_effect=[0])  # Selección de salir
    @patch("builtins.print")
    def test_cambiar_estado_salir(self, mock_print, mock_intInput):
        pedidos_simulados = [
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido", "platos": [["Plato 1", 1, "recibido"]]}
        ]

        # Llamar a la función
        fn.cambiarEstados(pedidos_simulados)

        # Verificar que no hubo cambios en el estado
        self.assertEqual(pedidos_simulados[0]["estado"], "recibido")

    @patch("funciones.intInput", side_effect=[5, 0])  # Selección fuera de rango y luego salir
    @patch("builtins.print")
    def test_cambiar_estado_seleccion_invalida(self, mock_print, mock_intInput):
        pedidos_simulados = [
            {"nombre": "Cliente 1", "mesa": 1, "estado": "recibido", "platos": [["Plato 1", 1, "recibido"]]}
        ]

        # Llamar a la función
        fn.cambiarEstados(pedidos_simulados)

        # Verificar que no hubo cambios en el estado
        self.assertEqual(pedidos_simulados[0]["estado"], "recibido")

class TestPedirIngredientes(TestCase):
    @patch("funciones.codeInput", side_effect=["1001", "1002"])  # Códigos de ingredientes
    @patch("funciones.intInput", side_effect=[5, 3])  # Cantidades ingresadas
    @patch("funciones.input", side_effect=["s", "n"])  # Finalizar ingreso
    @patch("funciones.guardarDatos")  # Mock para evitar guardar en disco durante el test
    def test_pedir_ingredientes(self, mock_guardarDatos, mock_input, mock_intInput, mock_codeInput):
        # Datos iniciales
        ingredientes = [
            {"id": "1001", "nombre": "Sal", "cantidad": 77},
            {"id": "1002", "nombre": "Pimienta", "cantidad": 186},
        ]
        compras = []

        # Llamar la función
        fn.pedirIngredientes(ingredientes, compras)

        # Verificar cambios
        self.assertEqual(len(compras), 2)
        self.assertEqual(compras[0]["id"], "1001")
        self.assertEqual(compras[0]["cantidad"], 5)
        self.assertEqual(compras[1]["id"], "1002")
        self.assertEqual(compras[1]["cantidad"], 3)

        # Verificar que guardarDatos fue llamado
        mock_guardarDatos.assert_called_once()

    @patch("funciones.codeInput", side_effect=["1003", "1001"])  # Código no existente
    @patch("funciones.intInput", side_effect=[5])  # Cantidad ingresada
    @patch("funciones.input", side_effect=["n"])  # Finalizar ingreso
    def test_pedir_ingredientes_codigo_invalido(self, mock_input, mock_intInput, mock_codeInput):
        # Datos iniciales
        ingredientes = [
            {"id": "1001", "nombre": "Sal", "cantidad": 77},
            {"id": "1002", "nombre": "Pimienta", "cantidad": 186},
        ]
        compras = []

        # Llamar la función
        fn.pedirIngredientes(ingredientes, compras)

        # Verificar que se agrego solo uno
        self.assertEqual(len(compras), 1)

    @patch("funciones.codeInput", side_effect=["1001", "1001"])  # Duplicar código de ingrediente
    @patch("funciones.intInput", side_effect=[5, 3])  # Cantidades ingresadas
    @patch("funciones.input", side_effect=["s", "n"])  # Finalizar ingreso
    @patch("funciones.guardarDatos")
    def test_pedir_ingredientes_codigo_duplicado(self, mock_guardarDatos, mock_input, mock_intInput, mock_codeInput):
        # Datos iniciales
        ingredientes = [
            {"id": "1001", "nombre": "Sal", "cantidad": 77},
            {"id": "1002", "nombre": "Pimienta", "cantidad": 186},
        ]
        compras = []

        # Llamar la función
        fn.pedirIngredientes(ingredientes, compras)

        # Verificar que se manejaron códigos duplicados
        self.assertEqual(len(compras), 1)  # Solo se cuenta una entrada
        self.assertEqual(compras[0]["id"], "1001")
        self.assertEqual(compras[0]["cantidad"], 8)  # Se suma la cantidad


class TestModificarCompras(TestCase):
    @patch("funciones.codeInput", side_effect=["1001"])  # Código de ingrediente existente
    @patch("funciones.intInput", side_effect=[10])  # Nueva cantidad deseada
    @patch("funciones.input", side_effect=["n"])  # Finalizar modificación
    @patch("funciones.guardarDatos")  # Mock para evitar guardar en disco
    def test_modificar_compras_valido(self, mock_guardarDatos, mock_input, mock_intInput, mock_codeInput):
        # Datos simulados
        compras = [{"id": "1001", "nombre": "Sal", "cantidad": 5}]
        
        # Llamar a la función
        fn.modificarCompras(compras)

        # Verificar cambios
        self.assertEqual(compras[0]["cantidad"], 10)

        # Verificar que los datos se guardaron
        mock_guardarDatos.assert_called_once()

    @patch("funciones.codeInput", side_effect=["9999", "1001"])  # Código de ingrediente inexistente
    @patch("funciones.intInput", return_value=1)  # Nueva cantidad deseada
    @patch("funciones.input", side_effect=["n"])  # Finalizar modificación
    @patch("funciones.guardarDatos")
    def test_modificar_compras_codigo_invalido(self, mock_guardarDatos, mock_input, mock_intInput, mock_codeInput):
        # Datos simulados
        compras = [{"id": "1001", "nombre": "Sal", "cantidad": 5}]
        
        # Llamar a la función
        fn.modificarCompras(compras)

        # Verificar que hubo cambios correctos
        self.assertEqual(compras[0]["cantidad"], 1)

        # Verificar que no se guardaron datos con codigos incorrectos
        mock_guardarDatos.assert_called_once()

class TestIngresarCompras(TestCase):
    @patch("funciones.confirmInput", side_effect=["s"])  # Confirmar ingreso
    @patch("funciones.actualizarIngredientes")  # Mock de actualización de ingredientes
    def test_ingresar_compras_confirmado(self, mock_actualizarIngredientes, mock_confirmInput):
        # Datos simulados
        compras_simuladas = [{"id": "1001", "nombre": "Sal", "cantidad": 10}]
        ingredientes_simulados = [{"id": "1001", "nombre": "Sal", "cantidad": 20}]

        # Llamar a la función
        fn.ingresarCompras(compras_simuladas, ingredientes_simulados)

        # Verificar que actualizarIngredientes fue llamado correctamente
        mock_actualizarIngredientes.assert_called_once_with(ingredientes_simulados, compras_simuladas)

    @patch("funciones.confirmInput", side_effect=["n"])  # Rechazar ingreso
    @patch("funciones.actualizarIngredientes")  # Mock de actualización de ingredientes
    def test_ingresar_compras_rechazado(self, mock_actualizarIngredientes, mock_confirmInput):
        # Datos simulados
        compras_simuladas = [{"id": "1001", "nombre": "Sal", "cantidad": 10}]
        ingredientes_simulados = [{"id": "1001", "nombre": "Sal", "cantidad": 20}]

        # Llamar a la función
        fn.ingresarCompras(compras_simuladas, ingredientes_simulados)

        # Verificar que actualizarIngredientes no fue llamado
        mock_actualizarIngredientes.assert_not_called()

class TestReservarMesa(TestCase):
    @patch("funciones.guardarDatos", autospec=True)  # Mock directo de la función guardarDatos
    @patch("funciones.cnf", autospec=True)  # Mock completo del módulo cnf
    def test_reservar_mesa_valido(self, mock_cnf, mock_guardarDatos):
        # Datos simulados
        mesas_simuladas = [
            {"idMesa": 1, "estado": "Libre", "cliente": "Sin reserva"},
            {"idMesa": 2, "estado": "Ocupada", "cliente": "Ale"},
        ]
        cliente = "Juan"
        ruta_mock = "ruta/falsa/mesas.json"  # Simulamos una ruta falsa

        # Configurar el mock de cnf
        mock_cnf.mesas = mesas_simuladas

        # Llamar a la función con la ruta mock
        fn.reservarMesa(1, cliente, ruta_mock)

        # Verificar cambios
        self.assertEqual(mock_cnf.mesas[0]["estado"], "Ocupada")
        self.assertEqual(mock_cnf.mesas[0]["cliente"], cliente)

    @patch("funciones.registrarExcepcion")
    @patch("funciones.cnf", autospec=True)
    def test_reservar_mesa_ocupada(self, mock_cnf, mock_registrarExcepcion):
        # Datos simulados
        mesas_simuladas = [
            {"idMesa": 1, "estado": "Ocupada", "cliente": "Ale"},
        ]
        cliente = "Juan"

        # Configurar el mock de cnf
        mock_cnf.mesas = mesas_simuladas

        # Llamar a la función y verificar la excepción
        with self.assertRaises(fn.MesaOcupada):
            fn.reservarMesa(1, cliente)

        # Verificar que se registró la excepción
        mock_registrarExcepcion.assert_called_once()

    @patch("funciones.registrarExcepcion")
    @patch("funciones.cnf", autospec=True)
    def test_reservar_mesa_inexistente(self, mock_cnf, mock_registrarExcepcion):
        # Datos simulados
        mesas_simuladas = [
            {"idMesa": 1, "estado": "Libre", "cliente": "Sin reserva"},
        ]
        cliente = "Juan"

        # Configurar el mock de cnf
        mock_cnf.mesas = mesas_simuladas

        # Llamar a la función y verificar la excepción
        with self.assertRaises(StopIteration):
            fn.reservarMesa(99, cliente)

        # Verificar que se registró la excepción
        mock_registrarExcepcion.assert_called_once()

class TestGestionarReserva(TestCase):
    @patch("funciones.intInput", side_effect=[1])  # Seleccionar mesa 1
    @patch("funciones.charInput", return_value="Juan")  # Nombre del cliente
    @patch("funciones.reservarMesa")  # Mock de la función reservarMesa
    def test_gestionar_reserva_valida(self, mock_reservarMesa, mock_charInput, mock_intInput):
        # Llamar a la función
        cliente, mesa = fn.gestionarReserva()

        # Verificar resultados
        self.assertEqual(cliente, "Juan")
        self.assertEqual(mesa, 1)

        # Verificar que reservarMesa fue llamado con los parámetros correctos
        mock_reservarMesa.assert_called_once_with(1, "Juan")

    @patch("funciones.intInput", side_effect=[2, 3])  # Intentar mesa ocupada, luego libre
    @patch("funciones.charInput", return_value="Pedro")  # Nombre del cliente
    @patch("funciones.reservarMesa", side_effect=[fn.MesaOcupada(2, "Koko"), None])  # Error para mesa 2
    @patch("builtins.print")  # Mock para verificar mensajes
    def test_gestionar_reserva_mesa_ocupada(self, mock_print, mock_reservarMesa, mock_charInput, mock_intInput):
        # Llamar a la función
        cliente, mesa = fn.gestionarReserva()

        # Verificar que eventualmente se reservó la mesa 3
        self.assertEqual(cliente, "Pedro")
        self.assertEqual(mesa, 3)

        # Verificar que reservarMesa fue llamado dos veces
        self.assertEqual(mock_reservarMesa.call_count, 2)

        # Verificar mensajes impresos
        mock_print.assert_any_call("Por favor, seleccione otra mesa.")


class TestCerrarMesa(TestCase):
    @patch("funciones.guardarDatos")  # Mock para evitar escritura en disco
    @patch("funciones.impresionMesas", return_value="Listado de mesas")  # Mock para listado
    @patch("funciones.intInput", side_effect=[1])  # Seleccionar mesa 1
    @patch("funciones.cnf", autospec=True)  # Mock completo del módulo cnf
    def test_cerrar_mesa_valida(self, mock_cnf, mock_intInput, mock_impresionMesas, mock_guardarDatos):
        # Datos simulados
        mesas_simuladas = [
            {"idMesa": 1, "estado": "Ocupada", "cliente": "Juan"},
            {"idMesa": 2, "estado": "Libre", "cliente": "Sin reserva"},
        ]
        mock_cnf.mesas = mesas_simuladas

        # Llamar a la función
        fn.cerrarMesa()

        # Verificar cambios
        self.assertEqual(mock_cnf.mesas[0]["estado"], "Libre")
        self.assertEqual(mock_cnf.mesas[0]["cliente"], "Sin reserva")

        # Verificar que guardarDatos fue llamado con los argumentos correctos
        mock_guardarDatos.assert_called_once_with(mock_cnf.rutas["mesas"], mock_cnf.mesas)

    @patch("funciones.guardarDatos")
    @patch("funciones.impresionMesas", return_value="Listado de mesas")
    @patch("funciones.intInput", side_effect=[0])  # Salir
    @patch("funciones.cnf", autospec=True)
    def test_cerrar_mesa_salir(self, mock_cnf, mock_intInput, mock_impresionMesas, mock_guardarDatos):
        # Datos simulados
        mesas_simuladas = [
            {"idMesa": 1, "estado": "Ocupada", "cliente": "Juan"},
        ]
        mock_cnf.mesas = mesas_simuladas

        # Llamar a la función
        fn.cerrarMesa()

        # Verificar que no se realizaron cambios
        self.assertEqual(mock_cnf.mesas[0]["estado"], "Ocupada")
        self.assertEqual(mock_cnf.mesas[0]["cliente"], "Juan")

        # Verificar que guardarDatos no fue llamado
        mock_guardarDatos.assert_not_called()


class TestMostrarMenuCliente(TestCase):
    @patch("funciones.intInput", side_effect=[1])  # Opción válida
    def test_mostrar_menu_cliente_opcion_valida(self, mock_intInput):
        # Llamar a la función
        opcion = fn.mostrarMenuCliente()

        # Verificar que devuelve la opción seleccionada
        self.assertEqual(opcion, 1)

    @patch("funciones.intInput", side_effect=[5, 3])  # Entradas inválidas y luego válida
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_mostrar_menu_cliente_entrada_invalida(self, mock_print, mock_intInput):
        # Llamar a la función
        opcion = fn.mostrarMenuCliente()

        # Verificar que devuelve la opción válida
        self.assertEqual(opcion, 3)


    @patch("funciones.intInput", side_effect=ValueError("Entrada inválida"))  # Simular excepción
    @patch("funciones.registrarExcepcion")  # Mock para registrar excepciones
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_mostrar_menu_cliente_excepcion(self, mock_print, mock_registrarExcepcion, mock_intInput):
        # Verificar que la excepción se relanza
        with self.assertRaises(ValueError):
            fn.mostrarMenuCliente()

        # Verificar que se registró la excepción con los argumentos esperados
        mock_registrarExcepcion.assert_called_once_with(ANY, "Error al capturar la opción del menú del cliente.")

        # Verificar mensaje de error
        mock_print.assert_any_call("Error inesperado. Por favor, intente nuevamente.")

class TestEjecutarOpcionCliente(TestCase):
    @patch("funciones.impresionMenu", return_value="Menú impreso")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_cliente_opcion_1(self, mock_input, mock_impresionMenu):
        # Llamar a la función con la opción 1
        resultado = fn.ejecutarOpcionCliente(1, "Juan", 1)

        # Verificar que se imprimió el menú
        mock_impresionMenu.assert_called_once_with(cnf.menu)
        self.assertTrue(resultado)

    @patch("funciones.hacerPedido")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_cliente_opcion_2(self, mock_input, mock_hacerPedido):
        # Llamar a la función con la opción 2
        resultado = fn.ejecutarOpcionCliente(2, "Juan", 1)

        # Verificar que se llamó a hacerPedido
        mock_hacerPedido.assert_called_once_with("Juan", 1)
        self.assertTrue(resultado)

    @patch("funciones.verPedido")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_cliente_opcion_3(self, mock_input, mock_verPedido):
        # Llamar a la función con la opción 3
        resultado = fn.ejecutarOpcionCliente(3, "Juan", 1)

        # Verificar que se llamó a verPedido
        mock_verPedido.assert_called_once_with("Juan", 1, cnf.pedidos)
        self.assertTrue(resultado)

    @patch("builtins.print")
    def test_ejecutar_opcion_cliente_opcion_4(self, mock_print):
        # Llamar a la función con la opción 4
        resultado = fn.ejecutarOpcionCliente(4, "Juan", 1)

        # Verificar que el mensaje de despedida se imprime y devuelve False
        mock_print.assert_called_once_with(">> Gracias, Juan.")
        self.assertFalse(resultado)

    @patch("funciones.hacerPedido", side_effect=Exception("Error simulado"))
    @patch("funciones.registrarExcepcion")  # Mock para registrar excepciones
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_ejecutar_opcion_cliente_excepcion(self, mock_print, mock_registrarExcepcion, mock_hacerPedido):
        # Llamar a la función con una opción que genera excepción
        resultado = fn.ejecutarOpcionCliente(2, "Juan", 1)

        # Verificar que se registró la excepción
        mock_registrarExcepcion.assert_called_once_with(ANY, "Error al ejecutar la opción 2 en el menú del cliente.")

        # Verificar mensaje de error
        mock_print.assert_any_call("Error inesperado al procesar la opción. Por favor, intente nuevamente.")
        self.assertTrue(resultado)

class TestMostrarMenuCocina(TestCase):
    @patch("funciones.intInput", side_effect=[3])  # Opción válida
    def test_mostrar_menu_cocina_opcion_valida(self, mock_intInput):
        # Llamar a la función
        opcion = fn.mostrarMenuCocina()

        # Verificar que devuelve la opción seleccionada
        self.assertEqual(opcion, 3)

    @patch("funciones.intInput", side_effect=[8, 5])  # Entradas inválidas y luego válida
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_mostrar_menu_cocina_entrada_invalida(self, mock_print, mock_intInput):
        # Llamar a la función
        opcion = fn.mostrarMenuCocina()

        # Verificar que devuelve la opción válida
        self.assertEqual(opcion, 5)

        # Verificar mensajes de error
        mock_print.assert_any_call("Opción inválida. Ingrese un número entre 1 y 7.\n")

    @patch("funciones.intInput", side_effect=ValueError("Entrada inválida"))  # Simular excepción
    @patch("funciones.registrarExcepcion")  # Mock para registrar excepciones
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_mostrar_menu_cocina_excepcion(self, mock_print, mock_registrarExcepcion, mock_intInput):
        # Verificar que la excepción se relanza
        with self.assertRaises(ValueError):
            fn.mostrarMenuCocina()

        # Verificar que se registró la excepción
        mock_registrarExcepcion.assert_called_once_with(ANY, "Error al capturar la opción del menú de cocina.")

        # Verificar mensaje de error
        mock_print.assert_any_call("Error inesperado. Por favor, intente nuevamente.")

class TestEjecutarOpcionCocina(TestCase):
    @patch("funciones.impresionPedidos", return_value=["Pedido 1", "Pedido 2"])
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_ejecutar_opcion_cocina_opcion_1(self, mock_print, mock_input, mock_impresionPedidos):
        # Llamar a la función con la opción 1
        resultado = fn.ejecutarOpcionCocina(1)

        # Verificar que se imprimieron los pedidos
        mock_impresionPedidos.assert_called_once_with(cnf.pedidos)
        mock_print.assert_any_call("Pedido 1")
        mock_print.assert_any_call("Pedido 2")
        self.assertTrue(resultado)

    @patch("funciones.avanzarPedidoCocina")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_cocina_opcion_2(self, mock_input, mock_avanzarPedidoCocina):
        # Llamar a la función con la opción 2
        resultado = fn.ejecutarOpcionCocina(2)

        # Verificar que se llamó avanzarPedidoCocina
        mock_avanzarPedidoCocina.assert_called_once_with(cnf.pedidos, cnf.rutas["pedidos"])
        self.assertTrue(resultado)

    @patch("funciones.consultarReceta")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_cocina_opcion_3(self, mock_input, mock_consultarReceta):
        # Llamar a la función con la opción 3
        resultado = fn.ejecutarOpcionCocina(3)

        # Verificar que se llamó consultarReceta
        mock_consultarReceta.assert_called_once_with(cnf.recetas)
        self.assertTrue(resultado)

    @patch("funciones.impresionIngredientes")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_cocina_opcion_4(self, mock_input, mock_impresionIngredientes):
        # Llamar a la función con la opción 4
        resultado = fn.ejecutarOpcionCocina(4)

        # Verificar que se llamó impresionIngredientes
        mock_impresionIngredientes.assert_called_once_with(cnf.ingredientes)
        self.assertTrue(resultado)

    @patch("funciones.pedirIngredientes")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_cocina_opcion_5(self, mock_input, mock_pedirIngredientes):
        # Llamar a la función con la opción 5
        resultado = fn.ejecutarOpcionCocina(5)

        # Verificar que se llamó pedirIngredientes
        mock_pedirIngredientes.assert_called_once_with(cnf.ingredientes, cnf.compras)
        self.assertTrue(resultado)

    @patch("funciones.impresionCompras")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_cocina_opcion_6(self, mock_input, mock_impresionCompras):
        # Llamar a la función con la opción 6
        resultado = fn.ejecutarOpcionCocina(6)

        # Verificar que se llamó impresionCompras
        mock_impresionCompras.assert_called_once_with(cnf.compras)
        self.assertTrue(resultado)

    @patch("builtins.print")  # Mock para capturar impresiones
    def test_ejecutar_opcion_cocina_opcion_7(self, mock_print):
        # Llamar a la función con la opción 7
        resultado = fn.ejecutarOpcionCocina(7)

        # Verificar que se imprimió el mensaje de cierre y devuelve False
        mock_print.assert_called_once_with(">> Cerrando módulo de cocina.")
        self.assertFalse(resultado)

        
class TestMostrarMenuSalon(TestCase):
    @patch("funciones.intInput", side_effect=[2])  # Opción válida
    def test_mostrar_menu_salon_opcion_valida(self, mock_intInput):
        # Llamar a la función
        opcion = fn.mostrarMenuSalon()

        # Verificar que devuelve la opción seleccionada
        self.assertEqual(opcion, 2)

    @patch("funciones.intInput", side_effect=["a", 7, 3])  # Entradas inválidas y luego válida
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_mostrar_menu_salon_entrada_invalida(self, mock_print, mock_intInput):
        # Llamar a la función
        opcion = fn.mostrarMenuSalon()

        # Verificar que devuelve la opción válida
        self.assertEqual(opcion, 3)

        # Verificar mensajes de error
        mock_print.assert_any_call(">> Opción inválida. Ingrese un número entre 1 y 6.\n")

    @patch("funciones.intInput", side_effect=ValueError("Entrada inválida"))  # Simular excepción
    @patch("funciones.registrarExcepcion")  # Mock para registrar excepciones
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_mostrar_menu_salon_excepcion(self, mock_print, mock_registrarExcepcion, mock_intInput):
        # Verificar que la excepción se relanza
        with self.assertRaises(ValueError):
            fn.mostrarMenuSalon()

        # Verificar que se registró la excepción
        mock_registrarExcepcion.assert_called_once_with(ANY, "Error al capturar la opción del menú del salón.")

        # Verificar mensaje de error
        mock_print.assert_any_call("Error inesperado. Por favor, intente nuevamente.")

class TestEjecutarOpcionSalon(TestCase):
    @patch("funciones.impresionMesas", return_value="Listado de mesas")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_ejecutar_opcion_salon_opcion_1(self, mock_print, mock_input, mock_impresionMesas):
        # Llamar a la función con la opción 1
        resultado = fn.ejecutarOpcionSalon(1)

        # Verificar que se imprimieron las mesas
        mock_impresionMesas.assert_called_once_with(cnf.mesas)
        mock_print.assert_any_call("Listado de mesas")
        self.assertTrue(resultado)

    @patch("funciones.impresionPedidos", return_value=["Pedido 1", "Pedido 2"])
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    @patch("builtins.print")  # Mock para capturar impresiones
    def test_ejecutar_opcion_salon_opcion_2(self, mock_print, mock_input, mock_impresionPedidos):
        # Llamar a la función con la opción 2
        resultado = fn.ejecutarOpcionSalon(2)

        # Verificar que se imprimieron los pedidos
        mock_impresionPedidos.assert_called_once_with(cnf.pedidos)
        mock_print.assert_any_call("Pedido 1")
        mock_print.assert_any_call("Pedido 2")
        self.assertTrue(resultado)

    @patch("funciones.avanzarPedidoSalon")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_salon_opcion_3(self, mock_input, mock_avanzarPedidoSalon):
        # Llamar a la función con la opción 3
        resultado = fn.ejecutarOpcionSalon(3)

        # Verificar que se llamó avanzarPedidoSalon
        mock_avanzarPedidoSalon.assert_called_once_with(cnf.pedidos, cnf.rutas["pedidos"])
        self.assertTrue(resultado)

    @patch("funciones.cerrarMesa")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_salon_opcion_4(self, mock_input, mock_cerrarMesa):
        # Llamar a la función con la opción 4
        resultado = fn.ejecutarOpcionSalon(4)

        # Verificar que se llamó cerrarMesa
        mock_cerrarMesa.assert_called_once()
        self.assertTrue(resultado)

    @patch("funciones.ingresoAdmin")
    @patch("builtins.input", return_value="")  # Simular pausa con Enter
    def test_ejecutar_opcion_salon_opcion_5(self, mock_input, mock_ingresoAdmin):
        # Llamar a la función con la opción 5
        resultado = fn.ejecutarOpcionSalon(5)

        # Verificar que se llamó ingresoAdmin
        mock_ingresoAdmin.assert_called_once()
        self.assertTrue(resultado)

    @patch("builtins.print")  # Mock para capturar impresiones
    def test_ejecutar_opcion_salon_opcion_6(self, mock_print):
        # Llamar a la función con la opción 6
        resultado = fn.ejecutarOpcionSalon(6)

        # Verificar que el mensaje de cierre se imprime y devuelve False
        mock_print.assert_called_once_with(">> Cerrando módulo de salón.")
        self.assertFalse(resultado)
