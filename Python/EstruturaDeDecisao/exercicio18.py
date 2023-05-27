"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""


def verifica_ano_bissexto(ano):
    """
    Função que verifica se um ano é bissexto

    :arg ano: ano a ser verificado
    :return: True se o ano for bissexto, False caso contrário
    """
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


def verifica_data_valida(dia, mes, ano):
    """
    Função que verifica se uma data é válida

    :param dia: dia a ser verificado
    :param mes: mês a ser verificado
    :param ano: ano a ser verificado
    :return: True se a data for válida, False caso contrário
    """
    meses = {
        '01': 31,
        '02': 28,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }
    if int(ano) < 0:  # Ano negativo retorna False
        return False
    else:
        if verifica_ano_bissexto(int(ano)):  # Se o ano for bissexto, o mês de fevereiro tem 29 dias
            meses['02'] = 29
        if 0 >= int(mes) > 12:  # Mês inválido retorna False (meses válidos: 1-12)
            return False
        else:
            if 0 <= int(dia) > 31:  # Dia inválido retorna False (dias válidos: 1-31)
                return False
            else:
                if int(dia) <= meses[mes]:  # Se o dia for menor ou igual ao número de dias do mês, retorna True
                    return True
                else:
                    return False


if __name__ == '__main__':
    data = input("Informe uma data (dd/mm/aaa): ").split('/')  # Recebe a data e separa em dia, mês e ano
    if verifica_data_valida(*data):
        print('VÁLIDA')
    else:
        print('INVÁLIDA')
