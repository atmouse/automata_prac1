'''
    Author: 
        Arne Esterhuizen
        15367940
        arne.esterhuizen@gmail.com

    Description:
        A scanner class which reads in characters from a text file one
        character at a time.
        Returns a token object each time get_token() is called.
        Token objects are defined in tokens.py.

        To create a scanner and begin reading tokens, use the following code:
            
            scanner = Scanner(filename)
            token = Token()
            token = scanner.get_token()
'''

from tokens import *

class ScanError(Exception):
    def __init__(self, value, line_num):
        self.value = value
        self.line_num = line_num
    def __str__(self):
        return self.value + ' in line ' + self.line_num + '.'

class Scanner:
    
    def __init__(self, input_file):
        self.src_file = open(input_file) #open the file to read from
        self.ch = ''
        self.reserved = {'DFA':Tokens.TOK_DFA}
        self.token = Token()
        self.get_char()
        self.line_num = 1
        
    def get_char(self):
        '''
            Return next character from input file.
        '''
        if self.ch == '\n':
            self.line_num = self.line_num + 1
        self.ch = self.src_file.read(1) #read one character
        #print 'SCANNER_READ: ' + self.ch + '\n'

    def get_line_num(self):
        '''
            Return the current line number of the input file.
        '''
        return self.line_num

    def close_file(self):
        self.src_file.close()

    def get_token(self):
        '''
            Return the next token.
        '''
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
            raise ScanError('Illegal character encountered', str(self.get_line_num()))

        return self.token
