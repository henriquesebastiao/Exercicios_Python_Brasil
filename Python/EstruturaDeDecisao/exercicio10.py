"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""


def saudacao(turno):
    if turno == "M":
        return "Bom Dia!"
    elif turno == "V":
        return "Boa Tarde!"
    elif turno == "N":
        return "Boa Noite!"
    else:
        return "Valor Inválido!"


if __name__ == "__main__":
    print("M - Matutino")
    print("V - Vespertino")
    print("N - Noturno")
    turno_selecionado = input("Informe o seu turno: ")

    print(saudacao(turno_selecionado))
