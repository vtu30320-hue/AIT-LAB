from collections import deque

def bfs_airline_routes(n, routes, start_airport):
    graph = [[] for _ in range(n)]
    for u, v in routes:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    traversal_order = []
    queue = deque([start_airport])
    visited[start_airport] = True

    while queue:
        airport = queue.popleft()
        traversal_order.append(airport)
        for neighbor in graph[airport]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    print("BFS Traversal Order:", traversal_order)
    if all(visited):
        print("✅ All airports can be visited from airport", start_airport)
    else:
        print("❌ Not all airports are reachable from airport", start_airport)


n = 6
routes = [(0,1),(0,2),(1,3),(2,4),(3,5)]
start_airport = 0
bfs_airline_routes(n, routes, start_airport)
