"7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO."

# Leitura dos valores booleanos
valor1 = input("Digite o primeiro valor booleano (True/False): ")
valor2 = input("Digite o segundo valor booleano (True/False): ")

# Convertendo os valores de string para booleanos
"""
A comparação com 'true' retorna True se o valor inserido for "true"
 (independente do caso, maiúsculo ou minúsculo), e False para qualquer outra entrada.
"""
valor1 = valor1.strip().lower() == 'true' # strip() remove espaços extras do início e do fim da string.
valor2 = valor2.strip().lower() == 'true' # lower() converte a string para letras minúsculas.

# Verificando se ambos são verdadeiros ou ambos são falsos
if valor1 and valor2:
    print("Ambos os valores são VERDADEIROS.")
elif not valor1 and not valor2:
    print("Ambos os valores são FALSOS.")
else:
    print("Os valores são diferentes.")


