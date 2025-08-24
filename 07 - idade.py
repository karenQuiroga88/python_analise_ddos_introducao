executar = True
while executar :
  anoNasci = int(input('Em que ano você nasceu?'))
  anoAtual = int(input('Em que ano estamos?'))
  idade = anoAtual - anoNasci
  print('Você tem:' + str(idade) + ' anos')
  opcao = input('\nDeseja testar novamente? \nSim ou não?')
  if opcao == "Não" or "N" or "Nao":
    executar = False