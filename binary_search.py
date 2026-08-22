## Nth Root of a Number using linear Search
def nth_root(m,n):
    for i in range(1,m+1):
        power = i ** n
        if power==m:
            return i
        if i ** n>m:
            break

    return -1
print (nth_root(27,3))  # Output: 3
print (nth_root(16,4))  # Output: 2

## Nth Root of a Number using Binary Search
def func(mid, n, m):
    ans = 1
    for i in range(n):
        ans *= mid
        if ans > m:
            return 2  # too big
    if ans == m:
        return 1      # exact match
    return 0           # too small

def NthRoot(n, m):
    low, high = 1, m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 2:
            high = mid - 1   # mid^n too big, search left
        else:
            low = mid + 1    # mid^n too small, search right
    return -1

# Test cases
print(NthRoot(3, 27))  # 3
print(NthRoot(4, 69))  # -1