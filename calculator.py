from os import *
import os
x = 0
myhost = os.uname()[0]
def clear_screen ():
    
    if myhost == 'Linux':
        _=system('clear')
    else:
        _=system('cls') 
#===========================
clear_screen ()
#============================
def my_res_sum ():
    global x
    x = float (res + n2)
    return x
#============================
def my_res_sub ():
    global x
    x = float (res - n2)
    return x
#============================
def my_res_mul ():
    global x
    x = float (res * n2)
    return x
#============================
def my_res_div ():
    global x
    x = float (res / n2)
    return x
#============================
def my_res_pwr ():
    global x
    x = float (res ** n2)
    return x
#============================
def my_res_prc ():
    global x
    x = float (res/100)
    return x
#============================


def photo():
    print ("""
    |=======================|
    |  CODER: AhmadNueirat  |
    |    < calculator >     |
    |=======================|
    |                       |
    |   [c]  [%]  [/]  [*]  |
    |                       |
    |   [7]  [8]  [9]  [-]  |
    |                       |
    |   [4]  [5]  [6]  [+]  |
    |                       |
    |   [1]  [2]  [3]  [=]  |
    |                       |
    |   [Esc]  [0]  [ MOD]  |
    |=======================|
    """)

def _math(opr,y):# not first time
    print (f"""
    |=======================|
    |   {res} {opr} {n2}     
    |   ==> {y}   
    |=======================|
    |                       |
    |   [c]  [%]  [/]  [*]  |
    |                       |
    |   [7]  [8]  [9]  [-]  |
    |                       |
    |   [4]  [5]  [6]  [+]  |
    |                       |
    |   [1]  [2]  [3]  [=]  |
    |                       |
    |   [Esc]  [0]  [ MOD]  |
    |=======================|
    """) 
    
def _math_f(opr):# first time 
    print (f"""
    |=======================|
    |   {n1} {opr} {n2}     
    |   ==> {res}  
    |=======================|
    |                       |
    |   [c]  [%]  [/]  [*]  |
    |                       |
    |   [7]  [8]  [9]  [-]  |
    |                       |
    |   [4]  [5]  [6]  [+]  |
    |                       |
    |   [1]  [2]  [3]  [=]  |
    |                       |
    |   [Esc]  [0]  [ MOD]  |
    |=======================|
    """)
n1 = 0 
n2 = 0
res = 0
count = 0
op = ""
photo()
n1 =int( input ("Enter The Number ==>  "))
while (1):
    op = input ("Enter The Oparate : ")
# ================for sum operations =========================
    if op == "+" : 
# ================for sum operations =========================
        if  count == (0):
            n2 =int( input ("Enter The Number ==>  "))
            count += 1
            clear_screen()
            res = n1+n2
            clear_screen () 
            _math_f(op)
        else:
            n2 =int( input ("Enter The Number ==>  "))
            clear_screen ()
            _math(op,my_res_sum())
            res = x
# ============== for sub oprations ===========================
    elif op == "-":
# ============== for sub oprations ===========================
        if  count == (0):
            n2 =int( input ("Enter The Number ==>  "))
            count += 1
            res = n1-n2
            clear_screen () 
            _math_f(op)
        else:
            n2 =int( input ("Enter The Number ==>  "))
            clear_screen ()
            _math(op,my_res_sub())
            res = x
# ============== for mul oprations ===========================
    elif op == "*":    
# ============== for mul oprations ===========================
        if  count == (0):
            n2 =int( input ("Enter The Number ==>  "))
            count += 1
            res = n1*n2
            clear_screen ()
            _math_f(op)
        else:
            n2 =int( input ("Enter The Number ==>  "))
            clear_screen ()
            _math(op,my_res_mul())
            res = x
            
# ============== for div oprations ===========================
    elif op == "/":    
# ============== for div oprations ===========================
        if  count == (0):
            n2 =int( input ("Enter The Number ==>  "))
            count += 1  
            res = n1/n2
            clear_screen ()
            _math_f(op)
        else:
            n2 =int( input ("Enter The Number ==>  "))
            clear_screen ()
            _math(op,my_res_div())
            res = x
# ============== for pwr oprations ===========================
    elif op == "^":    
# ============== for pwr oprations ===========================
        if  count == (0):
            n2 =int( input ("Enter The Number ==>  "))
            count += 1  
            res = n1**n2
            clear_screen ()
            _math_f(op)
        else:
            n2 =int( input ("Enter The Number ==>  "))
            clear_screen ()
            _math(op,my_res_pwr())
            res = x
# ============== for prc oprations ===========================
    elif op == "%":    
# ============== for prc oprations ===========================
        if  count == (0):
            count += 1
            n2 = ' '  
            res = (n1 / 100)
            clear_screen ()
            _math_f(op)
        else:
            n2 = ' '
            clear_screen ()
            _math(op,my_res_prc())
            res = x
