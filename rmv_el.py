'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

''' 

def removeElement(nums, val):
    i=0
    try:
	while nums:
            nums.remove(val)
	    i+=1
    except ValueError:
        return i
    return 0

def main():
    nums = [2,2,3]
    val = 4
    print(nums, removeElement(nums, val))

if __name__=='__main__':
    main()
