def divisao(a, b):
    try:
        # Tentando dividir os dois números
        resultado = a / b
        print(f"O resultado da divisão de {a} por {b} é: {resultado}")
    except ZeroDivisionError:
        # Se houver um erro de divisão por zero, o código dentro do except é executado
        print("Erro: Não é possível dividir por zero.")
    except TypeError:
        # Caso os parâmetros fornecidos não sejam numéricos, o código dentro desse except será executado
        print("Erro: Ambos os valores devem ser números.")
    except Exception as e:
        # Captura qualquer outro tipo de exceção que não tenha sido tratada nos excepts anteriores
        print(f"Erro inesperado: {e}")
    else:
        # O bloco else é executado se o código dentro do try for bem-sucedido (sem erros)
        print("Divisão realizada com sucesso!")
    finally:
        # O bloco finally sempre será executado, independentemente de erro ou sucesso
        print("Processo de divisão concluído.")

# Teste 1: Divisão normal
divisao(10, 2)

# Teste 2: Divisão por zero
divisao(10, 0)

# Teste 3: Divisão com tipos inválidos
divisao(10, "dois")

# Teste 4: Divisão com erro inesperado
divisao("dez", 2)
