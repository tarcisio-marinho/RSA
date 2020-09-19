#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import random


'''
Calcula o totiente do numero primo
'''
def totient(number):
    if(prime(number)):
        return number-1
    else:
        return False


'''
Verifica se um numero gerado é primo
'''
# fairly good method to check if a number is prime
def prime(n):  # check if the number is prime
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i+2) == 0):
            return False
        i += 6
    return True


'''
Gera um numero aleatório E, sasfazendo as condições
'''
def generate_E(num):
    def mdc(n1, n2):
        rest = 1
        while(n2 != 0):
            rest = n1 % n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2, num)
        if(mdc(num, e) == 1):
            return e


'''
Gera um numero primo aleatório
'''
def generate_primes():  # generate the primes numbers - p and q
    while True:  # 2**2048 is the RSA standart keys
        x = random.randrange(11, 101, 2)  # this third param is the step (only odd numbers are accounted)
        y = random.randrange(11, 101, 2)  # it starts at twelve so the lower primes don't mess up
        if(prime(x) and prime(y) and x != y):  # x can't be equal to y, otherwise the algorithm won't work
            return (x, y)


'''
Cifra um texto
'''
def cipher(words, e, n):  # get the words and compute the cipher
    tam = len(words)
    i = 0
    lista = []
    while(i < tam):
        letter = words[i]
        k = ord(letter)
        k = k**e
        d = k % n
        lista.append(d)
        i += 1
    return lista


'''
Descriptografa um texto criptografado
'''
def descifra(cifra, n, d):
    lista = []
    i = 0
    tamanho = len(cifra)
    # texto=cifra ^ d mod n
    while i < tamanho:
        result = cifra[i]**d
        texto = result % n
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return "".join(lista)


'''
Calcula a chave privada
'''
def calculate_private_key(toti, e):
    d = 0
    while(d*e % toti != 1):
        d += 1
    return d



# MAIN
if __name__ == '__main__':
    text = input("Insert message: ")
    p, q = generate_primes()  # generates random primes
    n = p*q  # compute N
    y = totient(p)  # compute the totient of P
    x = totient(q)  # compute the totient of Q
    totient_de_N = x*y  # compute the totient of N
    e = generate_E(totient_de_N)  # generate E
    public_key = (n, e)

    print('Your public key:', public_key)
    text_cipher = cipher(text, e, n)
    print('Your encrypted message:', text_cipher)
    d = calculate_private_key(totient_de_N, e)
    print('Your private key is:', d)
    original_text = descifra(text_cipher, n, d)
    print('your original message:', original_text)
