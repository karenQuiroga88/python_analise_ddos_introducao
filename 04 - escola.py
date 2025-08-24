tipoEscola = input("Estuda em colegio: \n [1]Publico \n [2]Particular: \n")
mediaAluno = input("Qual a media do aluno?")
freqAluno = input("Qual a frequencia do aluno?")
mediaAluno = int(mediaAluno)
freqAluno = int(freqAluno)

# != diferente
# == igual
# <= menor ou igual
# >= maior ou igual
# > maior
# < menor

if tipoEscola == "2" :
  print("------- Colegio Particular --------")
  if mediaAluno >= 7 and freqAluno >= 70 :
    print("Aprovado")
  else :
    print("Reprovado")

if tipoEscola == "1" :
  print("-------- Colegio Publico --------")
  if mediaAluno >= 7 or freqAluno >= 70 :
    print("Aprovado")
  else :
    print("Reprovado")

print("fim")