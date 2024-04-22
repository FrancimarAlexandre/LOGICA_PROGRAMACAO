"""
15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias essa pessoa ja viveu. Leve em 

consideração o ano com 365 dias e o mês com 30 dias.

(Ex: 5 anos, 2 meses e 15 dias de vida)
"""
import datetime # biblioteca para pegar a data atual

ano_nasc = int(input("Em que ano você nasceu: "))

ColAno = datetime.datetime.now()
ano = ColAno.year
mes = ColAno.month
dia = ColAno.day

if mes < 12 and dia <30:
    print(f"Você tem {ano - ano_nasc} anos, {mes} meses e {dia} dias de vida")