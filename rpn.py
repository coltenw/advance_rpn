#!/usr/bin/env python3

import readline
from pygments.lexers import Python3Lexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.lexers import PygmentsLexer
from pygments.styles import get_style_by_name
from prompt_toolkit.styles.pygments import style_from_pygments_cls
from pygments.token import Token
from pygments.style import Style
from pygments import highlight
from pygments.formatters import Terminal256Formatter

class MyStyle(Style):
    styles = {
        Token.Number: '#ansiblue',
        Token.Operator: '#ansiyellow'
    }

def calculate(arg):
    stack = []

    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val1 - val2
            elif token == '*':
                result = val1 * val2
            
            stack.append(result)
            if len(stack) > 1:
                raise ValueError('Too many arguments on the stack')

    return stack[0]

def main():
    while True:
        try:
            style = style_from_pygments_cls(get_style_by_name('monokai'))
            result = calculate(prompt('rpn calc> ', lexer=PygmentsLexer(Python3Lexer), style=style, include_default_pygments_style=False))
            out = highlight(str(result), Python3Lexer(), Terminal256Formatter(style=get_style_by_name('monokai')))
            print(out)
        except ValueError:
            pass

if __name__== '__main__':
    main()
