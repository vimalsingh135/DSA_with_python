class solution:
    def heaps(self):
        self.heap=[]

    def insert(self, value):
        self.heap.append(value)
        self._shiftUp(len(self.heap)-1)

    def changeValue(self, index, newValue):
        oldValue=self.heap[index]
        self.heap[index]=newValue
        if newValue>oldValue:
            self._shiftUp(index)
        else:
            self._sdhiftDown(index)
    def extractMax(self):
        if len(self.heap)==0:
            return None
        maxValue=self.heap[0]
        self.heap[0]=self.heap[-1]
        self.heap.pop()
        self._shiftDown(0)
        return maxValue
    def isempty(self):
        return len(self.heap)==0
    def getmax(self):
        return self.heap[0] if self.heap else None
    def heapsize(self):
        return len(self.heap)

    def _shiftUp(self, index):
        while index>0:
            parent=(index-1)//2
            if self.heap[index]>self.heap[parent]:
                self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
                index=parent
            else:
                break
    def _shiftDown(self, index):
        size=len(self.heap)
        while index<size:
            left=2*index+1
            right=2*index+2
            largest=index
            if left<size and self.heap[left]>self.heap[largest]:
                largest=left
            if right<size and self.heap[right]>self.heap[largest]:
                largest=right
            if largest!=index:
                self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
                index=largest
            else:
                break

print("Heap Implementation")
heap=solution()

## k-th largest/smallest element in an array 
import heapq
def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
print (findKthLargest([3,2,1,5,6,4], 2))  # Output: 5
print (findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # Output: 4

## Maximum Sum Combination
## brute force approach: generate all possible sums and sort them to get the k largest sums. This approach has a time complexity of O(n^2 log n) due to sorting.
def maxSumCombination(arr1, arr2, k):
    min_heap = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            total = arr1[i] + arr2[j]
            heapq.heappush(min_heap, total)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
    return sorted(min_heap, reverse=True)

print(maxSumCombination([1, 4, 5], [2, 3, 6], 3))  # [11, 10, 8]
print(maxSumCombination([1, 2], [3, 4], 2))          # [6, 5]

## optimized approach: use a max heap to keep track of the k largest sums. This approach has a time complexity of O(k log k) since we only maintain a heap of size k.
def maxSumCombinationOptimized(arr1, arr2, k):
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    max_heap = []
    visited = set()
    
    heapq.heappush(max_heap, (-(arr1[0] + arr2[0]), 0, 0))
    visited.add((0, 0))
    
    result = []
    
    while len(result) < k:
        current_sum, i, j = heapq.heappop(max_heap)
        result.append(-current_sum)
        
        if i + 1 < len(arr1) and (i + 1, j) not in visited:
            heapq.heappush(max_heap, (-(arr1[i + 1] + arr2[j]), i + 1, j))
            visited.add((i + 1, j))
        
        if j + 1 < len(arr2) and (i, j + 1) not in visited:
            heapq.heappush(max_heap, (-(arr1[i] + arr2[j + 1]), i, j + 1))
            visited.add((i, j + 1))
    
    return result

## Find Median from Data Stream
import heapq
class MeadianFinder:
    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]

    def addNum(self, num):
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.max_heap)<len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        if len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0]+self.min_heap[0])/2

print("Median Finder")
medianFinder = MeadianFinder()
medianFinder.addNum(1)
print(medianFinder.findMedian())  # Output: 1.0
medianFinder.addNum(2)
print(medianFinder.findMedian())  # Output: 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian())  # Output: 2.0

## Merge K Sorted Arrays
import heapq

class Solution:
    def mergeKSortedArrays(self, arr, k):
        # min-heap of (value, array_index, element_index)
        min_heap = []
        
        # push the first element of each of the k arrays
        for i in range(k):
            heapq.heappush(min_heap, (arr[i][0], i, 0))
        
        result = []
        
        # pop the smallest, push the next element from the same array
        while min_heap:
            val, arr_idx, elem_idx = heapq.heappop(min_heap)
            result.append(val)
            
            if elem_idx + 1 < len(arr[arr_idx]):
                next_val = arr[arr_idx][elem_idx + 1]
                heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))
        
        return result
print("Merge K Sorted Arrays")
solution = Solution()
arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
merged_array = solution.mergeKSortedArrays(arrays, len(arrays))
print(merged_array)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


## Top K Frequent Elements
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        
        # bucket[i] = list of numbers that occur exactly i times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        # scan from highest possible frequency down to 1
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result

print("Top K Frequent Elements")
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(solution.topKFrequent(nums, k))  # Output: [1, 2]