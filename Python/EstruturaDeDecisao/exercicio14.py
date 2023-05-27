"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
    se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""


def calcula_conceito(*notas):
    media = 0
    for nota in notas:
        media += nota
    media /= len(notas)
    if media < 4:
        return notas, media, "E", "REPROVADO"
    elif 4 <= media < 6:
        return notas, media, "D", "REPROVADO"
    elif 6 <= media < 7.5:
        return notas, media, "C", "APROVADO"
    elif 7.5 <= media < 9:
        return notas, media, "B", "APROVADO"
    else:
        return notas, media, "A", "APROVADO"


if __name__ == "__main__":
    conceito_henrique = calcula_conceito(5.2, 5.6)
    print(f'''Notas: {conceito_henrique[0]}
Média: {conceito_henrique[1]}
Conceito: {conceito_henrique[2]}
Resultado: {conceito_henrique[3]}''')
