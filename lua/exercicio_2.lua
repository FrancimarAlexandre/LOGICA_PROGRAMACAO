--[[
    2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.
]]

print("Digite um número inteiro qualquer: ")
local num = io.read("*n")

if num % 2 == 0 then
    if num >= 0 then
        print("O número é par e positivo")
    else
        print("O número é negativo")
    end
else
    if num >= 0 then
        print("O número é ímpar e positivo")
    else
        print("O número é ímpar e negativo")
    end
end
