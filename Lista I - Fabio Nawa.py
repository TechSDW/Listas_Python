#Faça um programa que peça dois números inteiros e imprima a soma desses dois números

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print ("A soma dos números é igual a", (a+b))

#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

c = float(input("Digite um número em metros: "))

print ((c),"m é igual a",(c*1000),"mm")

#Escreva um programa que leia a quantidade de dias, horas,minutos e segundos do usuário. Calcule o total em segundos

d = int(input("Digite a quantidade de horas: "))
e = int(input("Digite a quantidade de minutos: "))
f = int(input("Digite a quantidade de segundos: "))

print ("O total de segundos é:",(f+e*60+d*3600))

#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário

g = float(input("Digite seu salário: "))
h = float(input("Digite seu aumento: "))

print ("Seu novo salário é:", (g+g*h/100))

#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a paga

i = float(input("Digite o preço do produto: "))
j = float(input("Digite o desconto recebido: "))

print ("Comprará o produto por:",(i-i*j/100), ", com um desconto de:", (i*j/100))

#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem

k = float(input("Digite a distância percorrida (km): "))
l = float(input("Digite a velocidade média (km/h): "))

print ("Irá demorar", (k/l), 'horas para chegar')

#Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

m = float(input("Digite uma temperatura (Celsius): "))

print ((m*9/5+32),"ºF")

#Faça agora o contrário, de Fahrenheit para Celsius

n = float(input("Digite uma temperatura (Fahrenheit): "))

print ((n*5/9-32),"ºC")

#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

o = float(input("Digite o total de kms percorridos: "))
p = float(input("Por quantos dias o carro foi alugado? "))

print("Você gastou",(o*0.15+p*60))

#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias

q = int(input("Digite a quantidade de cigarros fumados por dia: "))
r = int(input("Por quantos anos você fuma? "))

print ("Você perdeu",(q/144*r*365),"dias de vida")

#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão

print (len(str(2**10000)))