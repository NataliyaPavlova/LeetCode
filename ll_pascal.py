'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''
def pascal_triangle(numRows):

    if numRows==0:
        return []
    elif numRows==1:
        return [[1]]
    elif numRows==2:
        return [[1],[1,1]] 

    pascal=[[1],[1,1]]
    k=2
    while k<numRows:
        row=[1]
        for i in range(1,k):
            row.append(pascal[-1][i-1]+pascal[-1][i])
        row.append(1)
        pascal.append(row)
        k+=1
    return pascal

print(pascal_triangle(5))
