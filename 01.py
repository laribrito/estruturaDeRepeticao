#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo 
# até que o usuário informe um valor válido.


limpar()
print(" - Acerte o valor -")
while True: #essa é uma estrutura que aprendi com meu professor. Criar um laço infinito e uni-lo a um if para parar (break) ele.
    num = float(input("Informe um número: ")) #recebe o número do usuário
    if num >= 0 and num <= 10: #testa se esta no intervalo pedido
        print("Parabéns! Você acertou o número!")
        break #e se for o caso, mostra uma mensagem de sucesso e para o laço
    else:
        print("Número errado. Tente novamente!") #se o teste retornar False, printa uma mensagem de erro e pede novamente um número





