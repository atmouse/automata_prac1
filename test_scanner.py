#!/usr/bin/env python

'''
    Author:
        Arne Esterhuizen
        15367940
        arne.esterhuizen@gmail.com

    Description:
        A test program for scanner.py.

    Usage:
        python scanner.py
'''

from scanner import *
from tokens import *

def scan_file(input_file):
    print 'Now printing: ' + input_file
    scanner = Scanner(input_file)
    token = Token()
    try:
        while 1:
            token = scanner.get_token()
            if token.ttype == Tokens.TOK_LBRACE:
                print '\n'
            print token_names[token.ttype], 
            if token.ttype == Tokens.TOK_EOF:
                break
    except Exception, message:
        print message
    print '\n\n'

if __name__ == '__main__':
    scan_file('test1.txt')
    scan_file('test2.txt')
    scan_file('test3.txt')
