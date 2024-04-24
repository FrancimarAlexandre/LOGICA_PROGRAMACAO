"""
18 - Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem 1,10m e cresce 3 centímetros por ano.
Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Francisco seja maior que Sara.
"""
altura_francisco = 150 # cm
altura_sara = 110 # cm

crescimento_ano_francisco = 2
crescimento_ano_sara = 3

anos = 0

while altura_sara <= altura_francisco:
    altura_francisco += crescimento_ano_francisco
    altura_sara += crescimento_ano_sara
    anos += 1
    
print(f"após {anos} anos Sara será maior que Francisco")