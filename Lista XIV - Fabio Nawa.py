#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0


# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


# Exercícios extras para listas


# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
# PS: se você usar o comando set deve ficar ordenado
# como aparece no resultado dos testes
# [2, 2, 1, 3]

def remove_iguais(nums):
  lista = []

  for x in range(len(nums)):
    if nums[x] not in lista:
      lista.append(nums[x])

  lista.sort()
  return lista

# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar
def cripto(frase):
  frase = frase.split()
  resp = ""

  for x in range(len(frase)):
    a = list(frase[x])
    a.sort()
    a = str(a)
    a = a.replace(",","")
    a = a.replace("[","")
    a = a.replace("]","")
    a = a.replace(" ", "")
    a = a.replace("'","")
    b = a[::-1]
    y = 0
    d = 0

    while y in range(len(b)):
      if b.count(b[y]) > 1:
        b = b.replace(b[y],"",b.count(b[y])-1)
        c = b[::-1]
      else:
        d += 1
      y += 1
    
    if d == len(b):
      resp += a + " "
    else:
      resp += c + " "

  resp = resp[:-1]
  return resp

# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2
def derivada(coef):
  resp = []
  for x in range(len(coef)):
    if x != 0:
      resp.append(coef[x]*x)
  
  return resp

# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# pode supor que n1 e n2 tem o mesmo número de dígitos
# Não vale converter a lista em número para somar diretamente
def soma(n1, n2):
  a = 0
  resp = []
  for x in range(len(n1)):
    b = n1[x] + n2[x] + a

    if b > 9:
      b = str(b)
      a = int(b[0])
      b = int(b) - 10
      resp.append(b)
      if x == len(n1)-1:
        resp.append(a)
    else:
      resp.append(b)
      a = 0

  return resp

# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é, uma palavra é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False
def anagrama(s1, s2):
  if len(s1) != len(s2):
    return False
  else:
    for x in range(len(s1)):
      x = str(s1[x])
      if s1.count(x) != s2.count(x):
        return False
    return True

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))


def main():
  print ('remove_iguais')
  test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
  test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
  test(remove_iguais([]), [])

  print ()
  print ('cripto')
  test(cripto('ana e mariana gostam de banana'),
       'an e aimnr agmost de abn')
  test(cripto('Batatinha quando nasce esparrama pelo chão'),
       'Bahint adnoqu acens aemprs elop choã')


  print ()
  print ('derivada de polinômio')
  test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
  test(derivada([4, 16, 1]), [16, 2])


  print ()
  print ('soma em listas invertidas')
  test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
  test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])


  print ()
  print ('anagrama')
  test(anagrama('abacate', 'abacatx'), False)
  test(anagrama('sim', 'xxs'), False)
  test(anagrama('sim', 'siiimmmmm'), False)
  test(anagrama('iracema', 'america'), True)
  test(anagrama('ator', 'rota'), True)
  test(anagrama('aberto', 'rebato'), True)
  test(anagrama('amor', 'roma'), True)
  test(anagrama('ramo', 'amor'), True)
  test(anagrama('baba', 'aba'), False)
  test(anagrama('casa', 'cassa'), False)
  test(anagrama('palmeiras', 'abacate'), False)
  test(anagrama('arco', 'roca'), True)
  test(anagrama('alegria', 'alergia'), True)
  test(anagrama('cantiga', 'catinga'), True)


if __name__ == '__main__':
  main()
