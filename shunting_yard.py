### Scratch file used for developing the shunting yard-based parser. 
### No longer current, all current code has moved to fraction_calculator and may have changed.

from fraction_calculator import *

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

input = [Token(digits, '5'), Token(plus, '+'), Token(lparen, '('), Token(digits, '1'), Token(plus, '+'), Token(digits, '2'), Token(mult, '*'), Token(digits, '3'), Token(plus, '+'), Token(digits, '4'), Token(rparen, ')')]

def shunt_parse(input):
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
            
    return output
       
output = shunt_parse(input)       
print output
print output[0]
print 'blergh'
print output[0].data
print output[0].left
print output[0].right

        
### Before ASTs
# input = [Token(digits, '5'), Token(plus, '+'), Token(lparen, '('), Token(digits, '1'), Token(plus, '+'), Token(digits, '2'), Token(mult, '*'), Token(digits, '3'), Token(plus, '+'), Token(digits, '4'), Token(rparen, ')')]

# output = []
# stack = []

# ops = ['+', '-', '*', '/', '//']
# prec = {'+': 1, '-':1, '*': 2, '/': 2, '//': 3}

# for token in input:
    # if is_int(token.text):
        # output.append(token)
    # elif token.text in ops:
        # if len(stack) > 0 and stack[-1].text in ops:
            # while len(stack) > 0 and stack[-1].text in ops and (prec[token.text] <= prec[stack[-1].text]):
                # output.append(stack.pop())
        # stack.append(token)
    # elif token.text == '(':
        # stack.append(token)
    # elif token.text == ')':
        # if len(stack) > 0:
            # while stack[-1].text != '(':
                # output.append(stack.pop())
        # stack.pop()
        
# while len(stack) > 0:
    # output.append(stack.pop())
        
# print output


### Before tokens
# input = ['5', '+', '(', '1', '+', '2', '*', '3', '+', '4', ')']

# output = []
# stack = []

# ops = ['+', '-', '*', '/', '//']
# prec = {'+': 1, '-':1, '*': 2, '/': 2, '//': 3}

# for elem in input:
    # if is_int(elem):
        # output.append(elem)
    # elif elem in ops:
        # if len(stack) > 0 and stack[-1] in ops:
            # while len(stack) > 0 and stack[-1] in ops and (prec[elem] <= prec[stack[-1]]):
                # output.append(stack.pop())
        # stack.append(elem)
    # elif elem == '(':
        # stack.append(elem)
    # elif elem == ')':
        # if len(stack) > 0:
            # while stack[-1] != '(':
                # output.append(stack.pop())
        # stack.pop()
        
# while len(stack) > 0:
    # output.append(stack.pop())
        
# print output