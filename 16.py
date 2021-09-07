#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

limpar()
print(" - Sequência de Fibonacci até o número 500 (ou maior que ele) -")
x = 0 #contador
a = 1 #primeiro termo da sequência
b = 0 #termo anterior
while b<500:
    print(a, end=", ") 
    c = a #armazena o termo anterior em uma variável auxiliar
    a += b #soma o atual com o anterior
    b = c #b recebe o termo anterior
    x+=1
print("\b\b.")#escreve um ponto final
print(f"Essa sequência tem {x} itens.")