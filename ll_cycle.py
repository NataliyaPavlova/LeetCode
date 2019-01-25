'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        
        slow, fast = head, head.next
        while slow.next and fast.next and fast.next.next:
            if slow==fast: return True
            slow=slow.next
            fast=fast.next.next
            
        return False
            
