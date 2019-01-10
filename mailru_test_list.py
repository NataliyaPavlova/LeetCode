#!/usr/bin/python3
'''
Дан большой iterable lst, скажем, xrange(10**10). Напишите код, разворачивающий lst в обратную сторону.
'''
       
class ReverseLst:

    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index-=1
            return self.lst[self.index]
        else:
            raise StopIteration


def my_reverse(lst):
    result = ReverseLst(lst)
    return result
    '''
    with open('data.txt', 'w') as outfile:
        try:
            outfile.write('[{}'.format(next(result)))
            while True: 
                outfile.write(', {}'.format(next(result)))
        except StopIteration:
            outfile.write(']\n')
            print('Fin!')
    '''
def main():
    #lst = [1,2,3,4,5]
    lst = range(10**10)
    the_result = my_reverse(lst)

if __name__=='__main__':
    main()

