#!/usr/bin/python3
'''sorting'''


class MyList(list):
    '''
    class that inherits from list
    '''
    def print_sorted(self):
        '''sub class'''
        print(sorted(self))
