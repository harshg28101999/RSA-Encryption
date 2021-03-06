import math
from random import randrange

# Author: Harsh Gupta

def gcd(a, b):
    # Your code here
    """
    --Giving the values of 2 numbers:
        - Choosing the number larger among the two numbers and the larger number would be 'a' and the smaller number as 'b'.
    -- If a and b are equal then the gcd would be a.
    -- If the smaller number is 0 then the gcd would be automatically a. 
    -- If these conditions are overridden then it would simply continue to calculate the gcd between b and a%b.
    """

    if (a<b):
        temp = a
        a = b
        b = temp
    
    if (a==b):
        return a
    elif (b==0):
        return a
    else:
        return (gcd(b,a%b))
    pass

def inverse(a, b):   # use extended euclidean algorithm to find inverse
    # Your code here
    """
    -- Given 2 numbers a and b. 
    -- So, for inverse we need to find the value of t as per the general equation of Extended Euclidean Algorithm. 
    -- So, the value of t will be calculated till the time when we dont get the value of b as 0, in order to get the gcd. 
    """
    for i in range (b):
        if ((i * a - 1) % b == 0):
            return i
    
    pass

def prime(number):
    """
    --Support function to the generate key to know if the function is prime or not.
        - If the function is prime and not equal it would be only then that generate_key function will be take place. 
    """
    count = 0 
    for i in range (1, number):

        if (number % i == 0):
            count = count + 1
    
    if count > 2:
        return False
    else: 
    	return True
          
def generate_keypair(a, b):
    # Your code here
    """
    -- Give the values of numbers.
        - The numbers have to be prime numbers and they cannot be equal. 
        - If any of the condition is violated then it would raise an error.  
    -- Find n and k. n is product of a and b, k is the product of a-1 and b-1. 
    -- Apply the gcd function of e and k. 
    -- Find the value of e which would be generated by implementing the randrage library.
    -- Once got e, use the modular inverse operation to get d. 
    """

    if not (prime(a) and prime(b)):
        raise ValueError("Both the numbers need to be prime")

    if (a==b):
        raise ValueError("Both the numbers cannot be equal to each other")

    n = a * b
    k = (a-1) * (b-1)

    e = randrange(1, k)
    hcf = gcd(e, k)

    while hcf != 1:
        e = randrange(1, k)
        hcf = gcd(e, k)
    
    d = inverse(e, k)
    # (e, n) is public, (d, n) is private
    return ((e, n), (d, n))
    pass

def encrypt(public_key, txt):
    # Your code here
    """
    -- Initiating the value of n as the public key. 
    -- To encrypt the string we would need to use to formula of encryption in order to change the values to ASCII values. 
    """
    k, n = public_key
    
    encrypted_string = [(ord(character) ** k) % n for character in txt]
    return encrypted_string
    pass

def decrypt(private_key, ciphers):
    # Your code here
    """
    -- Initiating n as a private key. 
    -- Without joining the strings, the error would be: 
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        - In order to remove the '', we would use the join function. 
    """
    k, n = private_key

    decrypted_string = [chr((character ** k) % n) for character in ciphers]
    return ''.join(decrypted_string)
    pass
