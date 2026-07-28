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

## finding the repeating number and the missing number
## brute force approach 
def rn_and_mn(arr):
    n=len(arr)
    a=[]
    for i in range(1,n+1):
        if arr.count(i)>1 :
            a.append(i)
        if i not in arr:
            a.append(i)
    return a
print("the missing number and the repeating number is " , rn_and_mn(arr=[1,3,3,4,5]))

## optimal approach
def rn_and_mn(arr):
    n = len(arr)
    
    # Expected sum and sum of squares for 1..n
    expected_sum = n * (n + 1) // 2
    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
    
    # Actual sum and sum of squares from arr
    actual_sum = sum(arr)
    actual_sq_sum = sum(x * x for x in arr)
    
    # diff1 = repeating - missing
    diff1 = actual_sum - expected_sum
    
    # diff2 = repeating^2 - missing^2 = (repeating - missing)(repeating + missing)
    diff2 = actual_sq_sum - expected_sq_sum
    
    # sum2 = repeating + missing
    sum2 = diff2 // diff1
    
    repeating = (diff1 + sum2) // 2
    missing = sum2 - repeating
    
    return repeating, missing

print("repeating, missing:", rn_and_mn([1, 3, 3, 4, 5]))

##inversions in an array
## brute force approach  
def inversions(arr):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(i+1,n):
           if arr[i]>arr[j]:
            count+=1
    return count
print("the inversions in an array are", inversions(arr=[1,2,3,4,5]))

## optimal approach
def count_inversions(arr):
    def merge_sort(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_left = merge_sort(a[:mid])
        right, inv_right = merge_sort(a[mid:])
        merged, inv_split = merge(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        merged = []
        i = j = 0
        inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                # left[i] > right[j], so left[i], left[i+1], ..., end of left
                # are ALL greater than right[j] → that's (len(left) - i) inversions
                merged.append(right[j])
                inv_count += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    _, total_inversions = merge_sort(arr)
    return total_inversions

print(count_inversions([1,2,3,4,5]))  # 0
print(count_inversions([5,4,3,2,1]))  # 10
print(count_inversions([5,3,2,1,4]))  # 7
