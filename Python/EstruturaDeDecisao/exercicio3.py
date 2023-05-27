"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""


def verifica_sexo(sexo):
    if sexo == "F":
        return "F - Feminino"
    elif sexo == "M":
        return "M - Masculino"
    else:
        return "Sexo Inválido"


if __name__ == "__main__":
    sexo_informado = input('Informe o sexo ("M" ou "F"): ')
    print(verifica_sexo(sexo_informado.upper()))
