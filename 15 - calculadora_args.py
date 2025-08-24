class Calculadora:
    def somar(self, *args):
        return sum(args)

calc = Calculadora()

# Pode passar qualquer número de argumentos
print(calc.somar(1, 2))            # Saída: 3
print(calc.somar(1, 2, 3, 4, 5))   # Saída: 15
