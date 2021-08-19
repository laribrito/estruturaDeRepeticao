#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que leia 5 números e informe a soma e a média dos números.

x=1 #inicializa o contador
somador=0 #inicializa a variável que vai armazenar a soma de todos os números
limpar()
#esse bloco vai se repetir 5 vezes
while x<=5: 
    num = int(input("Digite um número: ")) #recebe um número
    somador += num #soma na variável somador
    x+=1 #incrementa o contador

print(f"A soma de todos os números digitados foi {somador}")  #exibe a soma
media = somador/5#calcula a media
print(f"A respectiva média foi {media}") #exibe a média