'''
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer=0
        roman_dict={'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50, 
                    'C': 100,
                    'D': 500,
                    'M': 1000,
                    'IV': 4,
                    'IX': 9,
                    'XL': 40,
                    'XC': 90,
                    'CD': 400,
                    'CM': 900
                   }
        i=0
        while i<len(s):
            if i+1<len(s) and s[i]+s[i+1] in roman_dict.keys():
                answer+=roman_dict[s[i]+s[i+1]]
                i+=1
            else:
                answer+=roman_dict[s[i]]
            i+=1
            #print(answer)
        return answer
            
