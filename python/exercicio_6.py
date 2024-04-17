"""
6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.
"""

valor = float(input("informe um valor: "))

novo_valor = ((valor * 5)/100) + valor

print(novo_valor)