"""
Faça um Programa que peça um número correspondente a um determinado ano
e em seguida informe se este ano é ou não bissexto.
"""


def verifica_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    ano_informado = float(input("Ano: "))
    if verifica_ano_bissexto(ano_informado):
        print("BISSEXTO")
    else:
        print("NÃO BISSEXTO")
