"""Handles the input from the user using python's AST implementation"""

import ast
import mymath as mm
from decimal import Decimal, InvalidOperation, DivisionByZero

# This is a hack to match this in match/case statements
class ERR:
    ERR = "ERROR: Can't handle your input!"

STORE = {'pi': mm.pi, 'e': mm.e}

def solve(s):
    global string
    string = s
    try:
        t = ast.parse(s).body
    except SyntaxError:
        if tmp:=mm.quad(s):
            return tmp
        return ERR.ERR
    l = list()
    for x in t:
        tmp = parse(x)
        try:
            l.append(str(round(tmp, 3)))
        except TypeError:
            l.append(tmp)
    return '; '.join(l)

def parse(E):
    def parse_binop(E):
        def bi_add(x, y):
            return x + y
        def bi_sub(x, y):
            return x - y
        def bi_mult(x, y):
            return x * y
        def bi_div(x, y):
            try:
                return x / y
            except DivisionByZero:
                return ERR.ERR
        def bi_mod(x, y):
            try:
                return x % y
            except InvalidOperation:
                return ERR.ERR
        def bi_pow(x, y):
            try:
                return x ** y
            except InvalidOperation:
                return ERR.ERR
        def bi_floordiv(x, y):
            try:
                return x // y
            except DivisionByZero:
                return ERR.ERR
        l = parse(E.left)
        r = parse(E.right)
        match E.op:
            case ast.Add():
                return bi_add(l, r)
            case ast.Sub():
                return bi_sub(l, r)
            case ast.Mult():
                return bi_mult(l, r)
            case ast.Div():
                return bi_div(l, r)
            case ast.Mod():
                return bi_mod(l, r)
            case ast.Pow():
                return bi_pow(l, r)
            case ast.FloorDiv():
                return bi_floordiv(l, r)
            case _:
                return ERR.ERR
    def parse_unaryop(E):
        a = parse(E.operand)
        match E.op:
            case ast.UAdd():
                return +a
            case ast.USub():
                return -a
            case _:
                return ERR.ERR
    def parse_call(E):
        if len(E.keywords) != 0:
            return ERR.ERR
        if len(E.args) != 1:
            return ERR.ERR
        try:
            return mm.exported[E.func.id](parse(E.args[0]))
        except KeyError:
            return ERR.ERR
    def parse_assign(E):
        v = parse(E.value)
        for t in E.targets:
            STORE[t.id] = v
        return ''
    match E:
        case ast.Expr():
            return parse(E.value)
        case ast.BinOp():
            return parse_binop(E)
        case ast.UnaryOp():
            return parse_unaryop(E)
        case ast.Constant():
            try:
                return Decimal(string[E.col_offset:E.end_col_offset])
            except InvalidOperation:
                return ERR.ERR
        case ast.Call():
            return parse_call(E)
        case ast.Name(ctx=ast.Load()):
            try:
                return STORE[E.id]
            except KeyError:
                return ERR.ERR
        case ast.Assign():
            return parse_assign(E)
        case ERR.ERR:
            return ERR.ERR
        case _:
            return ERR.ERR
