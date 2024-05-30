# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
from pywebio.input import *
from pywebio.output import *

def mathematicaloperations():
    number1 = input("Enter First Number: ", type=FLOAT)
    number2 = input("Enter Second Number: ", type=FLOAT)
    ans = 0
    operation = radio("Choose any one from the following operations:", options=['+', '-', '*', '/', '%', 'fact', 'square', 'sqrt', 'cube', 'pow', 'ln', 'log10'])

    operation_name = ""
    
    if operation == '+':
        operation_name = 'Addition'
        ans = number1 + number2                              
    
    elif operation == '-':
        operation_name = 'Subtraction'
        ans = number1 - number2
        
    elif operation == '*':
        operation_name = 'Multiplication'
        ans = number1 * number2 
        
    elif operation == '/':
        operation_name = 'Division'
        ans = number1 / number2
        
    elif operation == '%':
        operation_name = 'Modulus'
        ans = number1 % number2
        
    elif operation == 'fact':
        operation_name = 'Factorial of 1st number'
        ans = math.factorial(number1)
        
    elif operation == 'square':
        operation_name = 'Square of 1st number'
        ans = number1**2
        
    elif operation == 'sqrt':
        operation_name = 'Square root of 1st number'
        ans = math.sqrt(number1)
        
    elif operation == 'cube':
        operation_name = 'Cube of 1st number'
        ans = number1**3
    
    elif operation == 'ln':
        operation_name = 'Natural Log'
        ans = math.log(number1)
        
    elif operation == 'log10':
        operation_name = 'Log to the base 10'
        ans = math.log10(number1)
        
    put_text('The operation performed is {} and the result is {}'.format(operation_name, ans))
    
if __name__ == '__main__':
    mathematicaloperations()
