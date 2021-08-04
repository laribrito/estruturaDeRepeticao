#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que imprima na tela os números de 1 a 20, 
# um abaixo do outro. Depois modifique o programa para que ele 
# mostre os números um ao lado do outro.

while True:
    limpar()
    op = int(input("Digite 1 ou 2: ")) #recebe um número
    if op == 1:
        #se for digitado '1', números em baixo um do outro
        for i in range(1,21):
            print(i)
        break
    elif op == 2:
        #se for digitado '2', números do lado um do outro
        for i in range(1,21):
            print(i, end=", ")
        print("\b\b.") #puramente por estética. Apaga a vírgula que ficaria depois do último número e escreve um ponto
        break
    else:
        #se for digitado outro número o programa para
        print("Número errado. Tente novamente!")