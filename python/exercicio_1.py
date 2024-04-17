"""
1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.
"""

# Lendo os valores
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

soma = A+B # somando A + B

print(f"SOMA DE A + B = {soma}") # imprimindo a soma de A + B

if soma < C: # condição if para verificar se a soma é menor que C
    print("a soma de A + B é menor que C")
