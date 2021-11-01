#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Altere o programa de cálculo do fatorial, permitindo ao usuário 
# calcular o fatorial várias vezes e limitando o fatorial a números inteiros 
# positivos e menores que 16.

def teste(num):
    if 16 < num > 0 :
        valido=True
    else:
        valido=False
    return valido

limpar()
print(" - Fatorial! -")
while True:
    num = int(input("Um número inteiro para ser fatoriado: "))
    if teste(num):
        print("Número inválido.\nAceita-se somente positivos menores que 16.\n")
    else:
        print(f"{num}!", end=" = ")
        somador = 1 #variável que vai armazenar o resultado do fatorial
        while num>=1:
            print(f"{num}", end=" x ")
            somador *= num 
            num -= 1
        print(f"\b\b= {somador}.")
    opc=input("Deseja repetir a operação? (S/n) ")
    if opc.lower()=="n":
        break
    else:
        pass
