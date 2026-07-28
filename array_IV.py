## Search in a sorted 2D matrix
# brute force approach
def search_in_2D_matrix(mat,t):
    for i in mat:
        for j in i:
            if j==t:
                return True
    return False
print ("the target element in the matrix is:", search_in_2D_matrix(mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ],t=8))

#optimal solution
def searchMatrix(mat, target):
    if not mat or not mat[0]:
        return False

    n, m = len(mat), len(mat[0])
    low, high = 0, n * m - 1

    while low <= high:
        mid = (low + high) // 2
        row, col = mid // m, mid % m
        val = mat[row][col]

        if val == target:
            return True
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

print(searchMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 8))
print(searchMatrix([[1,2,4],[6,7,8],[9,10,34]], 78))


##Implement Pow(x,n) | X raised to the power N
# by Python's built-in ** operator
def pow(x,n):
    a=x**n
    return a
print("the answer is:", pow(x=2.0000,n=10))

#brute force approach 
def mypow(x,n):
    if n<0:
        x=1/x
        n=-n
    result=1
    for i in range(n):
        result *=x
    return result
print("the answer is:", mypow(x=2.0000,n=10))

#optimal approach
def myPow(x, n):
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n > 0:
        if n % 2 == 1:       # n is odd
            result *= x
            n -= 1
        else:                # n is even
            x *= x
            n //= 2

    return result

print(myPow(2.0, 10))
print(myPow(2.0, -2))   

