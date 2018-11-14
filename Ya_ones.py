'''
Find in bin vector the longest sequince of 1 and return its length. Linear time, one-way.
'''


import sys
 
n = int(sys.stdin.readline())
ones=[]
i=0
while n:
    s = sys.stdin.readline()
    if int(s)==1:
        i+=1    
    else:
        if i!=0: ones.append(i)
        i=0
    n-=1
if i!=0: ones.append(i)
if not ones: print(0)
else: print(max(ones))

