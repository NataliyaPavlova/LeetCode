'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        
        while node:
            temp = node
            while temp.next and temp.val==temp.next.val:
                temp = temp.next
            node.next=temp.next
            node=node.next
        return head
