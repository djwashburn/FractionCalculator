FractionCalculator
===================

**Basic description**

A simple calculator for working with infinite precision rational numbers (fraction and integer input), with a handwritten lexer and simple shunting-yard based parser, and a slightly unusual syntax. Written for fun, because my nice, overpriced TI-something calculator was in storage, and because I didn't like the normal input methods for fractions in most programming language REPLs, etc.

**Syntax**

Think classic order of operations: +, -, *, /, (, and ) do what you expect, including precedence. The // operator takes two integers and forms a fraction from them, and has higher precedence than all the other operators (though not parentheses, of course). There is no exponentiation, variable assignment, or other identifiers, nor floats.

**Use**

Just cd into the repo's root directory and run `python fraction_calculator`. A starting prompt will print. After that, enter expressions and they will be evaluated. Type 'exit' to quit, or Ctrl-C (but this may cause weird errors).