"""Aula 04 - Estruturas condicionais (if / elif / else) e while.

Operadores relacionais (o resultado é sempre True ou False):
    >   maior            <   menor
    >=  maior ou igual   <=  menor ou igual
    ==  igual            !=  diferente
"""


def situacao_aluno(nota, frequencia):
    """Aprovado se nota >= 60 e frequência >= 75."""
    if nota >= 60 and frequencia >= 75:
        return "Aprovado"
    return "Reprovado"


def sacar(saldo, valor):
    """Retorna (novo_saldo, mensagem). O saque é permitido até o valor do saldo."""
    if valor <= saldo:
        return saldo - valor, "Saque realizado!"
    return saldo, "Saldo insuficiente para saque"


def situacao_com_recuperacao(nota):
    """nota >= 60: aprovado | 40 <= nota < 60: recuperação | nota < 40: reprovado."""
    if nota >= 60:
        return "Aprovado"
    if nota >= 40:
        return "Recuperação"
    return "Reprovado"


def conceito(n1, n2):
    """Conceito pela média: A (>= 9), B (>= 7), C (>= 5), D (< 5)."""
    media = (n1 + n2) / 2
    if media >= 9:
        return "A"
    if media >= 7:
        return "B"
    if media >= 5:
        return "C"
    return "D"


def menu_caixa():
    """Simulador de caixa eletrônico: repete até o usuário escolher 1, 2 ou 3."""
    print("MENU:")
    print("[ 1 ] Consultar saldo")
    print("[ 2 ] Fazer depósito")
    print("[ 3 ] Sair")

    opcao = 0
    while opcao < 1 or opcao > 3:
        try:
            opcao = int(input("\nDigite o número da opção correspondente: "))
        except ValueError:
            opcao = 0
        if opcao == 1:
            print("Acessando sua conta... Seu saldo atual é de R$ 1.500,00.")
        elif opcao == 2:
            print("Iniciando depósito... Por favor, insira as notas no compartimento indicado.")
        elif opcao == 3:
            print("Sessão encerrada. Retire o seu cartão e tenha um bom dia!")
        else:
            print("Erro: Opção inválida! Por favor, escolha um número de 1 a 3.")


if __name__ == "__main__":
    nota = float(input("Informe a nota: "))
    frequencia = float(input("Informe a frequencia: "))
    print(situacao_aluno(nota, frequencia))

    saldo = 5000.50
    valor = float(input("Informe o valor do saque: "))
    saldo, mensagem = sacar(saldo, valor)
    print(mensagem)
    print("Saldo disponível: ", saldo)

    print(situacao_com_recuperacao(float(input("Informe a nota: "))))

    n1 = float(input("Informe a nota 1: "))
    n2 = float(input("Informe a nota 2: "))
    print("Conceito", conceito(n1, n2))

    menu_caixa()
