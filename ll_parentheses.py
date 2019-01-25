'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
def revert(symbol):
    dct = {'[':']',
           '(':')',
           '{':'}'
          }
    return dct[symbol] 


def isValid(s):
    stek_parentheses=[]
    for parenthes in s:
        if any(opens==parenthes for opens in ['(','[','{']):
            stek_parentheses.append(parenthes)
        else:
            if revert(stek_parentheses[-1])==parenthes:
                stek_parentheses.pop(-1)
            else: return False
    return len(stek_parentheses)==0

def main():
    s='()[]{{}}'
    print(isValid(s))

if __name__=='__main__':
    main()
