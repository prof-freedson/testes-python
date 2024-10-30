from calculadoraIMC import CalculadoraIMC

import unittest

class TestCalculadoraIMC(unittest.TestCase):
    def setUp(self):
        self.calcIMC = CalculadoraIMC()
        
    # testando o método calcular
    def test_calcular(self):
        self.assertEqual(self.calcIMC.calcular(55, 1.80), "Magreza")
        self.assertEqual(self.calcIMC.calcular(70, 1.80), "Normal")
        self.assertEqual(self.calcIMC.calcular(85, 1.80), "Sobrepeso")
        self.assertEqual(self.calcIMC.calcular(95, 1.80), "Obesidade")

if __name__ == "__main__":
    unittest.main()