'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

def plus_one(digits):
    integer=int(''.join([str(x) for x in digits]))+1
    answer=[]
    while integer:
        answer.append(integer%10)
        integer//=10    

    return answer[::-1]

def main():
    digits=[1,2,3,9]
    print(plus_one(digits))


if __name__=='__main__':
    main()        
