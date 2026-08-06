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

## Job Sequencing Problem
def job_sequenc(id,deadline,profit):
    jobs = []
    for i in range(len(id)):
        jobs.append((id[i], deadline[i], profit[i]))
    
    # Sort jobs based on profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(deadline)
    result = [None] * max_deadline
    total_profit = 0
    
    for job in jobs:
        for j in range(min(max_deadline, job[1]) - 1, -1, -1):
            if result[j] is None:
                result[j] = job[0]
                total_profit += job[2]
                break
    
    return result, total_profit

## Fractional Knapsack Problem : Greedy Approach
def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    items = []
    
    for i in range(n):
        items.append((values[i] / weights[i], weights[i], values[i]))
    
    # Sort items based on value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)
    
    total_value = 0.0
    for ratio, weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            break
    
    return total_value

## Minimum Coins (DP - 20)
def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
print("Minimum coins required: ", min_coins([1, 2, 5], 11))