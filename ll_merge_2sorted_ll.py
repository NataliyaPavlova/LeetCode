'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        root = ListNode(0)
        ptr = root
        ptr1, ptr2 = l1, l2
        
        while ptr1 and ptr2:
            if ptr1.val<ptr2.val:
                ptr.next = ptr1
                ptr=ptr.next
                ptr1 = ptr1.next
            else:
                ptr.next=ptr2
                ptr=ptr.next
                ptr2=ptr2.next
        if ptr1:
            ptr.next = ptr1
        elif ptr2:
            ptr.next = ptr2
        return root.next
    
