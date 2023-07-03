"""
Author: Navid Raufi
Date: 4th of July
Title: Prime Number Checker
"""
num = int(input("Type the number: "))

def isPrime(number):
    isPrime = True
    for i in range(2,number):
        if number % i==0:
            isPrime = False
    if isPrime:
        print("This number is prime.")
    else:
        print("This number is not prime.")
isPrime(num)