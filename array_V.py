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
