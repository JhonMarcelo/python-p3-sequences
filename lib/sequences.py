#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci=[]
    i=0
    while i < length:
        if i == 0:
            fibonacci.append(i)
            i+=1
        elif i == 1:
            fibonacci.append(i)
            i+=1
        else:
            fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
            i+=1
    print(fibonacci)
    

