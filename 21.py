#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que peça um número inteiro e determine se 
# ele é ou não um número primo. Um número primo é aquele que é divisível 
# somente por ele mesmo e por 1.

limpar()
print(" - Primo ou outro parente? -")
num=int(input("Digite um número inteiro: "))
divide=[] #inicializa a lista que armazenará os números divisíveis
for i in range(num, 1, -1): #ex: num=4; range(num, 1, -1)==4,3,2
    if num%i==0: #se a divisão for sem resto
        divide.append(i)

if len(divide) != 1: #se na lista existir mais números, significa que ele é divisível por outros além dele mesmo
    print('Não é primo')
else:
    print("É primo")
