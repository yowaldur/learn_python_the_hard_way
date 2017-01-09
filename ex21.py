# -*- coding: utf-8 -*-

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = int(raw_input('a? '))
b = int(raw_input('b? '))

print '''What do you want to do with these values?
1: add
2: subtract
3: multiply
4: divide
'''

operation = int(raw_input('Only number: '))

if operation == 1:
    result = add(a, b)
    print '%d + %d = %d' % (a, b, result)
elif operation == 2:
    result = subtract(a, b)
    print '%d - %d = %d' % (a, b, result)
elif operation == 3:
    result = multiply(a, b)
    print '%d * %d = %d' % (a, b, result)
elif operation == 4:
    result = divide(a, b)
    print '%d / %d = %d' % (a, b, result)
