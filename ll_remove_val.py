'''
Remove all elements from a linked list of integers that have value val.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val==val:
            head=head.next
            
        node = head
        while node:
            while node.next and node.next.val==val:
                node.next=node.next.next
            node=node.next
        
        return head    
