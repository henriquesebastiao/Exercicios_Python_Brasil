"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""


def verifica_modulo(numero):
    if numero >= 0:
        return "POSITIVO"
    else:
        return "NEGATIVO"


if __name__ == "__main__":
    numero_informado = float(input("Informe um número: "))
    print(verifica_modulo(numero_informado))
