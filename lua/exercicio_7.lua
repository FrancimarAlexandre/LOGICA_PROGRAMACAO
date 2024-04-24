--[[
    7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.
]]

local function stringToBoolean(str)
    if str:lower() == "true" then
        return true
    elseif str:lower() == "false" then
        return false
    else
        error("Entrada inválida. Por favor, digite 'True' ou 'False'.")
    end
end

-- Leitura dos valores booleanos
print("Digite o primeiro valor booleano (True/False): ")
local valor1 = stringToBoolean(io.read())
print("Digite o segundo valor booleano (True/False): ")
local valor2 = stringToBoolean(io.read())

-- Avaliação dos valores booleanos
if valor1 and valor2 then
    print("Ambos os valores são VERDADEIROS.")
elseif not valor1 and not valor2 then
    print("Ambos os valores são FALSOS.")
else
    print("Os valores são diferentes.")
end