"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
    porém não há limites para a quantidade de carne por cliente.
    Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
    Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
    contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
    valor do desconto e valor a pagar.
"""


class Compra:
    def __init__(self, tipo_de_carne, peso, metodo_de_pagamento):
        self.tipo_de_carne = tipo_de_carne
        self.peso = peso
        self.metodo_de_pagamento = metodo_de_pagamento

    def calcula_valor_total(self):
        if self.peso < 5:
            if self.tipo_de_carne == '1':
                return self.peso * 4.9
            elif self.tipo_de_carne == '2':
                return self.peso * 5.9
            else:
                return self.peso * 6.9
        else:
            if self.tipo_de_carne == '1':
                return self.peso * 5.8
            elif self.tipo_de_carne == '2':
                return self.peso * 6.8
            else:
                return self.peso * 7.8

    def calcula_desconto(self):
        valor_total = self.calcula_valor_total()
        if self.metodo_de_pagamento == 'Cartão Tabajara':
            return valor_total * 0.05
        else:
            return 0

    def calcula_valor_liquido(self):
        valor_total = self.calcula_valor_total()
        desconto = self.calcula_desconto()
        return valor_total - desconto

    def gera_cupom_fiscal(self):
        if self.metodo_de_pagamento == '1':
            self.metodo_de_pagamento = 'Cartão Tabajara'
        else:
            self.metodo_de_pagamento = 'Outros'

        if self.tipo_de_carne == '1':
            self.tipo_de_carne = 'Filé Duplo'
        elif self.tipo_de_carne == '2':
            self.tipo_de_carne = 'Alcatra'
        else:
            self.tipo_de_carne = 'Picanha'

        return f"""\nTipo de carne: \t{self.tipo_de_carne}
Quantidade: \t{self.peso:.2f} Kg
Preço total: \tR$ {self.calcula_valor_total():.2f}
Tipo de pagamento: \t{self.metodo_de_pagamento}
Desconto: \tR$ {self.calcula_desconto():.2f}
Valor líquido: \tR$ {self.calcula_valor_liquido():.2f}"""


if __name__ == '__main__':
    tipo_de_carne = input("""Tipo de carne:
[1] Filé Duplo
[2] Alcatra
[3] Picanha
Opção: """)
    peso = float(input("Quantidade (Kg): "))
    metodo_de_pagamento = input("""Método de pagamento:
[1] Cartão Tabajara
[2] Outros
Opção: """)
    compra = Compra(tipo_de_carne, peso, metodo_de_pagamento)
    print(compra.gera_cupom_fiscal())
