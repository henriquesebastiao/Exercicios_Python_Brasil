"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""


def verifica_vogal_consoante(letra):
    if len(letra) > 1:
        return "VOCÊ INFORMOU MAIS DO QUE UM CARACTERE!"
    elif letra in "AEIOU":
        return "A letra é um VOGAL."
    elif letra in "BCDFGHJKLMNPQRSTVWXYZ":
        return "A letra é uma CONSOANTE."
    else:
        return "CARACTERE INVÁLIDO!"


if __name__ == "__main__":
    letra_informada = input("Informe uma letra: ").upper()
    print(verifica_vogal_consoante(letra_informada))
