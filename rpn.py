#!/usr/bin/env python3

import operator
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    '|': operator.or_
}


def  calculate(myarg):
    stack = list()
    tokens = myarg.split()
    for token in tokens:
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            val2 = stack.pop()
            val1 = stack.pop()
            result = function(val1, val2)
            stack.append(result)

    if len(stack) != 1:
        raise TypeError('Too many arguments on the stack')
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 15:
            result = colored(result, 'red', attrs=['bold'])
        elif result > 25:
            result = colored(result, 'green', attrs=['blink'])
        else
            result = colored(result, 'yellow', attrs=['underline'])
        print(result)


if __name__ == '__main__':
    main()
