import time
import tracemalloc

from math import sin, cos, tan, log
e = 2.71828182846
pi = 3.141592653589793

class InvalidSymbols(Exception):
    pass

def rectangle_rule(func, a, b, nseg=100):
    dx = 1.0 * (b - a) / nseg
    sum = 0
    for i in range(0, nseg):
        temp = (
            (func(i*dx) + func(i*dx + dx))/2 * dx 
        )
        sum += temp
    return sum

def trapezoid_rule(func, a, b, nseg=100):
    dx = 1.0 * (b - a) / nseg
    sum = 0.5 * (func(a) + func(b))
    for i in range(1, nseg):
        sum += func(a + i * dx)

    return sum * dx

def simpson_rule(func, a, b, nseg=100):
    if nseg%2 == 1:
        nseg += 1
    dx = 1.0 * (b - a) / nseg
    sum = (func(a) + 4 * func(a + dx) + func(b))
    for i in range(1, nseg // 2):
        sum += 2 * func(a + (2 * i) * dx) + 4 * func(a + (2 * i + 1) * dx)

    return sum * dx / 3

def processArguments(args, method):
    print(args)
    limits = []
    for i in args:
        if 'x' not in i:
            if i.isdigit():
                limits.append(float(i))
            else:
                limits.append(float(eval(i)))
    
    a = limits[0]
    b = limits[1]
    for sign in ('import', ';', ',', '&', '$', '#', '@'):
        if sign in args[2]:
            raise InvalidSymbols('Invalid Symbols in text area')
    func = eval(f'lambda x: {args[2]}')
    #print(args)
    if method == 'Trapezoid method':
        result = (trapezoid_rule, (func, a, b))
    elif method == 'Rectangle method':
        result = (rectangle_rule, (func, a, b))
    elif method == 'Simpson method':
        result = (simpson_rule, (func, a, b))

    start = time.time ()
    tracemalloc.start ()

    result = result[0](*result[1])

    current, peak = tracemalloc.get_traced_memory ()
    end = time.time ()

    exec_time = f"Execution time : {end - start}"
    mem_usage = f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB"

    tracemalloc.stop ()

    return (result, exec_time, mem_usage)


if __name__ == '__main__':
    #a = rimansIntegral(a=float(input("a : ")), b=float(input("b : ")), func=input('Enter function : '))
    #print(a)
    pass