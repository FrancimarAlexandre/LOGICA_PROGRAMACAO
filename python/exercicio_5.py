"""
5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse 

usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).
"""
salario_minimo = 1293.20
salario_usuario = float(input("digite seu salário: "))
quant = 0
condicao = True
if salario_usuario > salario_minimo:    
    while condicao:
        quant +=1
        salario_usuario = salario_usuario - salario_minimo

        if salario_usuario < salario_minimo:
            print(f"quantidade salários minimos: {quant}")
            condicao =  False
else:
    print(f"o salário do usuário é menor que um salário minimo")
        
