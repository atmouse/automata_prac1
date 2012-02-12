'''
    Author:
        Arne Esterhuizen
        15367940
        arne.esterhuizen@gmail.com

    Description:
        tokens.py defines the Token object, and an enum class for use by the scanner and parser components of the
        DFA simulator.
'''

class Tokens:
    '''
        A quick way of cheating enums into python, since python has no real support for enums.
        This enum class defines token types, so that all characters read in by the scanner object
        may be classified as a special token type. That is, TOK_EQUALS represents the '=' sign, and so on.
    '''
    TOK_EOF, TOK_EQUALS, TOK_DFA, TOK_LPAREN, TOK_COMMA, TOK_RPAREN, TOK_TRANSITION, TOK_RBRACE, TOK_LBRACE, TOK_LETTER, TOK_DIGIT = range(11)  
    
class Token:
    '''
        Token objects are used by the scanner object. For numbers, self.value will be set to the
        value of the number. For text, self.lexeme will be set to the string representation
        of the text. self.ttype is always set to one of the token types  definded in the Tokens class.
    '''
    def __init__(self):
        self.ttype = -1
        self.value = 0
        self.lexeme = ''

#A dictionary containing string representations of the the various token types defined the Tokens class.
token_names = {Tokens.TOK_EOF:'end of file', Tokens.TOK_EQUALS:'=', Tokens.TOK_DFA:'DFA', Tokens.TOK_LPAREN:'(', Tokens.TOK_COMMA:',', Tokens.TOK_RPAREN:')', Tokens.TOK_TRANSITION:'->', Tokens.TOK_RBRACE:'}', Tokens.TOK_LBRACE:'{', Tokens.TOK_DIGIT:'digit', Tokens.TOK_LETTER:'letter'}
