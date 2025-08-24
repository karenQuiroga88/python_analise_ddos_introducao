palavra = "caio"
contador = 0
for letra in palavra :
  print(str(contador) + "-" + letra)
  contador = contador + 1


cidades = ['São Paulo','Guarulhos','Rio de Janeiro','Poá']
#print(cidades[0])

for cidade in cidades :
  print(cidade)

botaoExecutar = True
contador = 0
while botaoExecutar :
  print(contador)
  contador = contador + 1
  if contador >= 10 :
    botaoExecutar = False