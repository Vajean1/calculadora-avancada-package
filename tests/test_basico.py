import unittest
from calculadora_avancada.basico import soma, subtracao

class TestBasico(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(1, 2), 3)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)

if __name__ == '__main__':
    unittest.main()
