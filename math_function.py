import math

def add(a, b):
    return a + b

def root(a):
    if a > 0 :
        return math.sqrt(a)
    elif a < 0 :
        str1 = f"Can't find root for {a}"
        return str1
        
