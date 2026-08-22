import heapq

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g_score[goal]

        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, float('inf')


# Example usage
graph = {
    'Restaurant': [('A', 2), ('B', 5)],
    'A': [('Restaurant', 2), ('C', 4), ('D', 6)],
    'B': [('Restaurant', 5), ('D', 2)],
    'C': [('A', 4), ('House', 7)],
    'D': [('A', 6), ('B', 2), ('House', 3)],
    'House': [('C', 7), ('D', 3)]
}

heuristic = {
    'Restaurant': 10,
    'A': 8,
    'B': 6,
    'C': 4,
    'D': 2,
    'House': 0
}

path, distance = a_star(graph, 'Restaurant', 'House', heuristic)
print("Optimal Route:", path)
print("Total Distance:", distance)
