#!/usr/bin/env python

from scanner import *
from tokens import *
import sys

def parse_dfa(scanner):
    pass

def scan_file(input_file):
    scanner = Scanner(input_file)
    token = Token()
    token = scanner.get_token()
    if token.ttype == Tokens.TOK_DFA:
        parse_dfa(scanner)
    else:
        print '\nParserError. Type of FA not specified, or incorrectly specified.\n'
        sys.exit(1)

if __name__ == '__main__':
    scan_file('test4.txt')
