"""
17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.

Fórmula: C = (5 * ( F-32) / 9)
"""

F = float(input("Temperatura em Fahrenheit: "))

C = (5* (F-32)/9)

print(f"A temperatura em Fahrenheit {F} convertida para celsius {C:.2f}")