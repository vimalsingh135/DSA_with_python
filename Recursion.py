## Subset Sum : Sum of all Subsets by recursion
def subset_sum(index, arr, target, current_sum):
    if index == len(arr):
        return current_sum == target

    # Include the current element in the subset
    include = subset_sum(index + 1, arr, target, current_sum + arr[index])

    # Exclude the current element from the subset
    exclude = subset_sum(index + 1, arr, target, current_sum)

    return include or exclude
print(subset_sum(0, [1, 2, 3], 5, 0))  # Output: True (subset: [2, 3])

## Subset - II | Print all the Unique Subsets by recursion
def unique_subsets(arr):
    n=len(arr)
    arr.sort()
    result = []
    def subsets(index, current_subset):
        result.append(current_subset[:])
        for i in range(index, n):
            if i >n and arr[i] == arr[i-1]:
                continue
            current_subset.append(arr[i])
            subsets(i + 1, current_subset)
            current_subset.pop()

    subsets(0, [])
    return result

print(unique_subsets([1, 2, 2]))