"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""


def ordem_decrescente(*numeros):
    return sorted(numeros, reverse=True)


if __name__ == "__main__":
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    numero3 = int(input("Informe o terceiro número: "))

    print(f"Números em ordem decrescente: {ordem_decrescente(numero1, numero2, numero3)}")
