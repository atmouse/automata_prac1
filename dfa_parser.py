#!/usr/bin/env python

from scanner import *
from tokens import *

if __name__ == '__main__':
    scanner = Scanner("test1.txt")
    token = Token()
    try:
        while 1:
            token = scanner.get_token()
            print token_names[token.type] + '\n'
            if token.type == Tokens.TOK_EOF:
                break
    except Exception, message:
        print message
