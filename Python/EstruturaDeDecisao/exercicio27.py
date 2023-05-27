"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
    receberá ainda um desconto de 10% sobre este total.
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
    de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""


def calcula_valor_liquido(peso_morangos, peso_macas):
    if peso_morangos < 5:
        valor_morangos = peso_morangos * 2.5
    else:
        valor_morangos = peso_morangos * 2.2

    if peso_macas < 5:
        valor_macas = peso_macas * 1.8
    else:
        valor_macas = peso_macas * 1.5

    valor_total = valor_macas + valor_morangos
    peso_total = peso_morangos + peso_macas

    if peso_total > 8 or valor_total > 25:
        valor_total *= 0.9

    return valor_total


if __name__ == '__main__':
    macas = float(input("Quantidade de maçãs (Kg): "))
    morangos = float(input("Quantidade de morangos (Kg): "))
    print(f'Valor a pagar: R$ {calcula_valor_liquido(morangos, macas):.2f}')
