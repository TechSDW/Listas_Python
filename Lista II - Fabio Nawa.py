# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escalen

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and a == c:
        print ("Esse triângulo existe e é equilátero!")

    elif a != b  and a != c and b != c:
        print ("Esse triângulo existe e é escaleno!")
    
    else:
        print ("Esse triângulo existe e é isósceles!")

else:
    print ("Esses valores não formam um triângulo!")

# Determine se um ano é bissexto. Verifique no Google como fazer isso...

year = int(input("Digite um ano: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print ("Esse ano é bissexto!")

else:
    print ("Esse ano não é bissexto!")

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO

peso = int(input("Digite o peso dos peixes pescados hoje: "))
multa = 0

if peso > 50:
    multa = (peso - 50) * 4
    print (f"Você excedeu o limite e terá uma multa de R${multa}")

else:
    print ("Você não recebeu multa")

# Faça um Programa que leia três números e mostre o maior dele

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print (f"O maior número é o primeiro ({n1})")

elif n2 > n1 and n2 > n3:
    print (f"O maior número é o segundo ({n2})")

else:
    print (f"O maior número é o terceiro ({n3})")

# Faça um Programa que leia três números e mostre o maior e o menor deles

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print (f"O maior número é o primeiro ({n1})")

elif n2 > n3:
    print (f"O maior número é o segundo ({n2})")

else:
    print (f"O maior número é o terceiro ({n3})")

if n1 < n2 and n1 < n3:
    print (f"O menor número é o primeiro ({n1})")

elif n2 < n3:
    print (f"O menor número é o segundo ({n2})")

else:
    print (f"O menor número é o terceiro ({n3})")


# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$

hora = float(input("Digite quanto você ganha por hora: "))
TempoMes = float(input("Digite quantas horas você trabalha em um mês: "))

SalarioBruto = hora * TempoMes
IR = SalarioBruto * 11 / 100
INSS = SalarioBruto * 8 / 100
Sindicato = SalarioBruto * 5 / 100

print (f"IR: R${IR:.2f}")
print (f"INSS: R${INSS:.2f}")
print (f"Sindicato: R${Sindicato:.2f}")
print ("Seu salário líquido é R$" + str(SalarioBruto - IR - INSS - Sindicato))

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

area = int(input("Qual é o tamanho da área a ser pintada (em m²)? "))

QtdLata, resto = str(area / 54).split('.')
QtdLata = int(QtdLata)
resto = int(resto)

if resto != 0:
    QtdLata = QtdLata + 1
    print (f"Você terá que usar {QtdLata} lata(s) e custará R$" + str(QtdLata * 80))

else:
    print (f"Você terá que usar {QtdLata} lata(s) e custará R$" + str(QtdLata * 80))