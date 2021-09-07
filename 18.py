#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dos valores.

limpar()
print(" - Menor, Maior, SOMA! -")
menor = 90000000000000000000000000000000000000000000000000000000000000000000 
#para que o programa funcione bem, menor recebe um valor bem alto e maior um bem baixo
maior = -90000000000000000000000000000000000000000000000000000000000000000000 
while True:
    num = float(input("Número: ")) #recebe um número
    #testa se é o maior digitado
    if num > maior:
        maior = num
    #testa se é o menor já digitado
    elif num < menor:
        menor = num
    #pergunta se quer digitar outro número
    opc = input("Infome pelo menos 2 números\nQuer digitar outro número? (S/n) ")
    if opc.lower() == 'n':
        break
print(f"\nO menor número informado foi {menor},")
print(f"O maior número informado foi {maior},")
print(f"E a soma entre eles é {maior + menor}")