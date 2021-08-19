#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que leia 5 números e informe o maior número.

x=1 #inicializa o contador
maior=0 #inicializa a variável que vai armazenar o maior valor
limpar()
#esse bloco vai se repetir 5 vezes
while x<=5: 
    num1 = int(input("Digite um número: ")) #recebe um número
    if num1 > maior: #se o número recebido for maior que o maior número já registrado...
        maior = num1 #maior recebe um novo valor
    #se o teste der negativo, nenhuma alteração precisa ser feita
    x+=1 #incrementa o contador

print(f"O maior número digitado foi {maior}")  #exibe o maior valor