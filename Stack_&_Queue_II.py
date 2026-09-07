## predict the smaller element
def predictsmaller(arr):
    stack=[]
    res=[-1]*len(arr)

    for i in range(len(arr)-1, -1, -1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()

        if stack:
            res[i]=stack[-1]

        stack.append(arr[i])
    return res
print(predictsmaller([4, 5, 2, 10, 8]))

##
            
