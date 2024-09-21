# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min

import random

a = 0
b = random.sample(range(100), 10)
c = 0
d = 101

while a <= 9:
    if b[a] > c:
        c = b[a]
    if b[a] < d:
        d = b[a]
    a = a + 1

print (f"O maior número é {c} e o menor número é {d}")

# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números paresna lista PAR e os números ímpares na lista IMPAR. Imprima as três listas

import random

b = random.sample(range(100), 20)
par = []
impar = []

for a in range (19):
    if b[a] % 2 == 0:
        par.append(b[a])
    else:
        impar.append(b[a])

print (f"Os números pares são: {par} e os números ímpares são: {impar}")

# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores

import random

a = random.sample(range(100), 10)
b = random.sample(range(100), 10)
c = []

for n in range (10):
    c.append(a[n])
    c.append(b[n])

print (a)
print (b)
print (c)

# Seja o statement sobre diversida de: “ The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas

a = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone Our community is based on mutual respect tolerance and encouragement and we are working to help each other live up to these principles We want our community to be more diverse whoever you are and whatever your background we welcome you'''
a = a.replace(":", " ").replace(",", " ").replace(".", " ")
a = a.lower()
a = a.split()
c = ""

for n in range(len(a)):
    c = (a[0 + n])

    if c[0] in 'python':
        print (c)

# Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais

a = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'''
a = a.replace(":", " ").replace(".", " ").replace(",", " ")
a = a.lower()
a = a.split()
b = ''
c = ''
soma = 0

for z in range(len(a)):
    b = a[z]
    x = 0

    while x < len(b):
        c = b[x]
        
        if c in 'python' and len(b) > 4:
            soma = soma + 1
            x = len(b)
        else:
            x = x + 1
            
print (soma)