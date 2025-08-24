class Carro:
    def __init__(self, modelo, cor):
        # Atributos do carro
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0  # O carro começa parado

    def acelerar(self, incremento):
        """Acelera o carro, aumentando a velocidade."""
        self.velocidade += incremento
        print(f"O carro {self.modelo} acelerou para {self.velocidade} km/h.")

    def parar(self):
        """Para o carro, deixando a velocidade igual a 0."""
        self.velocidade = 0
        print(f"O carro {self.modelo} parou.")

# Criando um objeto carro
meu_carro = Carro("Fusca", "Amarelo")

# Usando os métodos
meu_carro.acelerar(20)  # Acelera o carro para 20 km/h
meu_carro.acelerar(30)  # Acelera o carro para 50 km/h
meu_carro.parar()       # Para o carro
