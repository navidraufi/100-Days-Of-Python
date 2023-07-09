"""
Author: Navid Raufi
Title: Calculator

"""
from os import system

first_number = float(input("Enter the first number: \n"))
operation = input("+\n-\n*\n/\nPick an operation: ")
second_number = float(input("Enter the second number that you wanna calculate: \n"))

def calculate(first_number,second_number):
    
    result = 0 
    if operation == "+":
        result += first_number + second_number
    elif operation == "-":
        result+= first_number-second_number
    elif operation == "*":
        result+= first_number*second_number
    elif operation == "/":
        result+= first_number/second_number
    else:
        print("Please try again!")
    
    return (result)


print(f"{first_number} {operation} {second_number} = {calculate(first_number,second_number)}")


more_calculate = True

while more_calculate:
    first_number = calculate(first_number,second_number)
    continue_more = input(f"Continue calculating with {first_number}? 'Y' \nor start new 'N' ? ").lower()
    if continue_more == "y":
        
        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("Enter the second number that you wanna calculate: \n"))
        total_result = calculate(first_number,second_number)
        print(f"{first_number} {operation} {second_number} = {calculate(first_number,second_number)}")
    elif continue_more == "n":
        system("cls")
        
        first_number = float(input("Enter the first number: \n"))
        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("Enter the second number that you wanna calculate: \n"))
        
        calculate(first_number,second_number)
        print(f"{first_number} {operation} {second_number} = {calculate(first_number,second_number)}")