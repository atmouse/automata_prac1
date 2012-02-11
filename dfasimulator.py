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
    global alphabet_counter
    
    if not (sym in alphabet_symbols):
        alphabet_symbols[sym] = alphabet_counter
        alphabet_counter += 1
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
    else:
        raise ParseError('You are trying to set an unknown state as a start state', str(scanner.get_line_num()))
    return

def tfunction():
    global token

    #initialize transition matrix as a two-dimensional python list
    for i in xrange(len(alphabet_symbols)):
        t_matrix.append([])
        for j in xrange(len(all_states)):
            t_matrix[-1].append(-1)

    #the expected number of transitions
    exp_num_transitions = len(alphabet_symbols) * len(all_states)
    #the actual number of transitoins
    act_num_transitions = 0

    if scanner.get_token().ttype == Tokens.TOK_LBRACE:
        act_num_transitions += 1
        map()
    else:
        raise ParseError('Expected a "{"', str(scanner.get_line_num()))

    #check for zero or more ', symbol'
    while token.ttype == Tokens.TOK_COMMA:
        act_num_transitions += 1
        map()

    if token.ttype == Tokens.TOK_RBRACE:
        if not (exp_num_transitions == act_num_transitions):
            raise ParseError('Every state of a DFA must have a next state for every input symbol', str(scanner.get_line_num()))
        scanner.get_token()       
        return
    else:
        raise ParseError('Expected a "}"', str(scanner.get_line_num()))
  
def map():
    global token
    
    if scanner.get_token().ttype == Tokens.TOK_LPAREN:
        src_state = id()

        src_state_index  = all_states[src_state]

        if token.ttype == Tokens.TOK_COMMA:
            pass
        else:
            raise ParseError('Expected a ","', str(scanner.get_line_num()))

        sym = symbol()

        symbol_index = alphabet_symbols[sym]

        if token.ttype == Tokens.TOK_RPAREN:
            pass
        else:
            raise ParseError('Expected a ")"', str(scanner.get_line_num()))
        
    else:
        raise ParseError('Expected a "("', str(scanner.get_line_num()))

    if scanner.get_token().ttype == Tokens.TOK_TRANSITION:
        dst_state = id()

        dst_state_index = all_states[dst_state]
    else:
        raise ParseError('Expected a "->"', str(scanner.get_line_num()))

    #add this map to the transition matrix
    if t_matrix[symbol_index][src_state_index] < 0:
        #If the index where this transition's destination state index is to be stored
        #is >= 0, then a destination state index has already been assigned
        #here. It means that for this state, the same alphabet symbol leads out
        #to two different states, which is not allowed.
        t_matrix[symbol_index][src_state_index] = dst_state_index
    else:
        raise ParseError('A next state for "' + src_state + '" using symbol "' + sym + '" has already been assigned', str(scanner.get_line_num()))
    return

def accept():
    idset(add_accept_state)

def add_state(state):
    global states_counter
    
    if not (state in all_states):
        all_states[state] = states_counter
        states_counter += 1
        return
    else:
        raise ParseError('State ' + state + ' already added', str(scanner.get_line_num()))

def add_accept_state(state):
    if not (state in accept_states):
        if state in all_states:
            accept_states.append(all_states[state])
        else:
            raise ParseError('You are trying to set an unknown state as an accept state', str(scanner.get_line_num()))
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
        return text
    else:
        raise ParseError('Expected a letter', str(scanner.get_line_num()))
    
def symbol():
    global token

    #TODO does symbol react correctly to symbols with length greater than one?
    token = scanner.get_token()
    if token.ttype == Tokens.TOK_DIGIT:
        num = token.value      
        if len(str(num)) > 1:
            raise ParseError('Expected a single digit or letter', str(scanner.get_line_num()))
        token = scanner.get_token()
        return str(num)
    elif token.ttype == Tokens.TOK_LETTER:
        text = token.lexeme
        if len(text) > 1:
            raise ParseError('Expected a single digit or letter', str(scanner.get_line_num()))
        token = scanner.get_token()
        return text
    else:
        raise ParseError('Expected a letter or a digit', str(scanner.get_line_num()))

def simulate_dfa(input_string):
    current_index = all_states[start_state]
    
    if input_string == '':
        #the dfa accepts the empty string if the start state is an accept state
        if current_index in accept_states:
            print 'accept'
        else:
            print 'reject'
        return
    
    for s in input_string:
        try:
            num = t_matrix[alphabet_symbols[s]][current_index]
        except KeyError:
            raise Exception('Input string consists of invalid symbols for this DFA\'s alphabet')
        if num >= 0:
            current_index = num
    if current_index in accept_states:
        print 'accept'
    else:
        print 'reject'

def main(filename, test_string):    
    global t_matrix #transition matrix
    global alphabet_counter
    global states_counter
    global accept_states
    global start_state
    global all_states
    global alphabet_symbols
    global scanner
    global token
    t_matrix = []
    states_counter = 0
    alphabet_counter = 0
    accept_states = []
    start_state = ''
    all_states = {}
    alphabet_symbols = {}
    scanner = Scanner(filename)
    token = Token()
    
    automaton()
    simulate_dfa(test_string)

if __name__ == '__main__':
    filename = sys.argv[1]
    test_string = sys.argv[2]
    main(filename, test_string)
    '''
    global t_matrix #transition matrix
    global alphabet_counter
    global accept_states
    global start_state
    global all_states
    global alphabet_symbols
    global scanner
    global token
    t_matrix = []
    states_counter = 0
    alphabet_counter = 0
    accept_states = []
    start_state = ''
    all_states = {}
    alphabet_symbols = {}
    scanner = Scanner('test1.txt')
    token = Token()
    
    automaton()

    simulate_dfa('abab') #reject
    simulate_dfa('bababaa')
    simulate_dfa('babab')
    simulate_dfa('baba')
    simulate_dfa('abb') #reject
    simulate_dfa('abba')
    simulate_dfa('baaaa')
    simulate_dfa('ba')
    simulate_dfa('b')
    simulate_dfa('baaaba')
    '''
    
