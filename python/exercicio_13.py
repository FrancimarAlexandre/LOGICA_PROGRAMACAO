"""
 13 - Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Olá senho {nome} o senhor é maior de idade")
else:
    print(f"Olá jovem {nome} o senhor é menor de idade")
        