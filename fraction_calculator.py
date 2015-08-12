from rational import *

### Constants:
# Token kinds:
lparen = 'lparen'
rparen = 'rparen'
frac_bar = 'frac_bar'
mult = 'mult'
div = 'div'
plus = 'plus'
minus = 'minus'
digits = 'digits'

class Token:
    def __init__(self, kind, text):
        self.kind = kind
        self.text = text
        
    def __str__(self):
        return '<' + self.kind + ', ' + self.text + '>'
    
    def __repr__(self):
        return 'Token(' + repr(self.kind) + ', ' + repr(self.text) + ')'
        
class btree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        
    def __str__(self, level=0):
        ret = "\t"*level + repr(self.data) + "\n"
        if self.left and type(self.left) == btree:
            ret += self.left.__str__(level+1)
        if self.right and type(self.right) == btree:
            ret += self.right.__str__(level+1)
        return ret
        
def is_int(_str):
    try:
        int(_str)
        return True
    except:
        return False

def pre():
    print "Welcome to fraction calculator! Enter a math expression (excluding exponentiation, allowing fractions like 1//2 (meaning one half), and not allowing decimals/floats."

def post():
    pass
    
def lexer(string):
    """ String -> list(Token)
        Takes a line of input cleared of whitespace and returns the lexed result."""
    
    lexed = []
    next_token = ['', ''] # left side is kind, right side is text
    # Build up a token until its fully identified. When it is, fill in its left side and return.
    for i, char in enumerate(string):
        digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if char == '(':
            next_token = (lparen, char)
        elif char == ')':
            next_token = (rparen, char)
        elif char == '*':
            next_token = (mult, char)
        elif char == '+':
            next_token = (plus, char)
        elif char == '-':
            if i+1 == len(string):
                next_token = (minus, char)
            elif string[i+1] in digit_list:
                next_token[1] += char
            else:
                next_token = (minus, char)
        elif char == '/':
            if i+1 == len(string):
                next_token = (div, char)
            elif string[i+1] == '/':
                next_token[1] += char
            elif string[i+1] != '/' and next_token[1] == '':
                next_token = (div, char)
            elif string[i+1] != '/' and next_token[1] == '/':
                next_token[1] += char
                next_token[0] = frac_bar
            else:
                raise(Exception)
        elif char in digit_list:
            next_token[1] += char
            if i+1 == len(string):
                next_token[0] = digits
            elif string[i+1] not in digit_list:
                next_token[0] = digits
        else:
            raise(Exception)
         
        if next_token[0] != '':
            lexed.append(Token(next_token[0], next_token[1]))
            next_token = ['', '']
    
    ### Printout of various verions of lexed input
    # print repr([token.text for token in lexed])
    # print ', '.join(str(v) for v in lexed)
    # print repr(lexed)
    
    return lexed
    
def parse(input):
    output = []
    stack = []

    ops = ['+', '-', '*', '/', '//']
    prec = {'+': 1, '-':1, '*': 2, '/': 2, '//': 3}

    def build_tree():
        op = stack.pop()
        r = output.pop()
        if type(r) == btree:
            right = r
        else:
            right = btree()
            right.data = r
        l =  output.pop()
        if type(l) == btree:
            left = l
        else:
            left = btree()
            left.data = l
        tree = btree()
        tree.left = left
        tree.right = right
        tree.data = op
        return tree

    for token in input:
        if is_int(token.text):
            output.append(token)
        elif token.text in ops:
            if len(stack) > 0 and stack[-1].text in ops:
                while len(stack) > 0 and stack[-1].text in ops and (prec[token.text] <= prec[stack[-1].text]):
                    output.append(build_tree())
            stack.append(token)
        elif token.text == '(':
            stack.append(token)
        elif token.text == ')':
            if len(stack) > 0:
                while stack[-1].text != '(':
                    output.append(build_tree())
            stack.pop()
            
    while len(stack) > 0:
        output.append(build_tree())
            
    return output[0]
    
def run_ast(ast):
    # Takes a btree binary tree with leaf nodes that have tokens as their `data` attribute
    if ast.data.kind == digits:
        try:
            return int(ast.data.text)
        except:
            raise(Exception("Parse error: digits could not be converted to int"))
    elif ast.data.kind == frac_bar:
        l = run_ast(ast.left)
        r = run_ast(ast.right)
        if isinstance(l, int) and isinstance(r, int):
            return Rational(l, r)
        else:
            #raise(Exception("Syntax error. // takes an integer on the left and an integer on the right."))
            raise(Exception("Error: // only valid with integer operands"))
    elif ast.data.kind == mult:
        l = run_ast(ast.left)
        r = run_ast(ast.right)
        try:
            return l * r
        except:
            raise(Exception("Error multiplying"))
    elif ast.data.kind == div:
        l = run_ast(ast.left)
        r = run_ast(ast.right)
        try:
            return l / r
        except:
            raise(Exception("Error dividing"))
    elif ast.data.kind == plus:
        l = run_ast(ast.left)
        r = run_ast(ast.right)
        try:
            return l + r
        except:
            raise(Exception("Error adding"))
    elif ast.data.kind == minus:
        l = run_ast(ast.left)
        r = run_ast(ast.right)
        try:
            return l - r
        except:
            raise(Exception("Error subtracting"))
    else:
        raise(Exception("Parsing error"))
    
def interpret(input):
    # Should take string input and return true if we should keep going, false otherwise
    if input == 'exit':
        return False
    lexed = lexer(input)
    parsed = parse(lexed)
    
    ### Print parse tree
    #print str(parsed)
    
    ast = parsed
    
    print run_ast(ast)
    return True
    
def loop():
    ret = True
    while ret:
        input = raw_input()
        input = "".join(input.split())
        ret = interpret(input)

if __name__ == '__main__':
    pre()
    loop()
    post()