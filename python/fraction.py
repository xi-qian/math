import random
import math

def mul(a):
    x = a[0]*a[2]
    y = a[1]*a[3]
    g = math.gcd(x,y)
    if g > 1:
        x = int(x/g)
        y = int(y/g)
    return (x, y)

def div(a):
    return mul([a[0],a[1],a[3],a[2]])

def add(a):
    g = math.gcd(a[1],a[3])
    d = int(a[1]/g)*int(a[3]/g)*g
    x = int(a[0]*a[3]/g)
    y = int(a[2]*a[1]/g)
    n = x+y
    g = math.gcd(d, n)
    return (int(n/g), int(d/g))

def sub(a):
    return add([a[0],a[1],-1*a[2], a[3]])

ops={'+':add, '-':sub, '/':div, '*':mul}
ops_keys = list(ops.keys())
ops_revers = {'+':'-', '-':'+', '*':'/', '/':'*'}

def generate_frac_cal(max_number=100):
    a = list()
    for i in range(4):
        m = 1+i%2; #don't use 1 as denominator
        a.append(random.randint(m, max_number))
    for i in (0,2):
        g = math.gcd(a[0+i], a[1+i])
        print("gcd(%d, %d)=%d"%(a[0+i], a[1+i], g))
        if g>1:
            a[0+i]=int(a[0+i]/g)
            a[1+i]=int(a[1+i]/g)
    op = random.choice(ops_keys)
    a.append(op)
    return a

def gen_frac_cal(max_number=100, max_answer=10):
    a = list()
    #generate answer
    for i in range(2):
        a.append(random.randint(1,max_answer))

    #generate one oprand

    for i in range(2):
        a.append(random.randint(2,max_number))

    op = random.choice(ops_keys)
    op_rev = ops_revers[op]
    (n,d) = ops[op_rev](a)

    r=list()
    r.append(n)
    r.append(d)
    g = math.gcd(a[2],a[3])
    r.append(int(a[2]/g))
    r.append(int(a[3]/g))
    r.append(op)

    return r

def print_frac_cal(a):
    s = str(a[0])+'/'+str(a[1])+' '+a[4]+' '+str(a[2])+'/'+str(a[3])
    print(s)
    answer = ops[a[4]](a)
    print(str(answer[0])+'/'+str(answer[1]))

for i in range(20):
    print_frac_cal(gen_frac_cal())
    #print_frac_cal(generate_frac_cal())
