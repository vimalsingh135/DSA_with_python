## two sum problem
def two_sum(arr,target):
    n=len(arr)
    for i in range (n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return True
    return False
print("the two sum is", two_sum(arr=[2,6,5,8,11],target=14))

## optimal approach
def two_sum_with_tp(arr, t):
    arr.sort()
    x,y=0,len(arr)-1
    while x<y:
        current_sum=arr[x]+arr[y]
        if current_sum==t:
            return True
        elif current_sum<t:
            x+=1
        else:
            y-=1
print("the two sum is", two_sum(arr=[2,6,5,8,11],target=14))

## 4 sum problem 
def four_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range (i+2,n):
                for l in range(i+3,n):
                    if arr[i]+arr[j]+arr[k]+arr[l]==target:
                        return True
    return False
print("the 4 sum is :", four_sum(arr=[1,0,-1,0,-2,2],target=0))

#optimal solution
def fourSum(arr, target):
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            left, right = j+1, n-1
            while left < right:
                total = arr[i] + arr[j] + arr[left] + arr[right]
                if total == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result


##Longest Consecutive Sequence in an Array
def longest_consecutives(arr):
   n=set(arr)
   longest=0
   for i in n:
       if i-1 not in n:
           current=i
           length=1
           while current+1 in n:
               current+=1
               length+=1

           longest=max(longest,length)

   return longest 
print ("the longest consecutive sequence is :", longest_consecutives(arr=[100, 4, 200, 1, 3, 2]))

## Length of the longest subarray with zero Sum
def longest_subarray_zero_sum_bruteforce(arr):
    n = len(arr)
    max_len = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)
    return max_len
print("Length of the longest subarray with zero Sum is:",longest_subarray_zero_sum_bruteforce(arr=[9, -3, 3, -1, 6, -5]))

#optimal approach
def longest_subarray_zero_sum(arr):
    prefix_sum_index = {}  # maps prefix_sum -> first index it occurred at
    curr_sum = 0
    max_len = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == 0:
            max_len = i + 1  # whole subarray from 0 to i sums to zero

        if curr_sum in prefix_sum_index:
            # same prefix sum seen before -> subarray between them sums to 0
            length = i - prefix_sum_index[curr_sum]
            max_len = max(max_len, length)
        else:
            # only store the FIRST occurrence -> gives the longest possible subarray
            prefix_sum_index[curr_sum] = i

    return max_len

print(longest_subarray_zero_sum([9, -3, 3, -1, 6, -5]))  

