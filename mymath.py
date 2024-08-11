from decimal import Decimal, InvalidOperation, DivisionByZero

pi = Decimal('3.141592653589793')
e = Decimal('2.718281828459045')
ERR = "ERROR: Can't handle your input!"

def abs(x):
    return x if x >= 0 else -x

def fact(x):
    if int(x) != x:
        return ERR
    elif x < 0:
        return ERR
    a = 1
    while x > 1:
        a *= x
        x -= 1
    return a

def sqrt(x):
    if x < 0:
        return ERR
    elif x == 0:
        return x
    guess = x # arbitrary #TODO: choose better first guess
    diff = 69 # arbitrary
    while diff >= Decimal('0.00001'):
        new_guess = guess - (guess**2 - x)/(2*guess)
        diff = abs(new_guess - guess)
        guess = new_guess
    return guess

def ln(x):
    if x <= 0:
        return ERR
    guess = x # arbitrary #TODO: choose better first guess
    diff = 1 # arbitrary
    while diff >= Decimal('0.00001'):
        new_guess = guess + x/e**guess - 1
        diff = abs(new_guess - guess)
        guess = new_guess
    return guess

def log(x):
    return ln(x)/ln(Decimal(10))

def sin(x):
    if x < 0:
        return -sin(-x)
    elif x <= pi/2:
        a = 0
        sign = 1
        div = 1
        t = x
        x *= x
        for i in range(1, 1001, 2):
            a += sign*t/div
            sign *= -1
            div *= (i+1)*(i+2)
            t *= x
        return a
    elif pi/2 <= x <= pi:
        return sin(pi - x)
    elif pi <= x <= 3*pi/2:
        return -sin(x - pi)
    elif 3*pi/2 <= x <= 2*pi:
        return -sin(2*pi - x)
    else:
        return sin(x%(2*pi))

def cos(x):
    if x < 0:
        return cos(-x)
    elif x <= pi/2:
        a = 0
        sign = 1
        div = 1
        t = Decimal('1')
        x *= x
        for i in range(0, 1000, 2):
            a += sign*t/div
            sign *= -1
            div *= (i+1)*(i+2)
            t *= x
        return a
    elif pi/2 <= x <= pi:
        return -cos(pi - x)
    elif pi <= x <= 3*pi/2:
        return -cos(x - pi)
    elif 3*pi/2 <= x <= 2*pi:
        return cos(2*pi - x)
    else:
        return cos(x%(2*pi))


def tan(x):
    return sin(x)/cos(x)

def cosec(x):
    return 1/sin(x)

def sec(x):
    return 1/cos(x)

def cot(x):
    return 1/tan(x)

def quad(s):
    s = s.strip()
    s = [x for x in s.split(' ') if x != '']
    if s[0] != 'quad':
        return ERR
    if len(s) != 4:
        return ERR
    try:
        s = [Decimal(x) for x in s[1:]]
    except InvalidOperation:
        return ERR
    try:
        d = sqrt(s[1]**2 - 4*s[0]*s[2])
        if d!=0:
            return ', '.join([str(round((-s[1] + sign*d)/(2*s[0]), 3)) for sign in (-1, 1)])
        else:
            return str(round(-s[1]/(2*s[0]), 3))
    except InvalidOperation:
        return 'ERROR: NON-real solutions'
    except DivisionByZero:
        if s[2] == 0:
            return str(round(Decimal('0'), 3))
        else:
            return 'ERROR: No solution'


exported = {'sin': sin, 'cos': cos, 'tan': tan, 'cosec': cosec, 'sec': sec,
            'cot': cot, 'sqrt': sqrt, 'log': log, 'fact': fact, 'abs': abs,
            'ln': ln}
