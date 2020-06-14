from os import *
_ = system('clear')
#============================
def my_res_sum ():
    global x
    x = int (res + n2)
    return x
#============================
def my_res_sub ():
    global x
    x = int (res - n2)
    return x
#============================
def my_res_mul ():
    global x
    x = int (res * n2)
    return x
#============================
def my_res_div ():
    global x
    x = int (res / n2)
    return x
#============================

def photo():# def in top * 
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
    |   [ ]  [0]  [ ]  [ ]  |
    |=======================|
    """)

#               {res} {opr} {n2} 
#         ===>  {y}


#       {n1} {opr} {n2}  
#===>  {res}

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
    |   [ ]  [0]  [ ]  [ ]  |
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
    |   [ ]  [0]  [ ]  [ ]  |
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
            _=system ('clear')
            res = n1+n2
            _=system ('clear') 
            _math_f(op)
        else:
            n2 =int( input ("Enter The Number ==>  "))
            _=system ('clear')
            _math(op,my_res_sum())
            res = x
# ============== for sub oprations ===========================
    elif op == "-":
# ============== for sub oprations ===========================
        if  count == (0):
            n2 =int( input ("Enter The Number ==>  "))
            count += 1
            res = n1-n2
            _=system ('clear') 
            _math_f(op)
        else:
            n2 =int( input ("Enter The Number ==>  "))
            _=system ('clear')
            _math(op,my_res_sub())
            res = x
# ============== for mul oprations ===========================
    elif op == "*":    
# ============== for mul oprations ===========================
        if  count == (0):
            n2 =int( input ("Enter The Number ==>  "))
            count += 1
            res = n1*n2
            _=system ('clear')
            _math_f(op)
        else:
            n2 =int( input ("Enter The Number ==>  "))
            _=system ('clear')
            _math(op,my_res_mul())
            res = x
            
# ============== for div oprations ===========================
    elif op == "/":    
# ============== for div oprations ===========================
        if  count == (0):
            n2 =int( input ("Enter The Number ==>  "))
            count += 1  
            res = n1/n2
            _=system ('clear')
            _math_f(op)
        else:
            n2 =int( input ("Enter The Number ==>  "))
            _=system ('clear')
            _math(op,my_res_div())
            res = x
