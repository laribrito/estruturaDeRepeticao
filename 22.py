#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Altere o programa de cálculo dos números primos, informando, 
# caso o número não seja primo, por quais número ele é divisível.

limpar()
print(" - Primo ou outro parente? -")
num=int(input("Digite um número inteiro: "))
divide=[] #inicializa a lista que armazenará os números divisíveis
for i in range(num, 1, -1): #ex: num=4; range(num, 1, -1)==4,3,2
    if num%i==0: #se a divisão for sem resto
        divide.append(i)

if len(divide) != 1: #se na lista existir mais números, significa que ele é divisível por outros além dele mesmo
    print('Não é primo')
    print("Ele é divisível por ", end="")
    for i in divide:
        print(f"{i}", end=", ")
    print("\b\b.")
else:
    print("É primo")
