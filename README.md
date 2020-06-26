# RSA-Encryption

RSA is abbreviated as Rivest–Shamir–Adleman which is an alogorithm that is used by modern computers to encrypt and decrypt messages. It is an asymmetric cryptographic algorithm. Asymmetric means that there are two different keys. This is also called public key cryptography, because one of the keys can be given to anyone.

This project contains different functions: 

## def gcd(a, b)

The function gcd(a, b), use the Euclidean Algorithm to find the GCD (Greatest Common Divisor) of two numbers a and b. The return type is an integer. 

## def inverse(a, b)

The function inverse(a, b), use the Extended Euclidean Algorithm to find the inverse of a mod b. The return type is an integer. So, for inverse we need to find the value of t as per the general equation of Extended Euclidean Algorithm. So, the value of t will be calculated till the time when we dont get the value of b as 0, in order to get the gcd. 

## def prime(number)

Support function to the generate key to know if the function is prime or not. If the function is prime and not equal it would be only then that generate_key function will be take place. 

## def generate_keypair(a, b)

The function generate key(a, b), generate the public key (e, n) and private key (d, n). As- sume that a and b would be primes and you don’t need to test the validity of inputs. Return type should be a two-element tuple: first element is tuple representing public key (e, n) and second element is tuple representing private key (d, n). For example, ((1, 4), (3, 4)) is a valid return type.

## def encrypt(public_key, txt)

The function encrypt(private key, txt), you are given a tuple (d, n) as private key, and you are suppose to create a list of ciphers that represents the encrypted version of string txt (each char in string has a corresponding cipher in list). The return type is a list of integers. Use the python in-built function ord(char) to convert a string character into integer before encrypting it.

## def decrypt(private_key, ciphers)

The function decrypt(public key, ciphers), you are given a tuple (e, n) as public key, and you are suppose to create a new string that is the decrypted version of the list of ciphers. After you decrypt a cipher, use Python in-built function char(int) to convert int to character. The return type is Python string.




