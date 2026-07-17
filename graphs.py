##graphs

## building an adjency matrix
## time complexity O(nlogn), space complexity is o(n^2)
def build_adjacency_matrix(n, edges):
    adj = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v in edges:
        adj[u][v] = 1
        adj[v][u] = 1
    return adj

n, m = 5, 6
edges = [(1,2), (1,3), (2,4), (3,4), (3,5), (4,5)]
adj = build_adjacency_matrix(n, edges)
print("our adjency matrix is this:",build_adjacency_matrix(n, edges) )

## building an adjency list
## time complexity O(nlogn), space complexity is o(2E)
def build_adjacency_list(n, edges):
    adj = [[] for _ in range(n + 1)]   # note: MUST use list comprehension here too!
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

n = 5
edges = [(1,3), (1,2), (3,5), (3,4), (2,4), (4,5)]
adj = build_adjacency_list(n, edges)
print(adj)
print("our adjency matrix is this:",build_adjacency_list(n, edges) )