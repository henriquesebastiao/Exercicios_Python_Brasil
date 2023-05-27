"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101,
    311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""


def separa_numero(numero):
    if numero >= 100:
        centenas = numero // 100
        dezenas = (numero % 100) // 10
        unidades = (numero % 100) % 10
        return f'{numero} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades'
    elif 9 < numero < 100:
        dezenas = numero // 10
        unidades = numero % 10
        return f'{numero} = {dezenas} dezenas e {unidades} unidades'
    else:
        return f'{numero} unidades'


if __name__ == '__main__':
    print(separa_numero(326))
    print(separa_numero(300))
    print(separa_numero(100))
    print(separa_numero(320))
    print(separa_numero(310))
    print(separa_numero(305))
    print(separa_numero(301))
    print(separa_numero(101))
    print(separa_numero(311))
    print(separa_numero(111))
    print(separa_numero(25))
    print(separa_numero(20))
    print(separa_numero(10))
    print(separa_numero(21))
    print(separa_numero(11))
    print(separa_numero(1))
    print(separa_numero(7))
    print(separa_numero(16))
