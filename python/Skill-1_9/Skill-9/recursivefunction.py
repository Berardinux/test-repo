#!/usr/bin/env python3

# Factorial
def factorial(number):
    final = 1
    for i in range(number, 0, -1):
        final = final * i
    
    return final

print( factorial(6))

def factorialRecur(number):
    if number == 1:
        return number
    else:
        return number * factorialRecur(number - 1)

print( factorialRecur(9))
