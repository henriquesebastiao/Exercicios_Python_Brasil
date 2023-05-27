"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""


def verifica_maior(*numeros):
    return max(numeros)


def verifica_menor(*numeros):
    return min(numeros)


if __name__ == "__main__":
    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))
    numero3 = float(input("Informe o terceiro número: "))

    print(f"O maior número é: {verifica_maior(numero1, numero2, numero3)}")
    print(f"O menor número é: {verifica_menor(numero1, numero2, numero3)}")
