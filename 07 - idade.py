executar = True
while executar :
  anoNasci = int(input('Em que ano você nasceu?'))
  anoAtual = int(input('Em que ano estamos?'))
  idade = anoAtual - anoNasci
  print('Você tem:' + str(idade) + ' anos')
  opcao = input('\nDeseja testar novamente? \nSim ou não?')
  if opcao == "Não" or "N" or "Nao":
    executar = False


### outra forma
from datetime import date
executar = True 
while executar: 
    anoNasc = int(input('Em que ano você nasceu?'))
    anoAtual = date.today().year
    idade = anoAtual - anoNasc 
    print ('Você tem: ' + str(idade) + 'anos')

    while True: 
        opcao = input('\nDeseja testar novamente? (Sim ou Não)')
        if opcao in ['Sim', 'sim']:
            executar = True
            break
        if opcao in ['Não', 'n', 'não']:
            executar = False
            break 
