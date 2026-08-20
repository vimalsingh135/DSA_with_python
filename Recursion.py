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

## Combination Sum | Print all the combinations that sum to a target by recursion
def combination_sum(arr, target):
    result = []
    arr.sort()
    def backtrack(index, remaining, path):
        if remaining==0:
            result.append(path[:])
            return
        if index==len(arr) or remaining<0:
            return
        if arr[index] <= remaining:
            path.append(arr[index])
            backtrack(index , remaining-arr[index], path)
            path.pop()

        backtrack(index+1, remaining, path)
    backtrack(0, target, [])
    return result
print(combination_sum([2, 3, 6, 7], 7))  
print(combination_sum([2, 3, 5], 8))
print(combination_sum([2], 1))

## combination sum II | Print all the unique combinations that sum to a target by recursion
def combinationSum2(candidates, target):
    candidates.sort()
    res = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return

        for i in range(start, len(candidates)):
            # skip duplicates at this recursion level (not across levels)
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break  # sorted, so everything after is even bigger — prune
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], path)  # i+1: use each number once
            path.pop()

    backtrack(0, target, [])
    return res
print(combinationSum2([10,1,2,7,6,1,5], 8))  # Output: [[1,1,6],[1,2,5],[1,7],[2,6]]