def minhaFuncao() :
  print("Hello Clarify")

minhaFuncao()
minhaFuncao()

cidades = ['São Paulo','Guarulhos','Rio de Janeiro','Poá']
contador = 0

def minhaFuncaoMelhorada(informacao,x) :
  print(str(x) + ' - ' + informacao)

for cidade in cidades :
  contador = contador + 1
  minhaFuncaoMelhorada(cidade , contador)