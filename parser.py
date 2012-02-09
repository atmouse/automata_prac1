#!/usr/bin/env python

from scanner import *
from tokens import *
import sys

global scanner
global token
global all_states

class ParseError(Exception):
    def __init__(self, value, line_num):
        self.value = value
        self.line_num = line_num
    def __str__(self):
        return self.value + ' in line ' + self.line_num + '.'

def automaton():
    token = scanner.get_token()
    if token.ttype == Tokens.TOK_DFA:
        if scanner.get_token().ttype == Tokens.TOK_EQUALS:
            if scanner.get_token().ttype == Tokens.TOK_LPAREN:
                states()
            else:
                raise ParseError('Expected a "("', str(scanner.get_line_num()))
        else:
            raise ParseError('Expected a "="', str(scanner.get_line_num()))
    else:
        raise ParseError('Type of FA not specified, or incorrectly specified', str(scanner.get_line_num()))

def states():
    idset()

def alphabet():
    pass

def tfunction():
    pass

def map():
    pass

def accept():
    pass

def idset():
    if scanner.get_token().ttype == Tokens.TOK_LBRACE:
        id()
    else:
        raise ParseError('Expected a "{"', str(scanner.get_line_num()))

    print token.ttype
    print 'the while'
    #check for zero or more ', id'
    while token.ttype == Tokens.TOK_COMMA:
        print 'inside the while'
        id()

    #print token_names[token.ttype]

    if token.ttype == Tokens.TOK_RBRACE:
        scanner.get_token()

        print token_names[token.ttype]
        print all_states
        sys.exit(0)

        return
    else:
        raise ParseError('Expected a "}"', str(scanner.get_line_num()))


def id():
    token = scanner.get_token()
    if token.ttype == Tokens.TOK_LETTER:
        text = ''
        while (token.ttype == Tokens.TOK_LETTER or token.ttype == Tokens.TOK_DIGIT):
            if token.ttype == Tokens.TOK_LETTER:
                #print token.lexeme
                text = text + token.lexeme
            if token.ttype == Tokens.TOK_DIGIT:
                #print str(token.value)
                text = text + str(token.value)
            token = scanner.get_token()
            #if token.ttype == Tokens.TOK_COMMA:
                #print 'fdfdfd'
        #print token.lexeme
        #print text
        #print 'id() ' + token_names[token.ttype]
        #sys.exit(0)
        if not (text in all_states):
            all_states.append(text)
            print 'PARSER: appended ' +text
            print 'PARSER, id(): ' + token_names[token.ttype]
            return
        else:
            raise ParseError('State ' + text + ' already added', str(scanner.get_line_num()))
    else:
        raise ParseError('Expected a letter', str(scanner.get_line_num()))

def symbol():
    pass

def scan_file(input_file):
    scanner = Scanner(input_file)
    token = Token()
    token = scanner.get_token()
    automaton()
    #if token.ttype == Tokens.TOK_DFA:
    #    parse_dfa(scanner)
    #else:
    #    #TODO throw an exception?
    #    print '\nParserError. Type of FA not specified, or incorrectly specified.\n'
    #    sys.exit(1)

if __name__ == '__main__':
    #scan_file('test1.txt')
    all_states = []
    scanner = Scanner('test1.txt')
    token = Token()
    automaton()

