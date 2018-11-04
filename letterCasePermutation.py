'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
'''

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        lst=[list(S)]
        for i in range(len(S)):
            if not S[i].isdigit():
                lst = self.add_perm(lst, i)
        
        s = [''.join(element) for element in lst]
        return s
                
    def add_perm(self, lst, i):
        lst_new=[]
        for perm in lst:
            if perm[i].isupper():
                str_new=perm[:]
                str_new[i]=str_new[i].lower()
                lst_new.append(str_new)
            else:
                str_new=perm[:]
                str_new[i]=str_new[i].upper()
                lst_new.append(str_new)
        return lst+lst_new
        
        
