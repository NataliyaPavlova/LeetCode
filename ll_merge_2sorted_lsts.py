'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
'''

def merge(nums1, m, nums2, n):
    nums1[m+n:]=nums1[0:m]
    i1, i2 = m+n, 0
    i=0
    while i1<m+m+n and i2<n:
        if nums1[i1]<nums2[i2]:
            nums1[i]=nums1[i1]
            i1+=1
        else:
            nums1[i]=nums2[i2]
            i2+=1
        i+=1
    if i1>=m+m+n+1:
        nums1[i:]=nums2[i2:]
    elif i2>=n:
        nums1[i:]=nums1[i1:]

nums1=[2,2,4,0,0,0]
nums2=[1,3,4]
merge(nums1, 3, nums2, 3)
print(nums1)
