"""
 11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 

 se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.
"""
aluno = input("Nome do Aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1+n2+n3+n4)/4

if media >= 7:
    print(f"O aluno {aluno} foi aprovado com média {media:.2f}")
else:
    print(f"O aluno {aluno} foi reprovado com média {media:.2f}")
