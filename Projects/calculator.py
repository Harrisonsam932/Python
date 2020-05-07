# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:35:50 2018

@author: nelson
"""


def add(a, b):
    sum = a + b
    print(sum)


def sub(a, b):
    sub = a - b
    print(sub)


def mul(a, b):
    product = a * b
    print(product)


def div(a, b):
    quotient = a / b
    print(quotient)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", sub(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", mul(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("Invalid input")
