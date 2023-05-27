"""
Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""


def calcula_media(nota1, nota2, nota3):
    """
    Função que calcula a média de três notas

    :param nota1: primeira nota
    :param nota2: segunda nota
    :param nota3: terceira nota
    :return: média das três notas
    """
    return (nota1 + nota2 + nota3) / 3


def verifica_aprovacao(nota1, nota2, nota3):
    """
    Função que verifica se um aluno foi aprovado ou não

    :param nota1: primeira nota
    :param nota2: segunda nota
    :param nota3: terceira nota
    :return: "Aprovado" se a média for maior ou igual a 7, "Reprovado" se a média for menor que 7
    """
    media = calcula_media(nota1, nota2, nota3)
    if media >= 7:
        if media == 10:
            return "Aprovado com Distinção"
        else:
            return f"Aprovado com média {media}"
    else:
        return f"Reprovado com média {media}"


if __name__ == '__main__':
    nota1_informada = float(input("Nota 1: "))
    nota2_informada = float(input("Nota 2: "))
    nota3_informada = float(input("Nota 3: "))
    print(verifica_aprovacao(nota1_informada, nota2_informada, nota3_informada))
