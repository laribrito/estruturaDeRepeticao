#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que calcule o fatorial de um número inteiro 
# fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

limpar()
print(" - Fatorial! -")
num = int(input("Um número inteiro para ser fatoriado: "))
print(f"{num}!", end=" = ")
somador = 1 #variável que vai armazenar o resultado do fatorial
while num>=1:
    print(f"{num}", end=" x ")
    somador *= num 
    num -= 1
print(f"\b\b= {somador}.")