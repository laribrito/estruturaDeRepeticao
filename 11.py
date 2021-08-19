#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Altere o programa anterior para mostrar no final a soma dos números.

limpar()
somador = 0 #inicializa o somador
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
    print(x, end=", ") #exibe os números
    somador += x #soma o número atual com os já armazenados
    x+=1 #incrementa
print("\b\b.") #minha famosa linha puramente estética
print(f"A soma de todos esse números é igual a {somador}.")