"""
19 - Faça um algoritmo que imprima na tela a tabuada de 1 até 10.
"""

tabuada = 1

while tabuada <=10:
    for i in range(11):
        print(f"{tabuada}X{i} = {tabuada*i}\n")
    print("=-=-=-=-=-=-=-=-=-=-=-")
    tabuada += 1