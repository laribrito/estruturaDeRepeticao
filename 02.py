#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que leia um nome de usuário e a sua senha 
# e não aceite a senha igual ao nome do usuário, mostrando uma mensagem 
# de erro e voltando a pedir as informações.


limpar()
print(" - Login -")
while True: #essa é uma estrutura que aprendi com meu professor. Criar um laço infinito e uni-lo a um if para parar (break) ele.
    user = input("Seu nome: ") #recebe o nome do usuário
    passw = input("Sua senha: ") #recebe a senha do usuário
    if user == passw: #testa se são iguais
        print("Nome e senha não podem ser iguais. Tente novamente.")
        #mostra uma mensagem de erro e deixa o while rodar
    else:
        print("Sucesso!")
        break 
        #as informações são diferente e por isso não é necessário perguntar novamente




