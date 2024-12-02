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