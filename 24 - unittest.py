# Importando o módulo unittest, que nos permite escrever testes automatizados.
import unittest

# Importando as funções de operações do arquivo operacoes.py
from operacoes import somar, subtrair, multiplicar, dividir

# Classe que contém os testes unitários para as funções de operações
class TestOperacoes(unittest.TestCase):

    # Teste para a função 'somar'
    def test_somar(self):
        # Verifica se a soma de 2 e 3 é igual a 5
        self.assertEqual(somar(2, 3), 5)
        
        # Verifica se a soma de -1 e 1 é igual a 0
        self.assertEqual(somar(-1, 1), 0)
        
        # Verifica se a soma de -2 e -3 é igual a -5
        self.assertEqual(somar(-2, -3), -5)

    # Teste para a função 'subtrair'
    def test_subtrair(self):
        # Verifica se a subtração de 5 e 3 é igual a 2
        self.assertEqual(subtrair(5, 3), 2)
        
        # Verifica se a subtração de -1 e 1 é igual a -2
        self.assertEqual(subtrair(-1, 1), -2)
        
        # Verifica se a subtração de 0 e 0 é igual a 0
        self.assertEqual(subtrair(0, 0), 0)

    # Teste para a função 'multiplicar'
    def test_multiplicar(self):
        # Verifica se a multiplicação de 2 e 3 é igual a 6
        self.assertEqual(multiplicar(2, 3), 6)
        
        # Verifica se a multiplicação de -1 e 1 é igual a -1
        self.assertEqual(multiplicar(-1, 1), -1)
        
        # Verifica se a multiplicação de 0 e 5 é igual a 0
        self.assertEqual(multiplicar(0, 5), 0)

    # Teste para a função 'dividir'
    def test_dividir(self):
        # Verifica se a divisão de 6 por 2 é igual a 3
        self.assertEqual(dividir(6, 2), 3)
        
        # Verifica se a divisão de -6 por 3 é igual a -2
        self.assertEqual(dividir(-6, 3), -2)

        # Verifica se a divisão por zero levanta o erro correto
        with self.assertRaises(ValueError):
            dividir(1, 0)  # Espera-se que levante um ValueError quando tentar dividir por zero

# Esse código permite que os testes sejam executados quando rodamos o arquivo diretamente
if __name__ == '__main__':
    unittest.main()  # Executa todos os testes definidos na classe
