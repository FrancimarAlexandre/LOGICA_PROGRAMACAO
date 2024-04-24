--[[
3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, 

caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e

imprimir seu valor na tela.
]]

print("Digite o valor de A: ")
local A = io.read("*n")

print("Digite o valor de B: ")
local B = io.read("*n")

if A == B then
    C = A + B
else
    C = A * B
end

print("Resultados: "..C.."")