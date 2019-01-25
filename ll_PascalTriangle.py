'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
'''
def getRow(rowIndex):
    k=0
    arr=[1]
    while k<rowIndex:
        arr_new=[1]
        for i in range(1,k+1):
            arr_new.append(arr[i-1]+arr[i])
        arr_new.append(1)
        arr=arr_new
        k+=1
    return arr
    

def main():
    k=1
    print(getRow(k))

if __name__=='__main__':
    main()
