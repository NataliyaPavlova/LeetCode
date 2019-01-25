'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Could you solve it without converting the integer to a string?
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False
        y=0
        copy_x=x
        while copy_x:
            y=y*10+copy_x%10
            copy_x/=10
        return y==x
