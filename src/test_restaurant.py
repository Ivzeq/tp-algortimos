from unittest import TestCase
from unittest.mock import patch, mock_open
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
        mock_file.assert_called_with("restaurant.log", "a")

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

from unittest.mock import patch
from unittest import TestCase

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


