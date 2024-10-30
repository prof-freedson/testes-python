# 1) Importar a classe 'Calculadora'
from calculadora import Calculadora

# 2) Importar o pacote de testes unitários
import unittest

# 3) Criar a classe de testes unitários
class TestCalculadora(unittest.TestCase):
    
    # 4) Criar o objeto para
    # herdar a classe Calculadora
    # através do método chamado 'setUp'
    def setUp(self):
        self.calc = Calculadora()
        
    # 5) Criando o teste
    # do método 'soma'
    def test_soma(self):
        self.assertEqual(self.calc.soma(10, 10), 20, "Deve somar dois números")
        
# Executar a classe de testes unitários
if __name__ == "__main__":
    unittest.main()