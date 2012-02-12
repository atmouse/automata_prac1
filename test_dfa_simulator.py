#!/usr/bin/env python

'''
    Author:
        Arne Esterhuizen
        15367940
        arne.esterhuizen@gmail.com

    Description:
        A test program for dfa_simulator.py

    Usage:
        python test_dfa_simulator.py
'''

import dfa_simulator

if __name__ == '__main__':
    
    print 'Test DFA simulator:\n'
    print 'Commencing with test of test1.txt'
    dfa_simulator.main('test1.txt', 'abab') #reject
    dfa_simulator.main('test1.txt', 'bababaa')
    dfa_simulator.main('test1.txt', 'babab')
    dfa_simulator.main('test1.txt', 'baba')
    dfa_simulator.main('test1.txt', 'abb') #reject
    dfa_simulator.main('test1.txt', 'abba')
    dfa_simulator.main('test1.txt', 'baaaa')
    dfa_simulator.main('test1.txt', 'ba')
    dfa_simulator.main('test1.txt', 'b')
    dfa_simulator.main('test1.txt', 'baaaba')

    print '\nCommencing with test of test2.txt'
    dfa_simulator.main('test2.txt', '0') #reject
    dfa_simulator.main('test2.txt', '000') #reject
    dfa_simulator.main('test2.txt', '0000000000000000000000000000') #reject
    dfa_simulator.main('test2.txt', '1111111111111111111111111111')
    dfa_simulator.main('test2.txt', '1')
    dfa_simulator.main('test2.txt', '11')
    dfa_simulator.main('test2.txt', '11100010010')  #reject
    dfa_simulator.main('test2.txt', '101')
    dfa_simulator.main('test2.txt', '010') #reject
    dfa_simulator.main('test2.txt', '01010') #reject
    dfa_simulator.main('test2.txt', '00111101001100110') #reject
    dfa_simulator.main('test2.txt', '001111010011001101')
    
    print '\nCommencing with test of test3.txt'
    dfa_simulator.main('test3.txt', '1') #reject
    dfa_simulator.main('test3.txt', '11')
    dfa_simulator.main('test3.txt', '111') #reject
    dfa_simulator.main('test3.txt', '1111')
    dfa_simulator.main('test3.txt', '11111')
    dfa_simulator.main('test3.txt', '111100')
    dfa_simulator.main('test3.txt', '1111000')  #reject
    dfa_simulator.main('test3.txt', '1111000011')
    dfa_simulator.main('test3.txt', '101011')
    dfa_simulator.main('test3.txt', '1110')
    dfa_simulator.main('test3.txt', '110') #reject
    
    print '\nCommencing with test of test4.txt'
    dfa_simulator.main('test4.txt', 'aaaabbbbaa')
    dfa_simulator.main('test4.txt', '')
