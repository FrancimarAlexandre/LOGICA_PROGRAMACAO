"""
14 - Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e o valor de B por A e imprima na tela os valores.
"""

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

C = A
A = B
B = C

print(f"Novos valores de A = {A} e B = {B}")