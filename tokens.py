
class Tokens:
    TOK_EOF, TOK_EQUALS, TOK_DFA, TOK_LPAREN, TOK_COMMA, TOK_RPAREN, TOK_TRANSITION, TOK_RBRACE, TOK_LBRACE, TOK_ID, TOK_DIGIT = range(11)  
    
class Token:
    def __init__(self):
        self.type = -1
        self.value = 0
        self.lexeme = ''

token_names = {Tokens.TOK_EOF:'end of file', Tokens.TOK_EQUALS:'=', Tokens.TOK_DFA:'DFA', Tokens.TOK_LPAREN:'(', Tokens.TOK_COMMA:',', Tokens.TOK_RPAREN:')', Tokens.TOK_TRANSITION:'->', Tokens.TOK_RBRACE:'}', Tokens.TOK_LBRACE:'{', Tokens.TOK_DIGIT:'digit', Tokens.TOK_ID:'id'}
