"""
22 - Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela o quociente e o resto da divisão inteira entre eles.
"""

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if B != 0 : # verificando se B é diferente de 0
    quociente = A // B
    resto = A % B
    
    print(f"quociente = {quociente}\nresto = {resto}")
else:
    print("Erro! o valor de B não pode ser 0")