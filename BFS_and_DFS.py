## breadth-first search 
from collections import deque

def bfs(n, adj, start):
    visited = [False] * (n + 1)
    result = []
    
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True   # mark visited when ADDING to queue, not when popping!
                queue.append(neighbor)
    
    return result


# ---- Input handling ----
n, m = map(int, input().split())   # e.g. 5 6
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

start = int(input())               # starting node
print(bfs(n, adj, start))


##depth- first search
def dfs(node, adj, visited, result):
    visited[node] = True
    result.append(node)
    
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited, result)
    
    return result


# ---- Input handling ----
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

start = int(input())
visited = [False] * (n + 1)
print(dfs(start, adj, visited, [])) 