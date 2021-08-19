#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

x=1 #inicializa o contador
limpar()
while x<=50: 
    print(x, end=", ") # exibe o número
    #como já temos o intervalo definido, para imprimir os números ímpares 
    # vou incrementar de 2 em 2
    x+=2
#linha puramente estética
print("\b\b.")
    