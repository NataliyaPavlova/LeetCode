'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

def remove_dupl(nums):
    l=len(nums)
    i=0
    while i<l:
        while i+1<len(nums) and nums[i+1]==nums[i]:
            nums.pop(i+1)
            l-=1
        i+=1
    return len(nums)


nums=[1,1,1]#,0,0,0,1,1,1,1,2,2,2,2,3,3,4,4,5,6,6,6]
remove_dupl(nums)
