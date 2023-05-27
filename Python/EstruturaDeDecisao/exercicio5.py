"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""


def verifica_aprovacao(*notas):
    media = 0
    for nota in notas:
        media += nota
    media = media / notas.__len__()

    if media >= 7 and media != 10:
        return "APROVADO"
    elif media < 7:
        return "REPROVADO"
    else:
        return "Aprovado com DISTINÇÃO"


if __name__ == "__main__":
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))

    print(verifica_aprovacao(nota1, nota2))
