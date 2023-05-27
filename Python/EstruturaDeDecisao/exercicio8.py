"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""


def produto_mais_barato(*produtos):
    return min(produtos)


if __name__ == "__main__":
    produto1 = float(input("Informe o preço do primeiro produto: "))
    produto2 = float(input("Informe o preço do segundo produto: "))
    produto3 = float(input("Informe o preço do terceiro produto: "))

    print(f"O produto mais barato é: {produto_mais_barato(produto1, produto2, produto3)}")
