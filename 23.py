#coding: UTF-8
import limpa

#QUESTÃO: Faça um programa que mostre todos os primos entre 1 e N sendo N um número
# inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões 
# que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o 
# estilo e o número de testes (divisões) executados.

print(" - Cadê os primos? -")
num=int(input("Digite um número inteiro: "))
#variável auxiliar
x = num
#contador de divisores
divisor = 0
#lista para os divisores
divisores =[]
#estado do número
primo = True
while x>=1:
    if num%x==0:
        divisores.append(x)
        divisor += 1

    if divisor>3:
        #se mais de 1 divisor for encontrado não é primo
        primo = False
        break
    x-=1
if primo:
    print(f"{num} é um número primo")
else:
    print(f"{num} é um número composto")
    print(f"{divisor} divisores")
    print(divisores)