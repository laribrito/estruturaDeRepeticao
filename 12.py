#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer 
# número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja 
# ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    # Tabuada de 5:
    # 5 X 1 = 5
    # 5 X 2 = 10
    # ...
    # 5 X 10 = 50

limpar()
print(" - Tabuada de 1 a 10 -")
num = int(input("Digite um número: ")) #recebe o número da tabuada
if num <1 or num>10: #verifica se o número está fora do intervalo 1 a 10 
    #sendo esse o caso, o programa não mostra a tabela
    print("Informação inválida! Tente novamente.")
else: 
    limpar()
    print(f"Para o número {num}, a tabuada é a seguinte:")
    x = 1 #inicia um contador
    while x<=10:
        print(f"{num} x {x} = {num*x}") #exibe uma linha da tabela
        x+=1 #incrementador