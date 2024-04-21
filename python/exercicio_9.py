"""
9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição 

de acordo com a tabela abaixo:

Fórmula do IMC = peso / (altura) ²

Tabela Condições IMC

  

 Abaixo de 18,5   | Abaixo do peso          

 Entre 18,6 e 24,9 | Peso ideal (parabéns)  

 Entre 25,0 e 29,9 | Levemente acima do peso

 Entre 30,0 e 34,9 | Obesidade grau I 

 Entre 35,0 e 39,9 | Obesidade grau II (severa)

 Maior ou igual a 40 | Obesidade grau III (mórbida)
"""

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso/altura**2
print(f"Seu IMC -> {IMC:.2f}")
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC >= 18.6 and IMC <= 24.9:
    print("Peso ideal (parabéns)")
elif IMC >= 25 and  IMC <= 29.9:
     print("Levemente acima do peso")
elif IMC >= 30 and IMC <= 34.9:
    print("Obesidade grau I")
elif IMC >= 35 and IMC <= 39.9:
    print("Obesidade grau II (severa)")
elif IMC >= 40:
    print("Obesidade grau III (móbida)")