'''

Sorted 32-bit integers. Delete all repeated elements.
Try to get a decision which doesn't take the whole file into the memory, but takes constant memory usage.
'''
#run-time error

import sys
 
n = int(sys.stdin.readline())
with open ('output.txt','w') as f:
    if n<=0: 
        prev=''
        f.write('{}\n'.format(prev))

    else:
        prev =int(sys.stdin.readline())
        f.write('{}\n'.format(prev))

        while n-1:
            s = sys.stdin.readline()
            if int(s)!=prev:
	        f.write('{}\n'.format(int(s)))
	        prev=int(s)
            n-=1


