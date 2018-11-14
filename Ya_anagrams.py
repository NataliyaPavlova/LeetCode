'''
Check if 2 strings are anagrams
'''
import sys
from collections import Counter

string1 = sys.stdin.readline()
string2 = sys.stdin.readline()

print(Counter(string1)==Counter(string2))
