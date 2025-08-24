class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

# Usando polimorfismo
def fazer_animal_falar(animal: Animal):
    print(animal.fazer_som())

# Criando objetos
cachorro = Cachorro()
gato = Gato()

# Chama o método de cada animal de forma polimórfica
fazer_animal_falar(cachorro)  # Saída: Au au
fazer_animal_falar(gato)      # Saída: Miau
