"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""


def converte_celsius_para_fahrenheit(graus_celsius):
    return (graus_celsius * 9 / 5) + 32


celsius = float(input("Informe a temperatura em graus Celsius: "))
print(f"{celsius} graus Celsius equivalem à {converte_celsius_para_fahrenheit(celsius)} graus Fahrenheit.")
