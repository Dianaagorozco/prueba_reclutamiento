# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 20:09:26 2022

@author: Win10Pro
"""

a = None
b = None
op = None

def zero(n):    #your code here
    global a
    global b
    global op
    if (a == None and b == None) or (a != None and b != None): #Condición inicial: asignar 2do num
        b = "0"
        return b
    elif a == None and b != None: #Condición final:asignar 1er num, ejecutar
        a = "0"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))

def one(n):    #your code here
    global a
    global b
    global op
    if a == None and b == None: #Condición inicial: asignar 2do num
        b = "1"
        return b
    elif a == None and b != None: #Condición final:asignar 1er num, ejecutar
        a = "1"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))
    
def two(n):    #your code here
    global a
    global b
    global op
    if a == None and b == None: #Condición inicial: asignar 2do num
        b = "2"
        return b
    elif a == None and b != None: #Condición final:asignar 1er num, ejecutar
        a = "2"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))

def three(n):    #your code here
    global a
    global b
    global op
    if a == None and b == None: #Condición inicial: asignar 2do num
        b = "3"
        return b
    elif a == None and b != None: #Condición final:asignar 1er num, ejecutar
        a = "3"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))


def four(n):    #your code here
    global a
    global b
    global op
    if a == None and b == None: #Condición inicial: asignar 2do num
        b = "4"
        return b
    elif a == None and b != None: #Condición final:asignar 1er num, ejecutar
        a = "4"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))
    

def five(n):    #your code here
    global a
    global b
    global op
    if a == None and b == None:
        b = "5"
        return b
    elif a == None and b != None:
        a = "5"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))
    
def six(n):    #your code here
    global a
    global b
    global op
    if a == None and b == None:
        b = "6"
        return b
    elif a == None and b != None:
        a = "6"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))

def seven(n):    #your code here
    global a
    global b
    global op
    if a == None and b == None:
        b = "7"
        return b
    elif a == None and b != None:
        a = "7"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))
    


def eight(n):    #your code here
    global a
    global b
    global op
    if a == None and b == None:
        b = "8"
        return b
    elif a == None and b != None:
        a = "8"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))   
    

def nine(n):    #your code here
    global a
    global b
    global op
    if a == None and b == None:
        b = "9"
        return b
    elif a == None and b != None:
        a = "9"
        x = a+op+b
        a = None
        b = None
        return round(eval(x))

def plus(n2):    #your code here
    global a
    global b
    global op
    op ="+"
    return n2

def minus(n2):    #your code here
    global a
    global b
    global op
    op ="-"
    return n2

def times(n2):    #your code here
    global a
    global b
    global op
    op ="*"
    return n2

def divided_by(n2):    #your code here
    global a
    global b
    global op
    op ="/"
    return n2

print(four(times(five(1)))) # imprime 20
print(one(plus(eight(1)))) # imprime 9
print(seven(minus(three(1)))) # imprime 4
print(nine(divided_by(three(1)))) # imprime 3