'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

def strStr(haystack, needle):
    if not needle: return 0 
    for index in range(len(haystack)-len(needle)+1):
        if haystack[index]==needle[0]:
            if haystack[index:index+len(needle):]==needle:
                return index
    return -1
    
def main():
    haystack='abresgvk'
    needle='sgv'
    print(strStr(haystack, needle))

if __name__=='__main__':
    main()
