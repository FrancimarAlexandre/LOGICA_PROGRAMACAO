--[[
    4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor
]]

print("Digite um valor inteiro")
local num = io.read("*n")

print("Seu antecessor "..num - 1 .." e seu sucessor "..num + 1 .."")
