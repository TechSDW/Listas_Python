# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido

nota = int(input("Digite uma nota entre 0 a 10: "))

while nota < 0 or nota > 10:
    print ("Nota inválida, tente novamente")
    nota = int(input("Digite uma nota entre 0 a 10: "))

print ("Essa nota é válida")

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

Nome = input ("Digite o nome de usuário: ")
Senha = input ("Digite sua senha: ")

while Nome == Senha:
    print ("Senha inválida, não coloque o nome de usuário igual à senha, tente novamente")
    Nome = input ("Digite o nome de usuário: ")
    Senha = input ("Digite sua senha: ")

print ("Dados aceitos.")

# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento

A = 80000
B = 200000
anos = 0

while A <= B:
    A = A + A * 3 / 100
    B = B + B * 1.5 / 100
    anos = anos + 1

print (f"Levou {anos} anos para a cidade A se equivaler com a cidade B")

# A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc

pos = int(input("Digite um número: "))
x = 2
pos1 = 1
pos2 = 1

if pos == 1 or pos == 2:
    print ("Seu número na sequência de Fibonacci é 1")

else:
    while x != pos:

        y = pos1 + pos2

        pos1 = pos2
        pos2 = y

        x = x + 1

    print (f"Seu número na sequência de Fibonacci é {y}")

# Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
dividendo = 0
divisor = 0

if n1 > n2:
    dividendo = n1
    divisor = n2
    resto = n1 % n2

else:
    dividendo = n2
    divisor = n1
    resto = n2 % n1

while resto != 0:
    dividendo = divisor
    divisor = resto
    resto = dividendo % divisor

print (f"O MDC é {divisor}")