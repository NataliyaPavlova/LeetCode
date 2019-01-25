'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ptr=0
        l = len(nums)-1
        while ptr<l:
            if nums[ptr]==0:
                nums.pop(ptr)
                nums.append(0)
                l=l-1
                #print(nums, ptr)
            else: ptr+=1
                
