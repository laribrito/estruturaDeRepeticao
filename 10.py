#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que receba dois números inteiros e gere 
# os números inteiros que estão no intervalo compreendido por eles.

limpar()
num1 = int(input("Digite um número: ")) #recebe o primeiro número
num2 = int(input("Digite outro número: ")) #recebe o segundo número
#identifica o menor número
if num1 < num2:
    x=num1 # e guarda o menor número na variável "x"
    y=num2
else: 
    x= num2
    y=num1

#dessa forma, ele sempre vai fazer a contagem progressiva
print("Há esses números entre eles:")
while x<=y:
    print(x, end=", ")
    x+=1
print("\b\b.")