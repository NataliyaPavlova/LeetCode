'''
Print all proper brackets sequenses in lexicographically order.

'''

import sys
 
def rec(opens, closes, ans, n):
    print('i am in rec, opens={}, closes={}, ans={}'.format(opens, closes, ans))
    if opens+closes==2*n:
        print(ans)
        return 0
    if opens<n:
        rec(opens+1, closes, ans+'(', n)
    if opens>closes:
        rec(opens, closes+1, ans+')', n)
    

def main():
    #n = int(sys.stdin.readline())    
    rec(0,0,'',2)
    return 0

if __name__=='__main__':
    main()    

