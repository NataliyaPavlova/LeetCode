'''
You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

'''


def switch_array(i):
    return 1 if i==0 else 0

def main():
    
    arr = [1,2,3,3,4,4,5,5]
    prev=arr[0]
    
    array=[[prev], []]
    i=0
    for el in arr[1:]:
        
        if el>prev+1: return False
        elif el==prev:
            i = switch_array(i)
            array[i].append(el)
            if len(array[i])>1:
                if el!=array[i][-2]+1: return False
        else: array[i].append(el)
        prev=el
        print(array)
    if len(array[0])>=6 and len(array[1])==0: return True 
    if len(array[0])<3 or len(array[1])<3: 
        return False
    return True

if __name__=='__main__':
    print(main())
