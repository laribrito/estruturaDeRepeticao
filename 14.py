#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que peça 10 números inteiros, calcule 
# e mostre a quantidade de números pares e a quantidade de números impares.

limpar()
print(" - Quantos ímpares? -")
x = 1 #inicializa o contador
#inciailiza as variáveis que irão armazenar a quantidade de números pares e impares
par = 0 
impar = 0
while x<=10: #10 vezes
    num = float(input("Número: ")) #recebe o número
    #ANOTAÇÃO IMPORTANTE
    # print(num % 2) resto
    # print(num // 2) divisão inteira
    if num % 2 == 0:
        par +=1
    else:
        impar +=1
    x+=1
print(f"Houveram {par} números pares e {impar} números ímpares.")