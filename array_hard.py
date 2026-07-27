## pascal's triangle 
## Pascal's Triangle - 3 problems in one!
## 1. Element at position (r, c)
## 2. N-th row of Pascal's triangle
## 3. First N rows of Pascal's triangle

## Pascal's triangle logic:
## each element = C(r-1, c-1) = (r-1)! / ((c-1)! * (r-c)!)
## but easier way: each element = previous element * (r-c) / c

def ncr(n, r):
    # calculate nCr = n! / (r! * (n-r)!)
    # optimized: multiply and divide simultaneously
    result = 1
    for i in range(r):
        result = result * (n - i)
        result = result // (i + 1)
    return result

## Problem 1: Element at position (r, c)
def element_at_position(r, c):
    # element at row r, col c = C(r-1, c-1)
    return ncr(r - 1, c - 1)

## Problem 2: N-th row of Pascal's triangle
def nth_row(n):
    row = []
    result = 1
    row.append(1)
    for i in range(1, n):
        result = result * (n - i)
        result = result // i
        row.append(result)
    return row

## Problem 3: First N rows of Pascal's triangle
def first_n_rows(n):
    triangle = []
    for i in range(1, n + 1):
        triangle.append(nth_row(i))
    return triangle


## --- Test ---
N = 8
r = 7
c = 5

print(f"Element at position (r, c): {element_at_position(r, c)}")

print(f"N-th row of Pascal's triangle:", *nth_row(N))

print("First n rows of Pascal's triangle:")
for row in first_n_rows(N):
    print(*row)


## find the Duplicated number
#bruth force code
def f_duplicated_num(arr):
    n=len(arr)
    for i in range(1, n):
        if arr.count(i)>1:
            return i
    
    return "no duplicate number is present in the given array"

print("the duplicate number is this", f_duplicated_num(arr=[1, 3, 4, 2, 2])) 

## optimal approach
def f_duplicated_num(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return "no duplicate number is present in the given array"