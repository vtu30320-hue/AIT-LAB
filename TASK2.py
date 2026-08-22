import random

def calculate_distance(route, distance_matrix):
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i+1]]
    return total

def hill_climbing(distance_matrix, start_point=0):
    n = len(distance_matrix)
    current_route = list(range(n))
    current_route.remove(start_point)
    current_route = [start_point] + current_route
    current_distance = calculate_distance(current_route, distance_matrix)

    improved = True
    while improved:
        improved = False
        for i in range(1, n-1):
            for j in range(i+1, n):
                new_route = current_route[:]
                new_route[i], new_route[j] = new_route[j], new_route[i]
                new_distance = calculate_distance(new_route, distance_matrix)
                if new_distance < current_distance:
                    current_route = new_route
                    current_distance = new_distance
                    improved = True
                    break
            if improved:
                break

    return current_route, current_distance


n = 9
distance_matrix = [
    [0, 2, 9, 10, 7, 3, 8, 6, 4],
    [2, 0, 8, 5, 6, 4, 7, 3, 9],
    [9, 8, 0, 6, 3, 7, 2, 5, 4],
    [10, 5, 6, 0, 4, 8, 3, 7, 2],
    [7, 6, 3, 4, 0, 5, 9, 8, 6],
    [3, 4, 7, 8, 5, 0, 6, 2, 9],
    [8, 7, 2, 3, 9, 6, 0, 4, 5],
    [6, 3, 5, 7, 8, 2, 4, 0, 6],
    [4, 9, 4, 2, 6, 9, 5, 6, 0]
]

optimal_route, optimal_distance = hill_climbing(distance_matrix, start_point=0)
print("Optimal Route:", optimal_route)
print("Total Distance:", optimal_distance)
