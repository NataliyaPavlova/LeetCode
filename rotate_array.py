'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        #make linked list
        head = ListNode(nums[0])
        node = head
        
        for i in range(1,n):
            node.next = ListNode(nums[i])
            node = node.next
        node.next = head
        
        #make returned array
        k = n-k if k<=n else 2*n-k
        while k>0:
            head = head.next
            k-=1
            
        for i in range(n):
            nums[i] = head.val
            head=head.next
            
        
