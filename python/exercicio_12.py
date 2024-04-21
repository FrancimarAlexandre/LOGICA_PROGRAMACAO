"""
 12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento

 pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

  Tabela de Código de Condições de Pagamento

 
 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto

 2 - À Vista no cartão de crédito, recebe 10% de desconto

 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros

 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%
"""

valor_produto = float(input("Digite o valor do produto: "))

print("Formas de pagamento")
print("""
 1 - À Vista em Dinheiro ou Pix

 2 - À Vista no cartão de crédito

 3 - Parcelado no cartão em duas vezes

 4 - Parcelado no cartão em três vezes ou mais
""")
forma_pagamento = int(input("Escolha uma forma de pagamento: "))

if forma_pagamento == 1:
    valor_final = valor_produto-((valor_produto * 15)/100)
elif forma_pagamento == 2:
    valor_final = valor_produto-((valor_produto * 10)/100) 
elif forma_pagamento == 3:
    valor_final = valor_produto
elif forma_pagamento == 4:
        valor_final = ((valor_produto * 10)/100) + valor_produto

print(f"Valor final do produto {valor_final:.2f}")