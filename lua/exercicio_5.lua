--[[
5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse 

usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).
]]

local salario_minimo = 1293.20

print("Digite o salário do usuário")
salario_usuario = io.read("*n")

quant = 0
condicao = true

if salario_usuario > salario_minimo then
    while condicao do
        quant = quant + 1
        salario_usuario = salario_usuario - salario_minimo
        
        if salario_usuario < salario_minimo then
            print("Quantidade de salários minimos: "..quant.."")
            condicao = false
        end
    end
else
    print("O salário do usuário é menor que um salário minimo")
end