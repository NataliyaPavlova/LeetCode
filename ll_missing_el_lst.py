'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''

def missing(nums):
    set_nums=set(nums):
    for i in range(len(nums)+1):
        if i not in set_nums:
            return i
    
nums=[0,2,1,4]
print(missing(nums))
