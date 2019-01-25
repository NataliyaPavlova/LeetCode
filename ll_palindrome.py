'''
Given a singly linked list, determine if it is a palindrome.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Double_ll:
    def __init__(self, node):
        self.val=node.val
        self.next=node.next
        self.prev=None
        
        
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        n=1
        head_dll=Double_ll(head)
        node=head_dll
        prev=None
        while node.next:
            prev, node = node, node.next
            node.prev = prev
            n+=1
        end, node = node, head_dll
        for i in range(n//2):
            if node.val!=end.val:
                return False
            node=node.next
            end=end.prev
        return True
