import unittest
from calculadora_avancada.avancado import raiz_quadrada, potencia
from calculadora_avancada.utils import validacao_numerica

class TestAvancado(unittest.TestCase):

    def test_raiz_quadrada(self):
        self.assertEqual(raiz_quadrada(9), 3)
        with self.assertRaises(ValueError):
            raiz_quadrada(-1)

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_validacao_numerica(self):
        self.assertTrue(validacao_numerica(10))
        with self.assertRaises(ValueError):
            validacao_numerica("string")

if __name__ == '__main__':
    unittest.main()
