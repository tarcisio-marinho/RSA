#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import random

def totient(number): # compute the totient of a prime number
    if(prime(number)==True):
        return number-1
    else:
        return False

# it isnt the best method to compute prime numbers
def prime(number): # check if the number is prime
    i=1
    times=0
    while(i<=number):
        if(number%i==0):
            times=times+1
        i=i+1

    if(times==2):
        return True
    else:
        return False



def generate_E(num): # recives totient of N as a parameter
    def mdc(n1,n2): # compute the mdc of the totient of N and E
        rest=1
        while(n2!=0):
            rest=n1%n2
            n1=n2
            n2=rest

        return n1

    while True:
        e=random.randrange(2,num) # define the range of the E
        if(mdc(num,e)==1):
            return e

def generate_prime(): # generate the prime number - p e q
    while True: # 2**2048 is the RSA standart keys
        x=random.randrange(1,100) # define the range of the primes
        if(prime(x)==True):
            return x

def mod(a,b): # mod function
    if(a<b):
        return a
    else:
        c=a%b
        return c

def cipher(words,e,n): # get the words and compute the cipher
    tam=len(words)
    i=0
    lista=[]
    while(i<tam):
        letter=words[i]
        k=ord(letter)
        k=k**e
        d=mod(k,n)
        lista.append(d)
        i=i+1
    return lista

def private_key(toti,e):
    d=0
    while(mod(d*e,toti)!=1):
        d=d+1
    return d

def descifra(cifra,n,d):
    lista=[]
    i=0
    tamanho=len(cifra)
    # texto=cifra ^ d mod n
    while i<tamanho:
        result=cifra[i]**d
        texto=mod(result,n)
        letra=chr(texto)
        lista.append(letra)
        i=i+1
    print(lista)


## MAIN
text=raw_input('Insert the text that u want to cryptograph: ')
p=generate_prime() # generates random P
q=generate_prime() # generates random Q
n=p*q # compute N
y=totient(p) # compute the totient of P
x=totient(q) # compute the totient of Q
totient_de_N=x*y # compute the totient of N
e=generate_E(totient_de_N) # generate E
public_key=[n,e]
print('Your public key is '+str(public_key))
text_cipher=cipher(text,e,n)
print(text_cipher)
d=private_key(totient_de_N,e)
print('Your private key is '+str(d))
descifra(text_cipher,n,d)
