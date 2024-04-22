"""
16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é 

equilátero, isósceles ou escaleno.
"""
v1 = int(input("Lado 1 do triângulo: "))
v2 = int(input("Lado 2 do triângulo: "))
v3 = int(input("Lado 3 do triângulo: "))

if v1 < v2 + v3 and v2 < v1+ v3 and v3 < v1+ v2:
    if v1+v2 == v2+v3 == v3+v1:
        print("É um triângulo equilátero")
    elif v1 == v2 or v2 == v3 or v1 == v3:
        print("É um triângulo isóceles")
    elif v1 != v2 and v1 != v3 and v2 != v3:
        print("É um triângulo escaleno")