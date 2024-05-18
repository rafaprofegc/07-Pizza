import unittest
from Pizza import Pizza

class TestPizza(unittest.TestCase):
    def setUp(self):
        self.p = Pizza("G", True)
        self.p.añade_ingrediente("PE")
        self.p.añade_ingrediente("MO")

    def test_ingredientes(self):
        # Comprobamos que el ingrediente está en la pizza
        self.assertIn("MO", self.p.ingredientes)

        # Comprobamos que el ingrediente NO está en la pizza
        self.assertNotIn("CH", self.p.ingredientes)


    def test_tamaño(self):
        with self.assertRaises(ValueError):
            self.p.tamaño = "P"

    def test_añadir_ingredientes(self):
        resultado = self.p.añade_ingrediente("MO")
        self.assertFalse(resultado)

        resultado = self.p.añade_ingrediente("AT")
        self.assertTrue(resultado)

        with self.assertRaises(KeyError):
            self.p.añade_ingrediente("WW")

    def test_quitar_ingredientes(self):
        resultado = self.p.quitar_ingrediente("MO")
        self.assertTrue(resultado)

        with self.assertRaises(KeyError):
            self.p.quitar_ingrediente("AT")

    def test_calcular_precio(self):
        # Ya tenemos en la pizza MOzzarela y PEperoni
        self.p.añade_ingrediente("PI")
        self.p.añade_ingrediente("AT")
        self.p.añade_ingrediente("PO")

        self.p.quitar_ingrediente("PE")
        self.p.quitar_ingrediente("AT")

        precio = self.p.calcular_precio()
        self.assertEqual(precio, 18.2)

        self.assertNotEqual(precio, 18)
        
        # Esto es un comentario
if __name__ == '__main__':
    unittest.main()
