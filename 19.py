#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

def teste(num):
    if num <0 or num >1000:
        valido = False
    else:
        valido =True
    return valido

limpar()
print(" - Menor, Maior, SOMA! -")
menor = 90000000000000000000000000000000000000000000000000000000000000000000 
#para que o programa funcione bem, menor recebe um valor bem alto e maior um bem baixo
maior = -0.90000000000000000000000000000000000000000000000000000000000000000000 
while True:
    num = float(input("Número: ")) #recebe um número
    #primeiramente, testa se esta no intervalo correto
    valido=teste(num)
    if valido:
        #testa se é o maior digitado
        if num > maior:
            maior = num
        #testa se é o menor já digitado
        elif num < menor:
            menor = num
        #pergunta se quer digitar outro número
    else:
        print("Número inválido!\nAceita-se somente entre 0 e 1000.\n")
    opc = input("Infome pelo menos 2 números\nQuer digitar outro número? (S/n) ")
    if opc.lower() == 'n':
        break
print(f"\nO menor número informado foi {menor},")
print(f"O maior número informado foi {maior},")
print(f"E a soma entre eles é {maior + menor}")