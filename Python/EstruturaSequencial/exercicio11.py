"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

A) O produto do dobro do primeiro com metade do segundo.
B) A soma do triplo do primeiro com o terceiro.
C) O terceiro elevado ao cubo.
"""

numero1 = int(input("Informe um número inteiro: "))
numero2 = int(input("Informe mais um número inteiro: "))
numero3 = float(input("Agora informe um número real: "))

print(f"A = {(2 * numero1) * (numero2 / 2)}")
print(f"B = {numero1 * 3 + numero3}")
print(f"C = {numero3 ** 3}")
