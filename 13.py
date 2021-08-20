#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que peça dois números, base e expoente, 
# calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.

limpar()
print(" - Potencialização facilitada -")
b = int(input("Base: ")) #recebe a base 
e = int(input("Expoente: ")) #recebe o expoente
expo = e #guarda o expoente para exibição no final
acumulador = 1 #inicializa a variável "acumulador", que armazenará o resultado das potenciações
while e>=1: #esse while será regressivo. Portanto, esse código só aceitará expoentes positivos
    acumulador *= b #realiza a multiplicação
    e-=1 #decrementador 
print(f"{b} elevado a {expo} é igual a {acumulador}")