#coding: UTF-8
import os

def limpar(): 
	os.system("clear" or "cls")

#QUESTÃO: Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

limpar()
print(" - Cadastro -")
while True: #essa é uma estrutura que aprendi com meu professor. Criar um laço infinito e uni-lo a um if para parar (break) ele.
    print("Informa corretamente as informações abaixo")
    nome = input("Nome: ") #recebe o nome do usuário
    idade = int(input("Idade: ")) #recebe a idade do usuário
    sal = float(input("Salário: R$ ")) #recebe o salário do usuário
    print("\n[f] - Feminino")
    print("[m] - Masculino")
    sexo = input("Sexo: ") #recebe o sexo do usuário
    print("\n[s] - Solteiro(a)")
    print("[c] - Casado(a)")
    print("[v] - Viúvo(a)")
    print("[d] - Divorciado(a)")
    estadoC = input("Estado civil: ") #recebe estado civil do usuário
    valido = True #inicializa a variável que vai confirmar se as informações dadas são válidas. ver linha 47
    if len(nome) < 3:
        valido = False #se o nome tiver menos que 3 letras, a variável "valido" recebe False
    elif idade < 0 or idade > 150:
        valido = False #se a idade não estiver no intervalo entre 0 e 150, a variável "valido" recebe False
    elif sal < 0:
        valido = False #se o salário digitado for um número negativo, a variável "valido" recebe False
    elif sexo.lower() != 'f' and sexo.lower() != 'm': #pega a variável 'sexo', transforma em letra minúscula e faz o teste
        valido = False #se for diferente de 'f' e 'm', a variável "valido" recebe False
    elif estadoC.lower() != 's' and estadoC.lower() != 'c' and \
         estadoC.lower() != 'v' and estadoC.lower() != 'd': #pega a variável 'estadoC', transforma em letra minúscula e faz o teste
        valido = False #se for diferente de 's', 'c', 'v' e 'd', a variável "valido" recebe False
    
    if valido:
        print("\nInformações armazenadas com sucesso!")
        break
    else:
        limpar()
        print("Alguma informação não foi digitada corretamente.\nVerifique o seguinte:")
        print("    Nome: maior que 3 caracteres;\n    Idade: entre 0 e 150;\n    Salário: maior que zero;")
        print("Tente novamente!\n")




