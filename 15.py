#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

limpar()
print(" - Sequência de Fibonacci -")
cont = int(input("Número 'n' de termos: ")) #recebe o contador do usuário
x = 0
a = 1 #primeiro termo da sequência
b = 0 #termo anterior
while x<cont:
    print(a, end=", ") 
    c = a #armazena o termo anterior em uma variável auxiliar
    a += b #soma o atual com o anterior
    b = c #b recebe o termo anterior
    x+=1
print("\b\b.")#escreve um ponto final 