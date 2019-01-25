'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''

def insert(arr, val):
    l=0
    r=len(arr)-1
    while l<=r:
        med = (l+r)//2
        if val==arr[med]: return med
        elif val<arr[med]:
            r=med-1
        else: l=med+1
    return l
    #print('l={} r={} med={} arr={} val={}'.format(l,r,med, arr, val))

def main():
    arr=[1,3,5,6]
    val = 4
    print(insert(arr, val))
    #return insert(arr, val)


if __name__=='__main__':
    main()
