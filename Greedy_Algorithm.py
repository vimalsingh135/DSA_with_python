## N meetings in one room
def n_meetings(start,end,n):
    meetings = []
    for i in range(n):
        meetings.append((start[i], end[i], i+1))
    
    # Sort meetings based on their end time
    meetings.sort(key=lambda x: x[1])
    
    result = []
    last_end_time = 0
    
    for meeting in meetings:
        if meeting[0] > last_end_time:
            result.append(meeting[2])  # Append meeting number
            last_end_time = meeting[1]
    
    return result
print ("the maximum meetings that can be held are: ", n_meetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9], 6))

## Minimum number of platforms required for a railway
def min_platforms(arr, dep, n):
    arr.sort()
    dep.sort()
    
    platforms = 1
    max_platforms = 1
    i = 1
    j = 0
    
    while i < n and j < n:
        if arr[i] < dep[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    
    return max_platforms