"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""


def converte_fahrenheit_para_celsius(graus_fahrenheit):
    return 5 * ((graus_fahrenheit - 32) / 9)


fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))
print(f"{fahrenheit} graus Fahrenheit equivalem à {converte_fahrenheit_para_celsius(fahrenheit)} graus Celsius.")
