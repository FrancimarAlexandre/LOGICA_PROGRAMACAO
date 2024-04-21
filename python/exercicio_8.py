"""
8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.
"""

v1 = int(input("Valor 1: "))
v2 = int(input("Valor 2: "))
v3 = int(input("Valor 3: "))

if v1 == v2 or v2 == v3 or v1 == v3:
    print("os valores devem ser diferentes...")


dv1 =dv2=dv3 = None

if v1 > v2:
    dv1 = v1

    if v2 > v3:
        dv2 = v2
        dv3 = v3
    else:
        dv2 = v3
        dv3 = v2
elif v2 > v1:
    dv1 = v2

    if v1 > v3:
        dv2 = v1
        dv3 = v3
    else:
        dv2 = v3
        dv3 = v1
elif v3 > v1:
    dv1 = v3
    if v1 > v2:
        dv2 = v1
        dv3 = v2
    else:
        dv2 = v2
        dv3 = v1
print(f"A seguencia {v1},{v2} e {v3} de forma decrescente...{dv1},{dv2},{dv3}")