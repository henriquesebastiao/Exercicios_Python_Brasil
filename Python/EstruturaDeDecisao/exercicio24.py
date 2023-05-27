"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    Par ou ímpar;
    Positivo ou negativo;
    Inteiro ou decimal.
"""


def realiza_operacao(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        return numero1 / numero2


def verifica_par_impar(numero):
    return "PAR" if numero % 2 == 0 else "ÍMPAR"


def verifica_positivo_negativo(numero):
    return "POSITIVO" if numero > 0 else "NEGATIVO"


def verifica_inteiro_decimal(numero):
    return "INTEIRO" if numero == round(numero) else "DECIMAL"


if __name__ == '__main__':
    numero1 = float(input("Número 1: "))
    numero2 = float(input("Número 2: "))
    operacao = input("Operação (+, -, *, /): ")
    resultado = realiza_operacao(numero1, numero2, operacao)
    print(f"Resultado: {resultado}")
    print(f"Par ou ímpar: {verifica_par_impar(resultado)}")
    print(f"Positivo ou negativo: {verifica_positivo_negativo(resultado)}")
    print(f"Inteiro ou decimal: {verifica_inteiro_decimal(resultado)}")