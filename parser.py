#!/usr/bin/env python

from scanner import *
from tokens import *
import sys

class ParseError(Exception):
    def __init__(self, value, line_num):
        self.value = value
        self.line_num = line_num
    def __str__(self):
        return self.value + ' in line ' + self.line_num + '.'

def automaton():
    global token
    token = scanner.get_token()
    if token.ttype == Tokens.TOK_DFA:
        if scanner.get_token().ttype == Tokens.TOK_EQUALS:
            if scanner.get_token().ttype == Tokens.TOK_LPAREN:
                pass
            else:
                raise ParseError('Expected a "("', str(scanner.get_line_num()))
            states()
            if token.ttype == Tokens.TOK_COMMA:
                pass
            else:
                raise ParseError('Expected a ","', str(scanner.get_line_num()))
            alphabet()
            if token.ttype == Tokens.TOK_COMMA:
                pass
            else:
                raise ParseError('Expected a ","', str(scanner.get_line_num()))
            tfunction()
            if token.ttype == Tokens.TOK_COMMA:
                pass
            else:
                raise ParseError('Expected a ","', str(scanner.get_line_num()))
            start()
            if token.ttype == Tokens.TOK_COMMA:
                pass
            else:
                raise ParseError('Expected a ","', str(scanner.get_line_num()))
            accept()
            if token.ttype == Tokens.TOK_RPAREN:
                print 'parsing successful'
                scanner.close_file()
            else:
                raise ParseError('Expected a ")"', str(scanner.get_line_num()))
            
        else:
            raise ParseError('Expected a "="', str(scanner.get_line_num()))
    else:
        raise ParseError('Type of FA not specified, or incorrectly specified', str(scanner.get_line_num()))

def states():
    idset(add_state)

def add_alpha(sym):
    if not (sym in alphabet_symbols):
        alphabet_symbols.append(sym)
    else:
        raise ParseError('Symbol ' + sym + ' already added', str(scanner.get_line_num()))

def alphabet():
    global token

    if scanner.get_token().ttype == Tokens.TOK_LBRACE:
        sym = symbol()
        add_alpha(sym)
    else:
        raise ParseError('Expected a "{"', str(scanner.get_line_num()))

    #check for zero or more ', symbol'
    while token.ttype == Tokens.TOK_COMMA:
        sym = symbol()
        add_alpha(sym)

    if token.ttype == Tokens.TOK_RBRACE:
        scanner.get_token()
        return
    else:
        raise ParseError('Expected a "}"', str(scanner.get_line_num()))
    
def start():
    global start_state

    state = id()
    if state in all_states:
        start_state = state
    return

def tfunction():
    global token

    if scanner.get_token().ttype == Tokens.TOK_LBRACE:
        map()
    else:
        raise ParseError('Expected a "{"', str(scanner.get_line_num()))

    #check for zero or more ', symbol'
    while token.ttype == Tokens.TOK_COMMA:
        map()

    if token.ttype == Tokens.TOK_RBRACE:
        scanner.get_token()
        return
    else:
        raise ParseError('Expected a "}"', str(scanner.get_line_num()))

def map():
    #TODO implement transition function
    global token
    
    if scanner.get_token().ttype == Tokens.TOK_LPAREN:
        id()

        if token.ttype == Tokens.TOK_COMMA:
            pass
        else:
            raise ParseError('Expected a ","', str(scanner.get_line_num()))

        symbol()

        if token.ttype == Tokens.TOK_RPAREN:
            pass
        else:
            raise ParseError('Expected a ")"', str(scanner.get_line_num()))
        
    else:
        raise ParseError('Expected a "("', str(scanner.get_line_num()))

    if scanner.get_token().ttype == Tokens.TOK_TRANSITION:
        id()
    else:
        raise ParseError('Expected a "->"', str(scanner.get_line_num()))

def accept():
    idset(add_accept_state)

def add_state(state):
    if not (state in all_states):
        all_states.append(state)
        return
    else:
        raise ParseError('State ' + state + ' already added', str(scanner.get_line_num()))

def add_accept_state(state):
    if not (state in accept_states):
        accept_states.append(state)
        return
    else:
        raise ParseError('State ' + state + ' already added', str(scanner.get_line_num())) 

def idset(function):
    global token
    
    if scanner.get_token().ttype == Tokens.TOK_LBRACE:
        state = id()
        function(state)
    else:
        raise ParseError('Expected a "{"', str(scanner.get_line_num()))

    #check for zero or more ', id'
    while token.ttype == Tokens.TOK_COMMA:
        state = id()
        function(state)

    if token.ttype == Tokens.TOK_RBRACE:
        scanner.get_token()
        return
    else:
        raise ParseError('Expected a "}"', str(scanner.get_line_num()))


def id():
    global token

    token = scanner.get_token()
    if token.ttype == Tokens.TOK_LETTER:
        text = ''
        while (token.ttype == Tokens.TOK_LETTER or token.ttype == Tokens.TOK_DIGIT):
            if token.ttype == Tokens.TOK_LETTER:
                text = text + token.lexeme
            if token.ttype == Tokens.TOK_DIGIT:
                text = text + str(token.value)
            token = scanner.get_token()
        '''
        if not (text in all_states):
            all_states.append(text)
            return
        else:
            raise ParseError('State ' + text + ' already added', str(scanner.get_line_num()))
        '''
        return text
    else:
        raise ParseError('Expected a letter', str(scanner.get_line_num()))
    
def symbol():
    global token

    token = scanner.get_token()
    if token.ttype == Tokens.TOK_DIGIT:
        num = token.value
        token = scanner.get_token()
        return num
    elif token.ttype == Tokens.TOK_LETTER:
        text = token.lexeme
        token = scanner.get_token()
        return text
    else:
        raise ParseError('Expected a letter or a digit', str(scanner.get_line_num()))

if __name__ == '__main__':
    global accept_states
    global start_state
    global all_states
    global alphabet_symbols
    global scanner
    global token
    accept_states = []
    start_state = ''
    all_states = []
    alphabet_symbols = []
    scanner = Scanner('test1.txt')
    token = Token()
    automaton()

