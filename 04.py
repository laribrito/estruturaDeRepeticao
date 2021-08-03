#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Supondo que a população de um país A seja da ordem de 80000 habitantes 
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
# e escreva o número de anos necessários para que a população do país A ultrapasse 
# ou iguale a população do país B, mantidas as taxas de crescimento.

limpar()
#algumas constantes
#dessa forma, fica fácil mudar esses dados, pensando na praticidade
POP_A = 80000       #população do país A
POP_B = 200000      #população do país B
CRESC_A = 0.030     #taxa de crescimento do país A
CRESC_B = 0.015     #taxa de crescimento do país B

#INICIO 
print(" - Calculo populacional -")
print(f"""Para a seguinte situação:
    País A: {POP_A}
    Sua taxa de crescimento populacional: {CRESC_A*100}%/ano
    País B: {POP_B}
    Sua taxa de crescimento populacional: {CRESC_B*100}%/ano
""")
novaPopA = POP_A + (POP_A*CRESC_A)  #calcula nova população do país A
novaPopB = POP_B + (POP_B*CRESC_B)  #calcula nova população do país B
x = 1 #insere a variável 'x' como um contador
while novaPopA <= novaPopB: #enquanto as populações forem diferentes...
    x += 1 #incrementa contador
    #calcula novamente as populações
    novaPopA = novaPopA + (novaPopA*CRESC_A) 
    novaPopB = novaPopB + (novaPopB*CRESC_B)
#quando sair do laço, o contador será igual aos anos necessários...
print(f"Serão necessários {x} anos para a população de A ultrapassar ou se igualar à população B.")
