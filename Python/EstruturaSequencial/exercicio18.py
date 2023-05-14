"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""


def calcular_tempo(tamanho, velocidade):
    """Calcula o tempo aproximado de download de um arquivo em minutos."""
    tempo_download = ((tamanho_arquivo * 8) / velocidade_link) / 60
    return f"Tempo aproximado de download: {tempo_download:.1f} minutos"


if __name__ == '__main__':
    tamanho_arquivo = float(input("Informe o tamanho do arquivo em MB: "))
    velocidade_link = float(input("Informe a velocidade da sua internet em Mbps: "))

    print(calcular_tempo(tamanho_arquivo, velocidade_link))
