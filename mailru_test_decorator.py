#!/usr/bin/python3

'''
Напишите декоратор, который считает количество вызовов произвольной функции и при превышении лимита, передаваемого параметром, выбрасывает исключение.
'''

class OverflowError(Exception):
    pass

class CounterDecorator():

    def __init__(self, limit):
        self.calls = 0
        self.limit = limit

    def __call__(self, func):
        def wrap(*args):
            self.calls += 1
            if self.calls>self.limit:
                raise OverflowError('You are off limits.')
            else:
                return func(*args)
        return wrap


@CounterDecorator(3)
def function(a):
    return function(a+1)
    

def main():
    return function(0)

if __name__=='__main__':
    main()    
        

