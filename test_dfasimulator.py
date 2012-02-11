#!/usr/bin/env python

import dfasimulator

if __name__ == '__main__':
    '''
    print 'Test DFA simulator:\n'
    print 'Commencing with test of test1.txt'
    dfasimulator.main('test1.txt', 'abab') #reject
    dfasimulator.main('test1.txt', 'bababaa')
    dfasimulator.main('test1.txt', 'babab')
    dfasimulator.main('test1.txt', 'baba')
    dfasimulator.main('test1.txt', 'abb') #reject
    dfasimulator.main('test1.txt', 'abba')
    dfasimulator.main('test1.txt', 'baaaa')
    dfasimulator.main('test1.txt', 'ba')
    dfasimulator.main('test1.txt', 'b')
    dfasimulator.main('test1.txt', 'baaaba')

    print '\nCommencing with test of test2.txt'
    dfasimulator.main('test2.txt', '0') #reject
    dfasimulator.main('test2.txt', '000') #reject
    dfasimulator.main('test2.txt', '0000000000000000000000000000') #reject
    dfasimulator.main('test2.txt', '1111111111111111111111111111')
    dfasimulator.main('test2.txt', '1')
    dfasimulator.main('test2.txt', '11')
    dfasimulator.main('test2.txt', '11100010010')  #reject
    dfasimulator.main('test2.txt', '101')
    dfasimulator.main('test2.txt', '010') #reject
    dfasimulator.main('test2.txt', '01010') #reject
    dfasimulator.main('test2.txt', '00111101001100110') #reject
    dfasimulator.main('test2.txt', '001111010011001101')
    
    print '\nCommencing with test of test3.txt'
    dfasimulator.main('test3.txt', '1') #reject
    dfasimulator.main('test3.txt', '11')
    dfasimulator.main('test3.txt', '111') #reject
    dfasimulator.main('test3.txt', '1111')
    dfasimulator.main('test3.txt', '11111')
    dfasimulator.main('test3.txt', '111100')
    dfasimulator.main('test3.txt', '1111000')  #reject
    dfasimulator.main('test3.txt', '1111000011')
    dfasimulator.main('test3.txt', '101011')
    dfasimulator.main('test3.txt', '1110')
    dfasimulator.main('test3.txt', '110') #reject
    '''

    print '\nCommencing with test of test4.txt'
    dfasimulator.main('test4.txt', 'aaaabbbbaa')
