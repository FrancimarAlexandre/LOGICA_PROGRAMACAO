--[[
1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.
]]

-- Lendo os valores
print("Digite o calor de A")
local A = io.read("*n")

print("Digite o calor de B")
local B = io.read("*n")

print("Digite o calor de C")
local C = io.read("*n")

local soma = A + B

print("SOMA DE A + B = "..soma.."")

if soma < C then
    print("a soma de A + B é menor que C")
end