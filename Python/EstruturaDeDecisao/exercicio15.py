"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""


def check_triangle(side1, side2, side3):
    """Check if the sides form a triangle."""
    if side1 + side2 > side3:
        return True
    else:
        return False


def check_type_triangle(sides):
    """Check the type of the triangle."""
    counter = 0
    for side in sides:
        if side == sides[counter]:
            counter += 1
    if counter == 3:
        return"EQUILATERAL"
    elif counter == 0:
        return "ESCALENO"
    else:
        return "ISOSCELES"


if __name__ == '__main__':
    sides_list = []
    for x in range(3):
        sides_list.append(input(f"Enter the {x + 1}st side of the triangle: "))
    if check_triangle(*sides_list):
        print("FORM A TRIANGLE!")
        print(f"The triangle is: {check_type_triangle(sides_list)}")
    else:
        print("NOT FORM A TRIANGLE!")
