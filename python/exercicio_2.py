"""
2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.
"""

num = int(input("Digite um número qualquer: "))

if num % 2 == 0:
    if num >= 0:
        print("o número é par e positivo")
    else:
        print("o número é par e negativo")
else:
    if num >= 0:
        print("o número é ímpar e positivo")
    else:
        print("o número é ímpar e negativo")