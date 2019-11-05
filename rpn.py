#!/usr/bin/env python3

import operator
import colored
from colored import stylize


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def print_list(stack):
    print("[", end="")
    for item in stack[:-1]:
        print(style(item), end=", ")
    if stack != []:
        print(style(stack[-1]), end="")
    print("]")

def style(val):
    try:
        val = int(val)
        return stylize(val, colored.fg("green" if val >= 0 else "red"))
    except:
        if val in operators:
            return stylize(val, colored.fg("orange_3"))
        return val

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print_list(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        equation = input("rpn calc> ")
        print("input:", end=" ")
        print_list(equation.split())
        result = calculate(equation)
        result = stylize(result, colored.fg("green" if result >= 0 else "red"))
        print("Result: ", result)

if __name__ == '__main__':
    main()
