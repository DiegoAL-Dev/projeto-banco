import textwrap

def menu():
    """
    Exibe o menu principal de opções na tela e captura a escolha do usuário.
    Retorna:
        str: A letra correspondente à opção escolhida pelo usuário.
    """
    opcoes = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(textwrap.dedent(opcoes))

def depositar(saldo, valor, extrato, /):
    """
    Realiza a operação de depósito na conta.
    (Utiliza passagem de argumentos apenas por posição)
    
    Parâmetros:
        saldo (float): O saldo atual da conta.
        valor (float): O valor a ser depositado.
        extrato (str): O histórico de transações da conta.
        
    Retorna:
        tuple: Retorna o saldo atualizado e o extrato atualizado.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque, validando regras de limite, saldo e quantidade diária.
    (Utiliza passagem de argumentos apenas por nome)
    
    Parâmetros:
        saldo (float): O saldo atual da conta.
        valor (float): O valor solicitado para saque.
        extrato (str): O histórico de transações.
        limite (float): O valor máximo permitido por saque.
        numero_saques (int): A quantidade de saques já realizados no dia.
        limite_saques (int): A quantidade máxima de saques permitidos no dia.
        
    Retorna:
        tuple: Retorna o saldo atualizado, o extrato atualizado e o número de saques atualizado.
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite de R$ 500,00. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de 3 saques diários excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o histórico de todas as transações realizadas e o saldo atual.
    (Utiliza passagem mista: saldo por posição, extrato por nome)
    
    Parâmetros:
        saldo (float): O saldo atual da conta.
        extrato (str): O histórico em texto das transações.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual:\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    """
    Função principal que inicializa as variáveis de controle e mantém o loop 
    de execução do programa (menu interativo) até que o usuário decida sair.
    """
    LIMITE_SAQUES = 3
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Gatilho que garante que o código principal (main) só seja executado 
# se o arquivo for rodado diretamente (e não importado como módulo).
if __name__ == "__main__":
    main()