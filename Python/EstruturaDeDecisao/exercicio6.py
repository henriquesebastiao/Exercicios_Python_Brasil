"""
Faça um Programa que leia três números e mostre o maior deles.
"""


def numero_maior(*numeros):
    return max(numeros)


if __name__ == "__main__":
    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))
    numero3 = float(input("Informe o terceiro número: "))

    print(f"O maior número é: {numero_maior(numero1, numero2, numero3)}")
