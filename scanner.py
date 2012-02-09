#!/usr/bin/env python

from tokens import *

class Scanner:
    
    def __init__(self, input_file):
        self.src_file = open(input_file) #open the file to read from
        self.ch = ''
        self.reserved = {'DFA':Tokens.TOK_DFA}
        self.token = Token()
        self.get_char()
        
    def get_char(self):
        self.ch = self.src_file.read(1) #read one character

    def get_token(self):
        
        while (self.ch.isspace()):
            self.get_char()

        if self.ch.isalpha():
            text = ''
            while (not self.ch.isspace()) and self.ch.isalpha():
                text = text + self.ch
                self.get_char()
            if text in self.reserved.keys():
                self.token.ttype = self.reserved[text]
            else:
                self.token.ttype = Tokens.TOK_LETTER
                self.token.lexeme = text
        elif self.ch.isdigit():
            num = 0
            while self.ch.isdigit():
                num = num * 10 + int(self.ch)
                self.get_char()
            self.token.ttype = Tokens.TOK_DIGIT
            self.token.value = num
        elif self.ch == '=':
            self.token.ttype = Tokens.TOK_EQUALS
            self.get_char()
        elif self.ch == '(':
            self.token.ttype = Tokens.TOK_LPAREN
            self.get_char()
        elif self.ch == ')':
            self.token.ttype = Tokens.TOK_RPAREN
            self.get_char()
        elif self.ch == '{':
            self.token.ttype = Tokens.TOK_LBRACE
            self.get_char()
        elif self.ch == '}':
            self.token.ttype = Tokens.TOK_RBRACE
            self.get_char()
        elif self.ch == ',':
            self.token.ttype = Tokens.TOK_COMMA
            self.get_char()
        elif self.ch == '-':
            self.get_char()
            if self.ch == '>':
                self.token.ttype = Tokens.TOK_TRANSITION
            self.get_char()
        elif self.ch == '':
            self.token.ttype = Tokens.TOK_EOF
        else:
            raise Exception('ScannerError', 'Illegal character encountered.')
        return self.token

if __name__ == '__main__':
    pass
