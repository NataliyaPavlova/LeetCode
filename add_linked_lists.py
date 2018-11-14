'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.make_number(l1)
        n2 = self.make_number(l2)
        
        return self.make_ll(n1+n2)
        
    def make_number(self, ll):
        str=''
        while ll:
            str=str+'{}'.format(ll.val)
            ll = ll.next
        return int(str[::-1])
    
    def make_ll(self, number):
        node = ListNode(number%10)
        number//=10
        head=node    
        while number:
            node.next = ListNode(number%10)
            number//=10
            node=node.next
        
        return head
    
