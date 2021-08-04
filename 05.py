#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Altere o programa anterior permitindo ao usuário informar 
# as populações e as taxas de crescimento iniciais. Valide a entrada 
# e permita repetir a operação.

while True:
    limpar()
    #INICIO 
    print("                 - Calculo populacional -")
    print("* Quantos anos demorá para um país ultrapassar o outro? *")
    a = float(input("População do país I: "))     #recebe a população do primeiro país
    b = float(input("População do país II: "))     #recebe a população do segundo país
    crescA = float(input("Taxa de crescimento anual do país I (%): "))   #recebe a taxa de crescimento do país A
    crescB = float(input("Taxa de crescimento anual do país II (%): "))   #recebe a taxa de crescimento do país B

    #validar as informações

    #como, no programa anterior, POP_A recebe a menor população, esse programa segue a mesma lógica
    # Portanto, o menor valor entre as variáveis 'a' e 'b' inicializará POP_A. 
    # as taxas de crescimento (crescA e crescB) também estão inseridas nesse IF
    if a < b:
        POP_A = a
        POP_B = b
        CRESC_A = crescA
        CRESC_B = crescB
    else:
        POP_A = b
        POP_B = a
        CRESC_A = crescB
        CRESC_B = crescA

    #transforma as % em números decimais para permitir os cálculos
    CRESC_A = CRESC_A / 100 
    CRESC_B = CRESC_B / 100 

    valido = True #inicializa a variável que vai confirmar se as informações dadas são válidas. 
    if POP_A <= 0 or POP_B <= 0 or CRESC_A <= 0 or CRESC_B <= 0:
        valido = False #se algum valor for negativo ou igual a zero, a variável "valido" recebe False

    if valido:
        limpar()
        print(f"""Para a seguinte situação:
            \b\b\b\bPaís A: {POP_A}
            \b\b\b\bSua taxa de crescimento populacional: {CRESC_A*100}%/ano
            \b\b\b\bPaís B: {POP_B}
            \b\b\b\bSua taxa de crescimento populacional: {CRESC_B*100}%/ano
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
        op = input("\nRodar o programa novamente? (S/n) ") #pergunta se deseja repetir a operação
        if op.lower() == "n":
            break
    else:
        print("Informações inválidas. Tente novamente!")
        break
