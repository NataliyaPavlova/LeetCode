'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here
'''


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dct = {letter: s.count(letter) for letter in set(s)}
        odd = 0
        pal = '1'
        for letter,val in dct.items():
            if val%2 and odd==0:
                odd==0
                i = pal.find('1')
                pal = pal[:i]+letter*val+pal[i+1:]
                odd=1
            else:
                pal = letter*(val//2) + pal + letter*(val//2)

        return len(pal.replace('1',''))
                    
        
        
