import random
import math

class AntColony:
    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=2):
        self.distances = distances
        self.pheromone = [[1 / (len(distances)) for _ in range(len(distances))] for _ in range(len(distances))]
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self, start=0):
        shortest_path = None
        all_time_shortest_path = ("route", math.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths(start)
            self.spread_pheromone(all_paths, self.n_best, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
            self.pheromone = [[p * self.decay for p in row] for row in self.pheromone]
        return all_time_shortest_path

    def gen_path_dist(self, path):
        total = 0
        for i in range(len(path) - 1):
            total += self.distances[path[i]][path[i+1]]
        total += self.distances[path[-1]][path[0]]  # return to restaurant
        return total

    def gen_all_paths(self, start):
        all_paths = []
        for _ in range(self.n_ants):
            path = self.gen_path(start)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = [start]
        visited = set(path)
        while len(path) < len(self.distances):
            move = self.pick_move(self.pheromone[path[-1]], self.distances[path[-1]], visited)
            path.append(move)
            visited.add(move)
        return path

    def pick_move(self, pheromone, dist, visited):
        pheromone = [p ** self.alpha for p in pheromone]
        heuristic = [((1 / d) if d > 0 else 0) ** self.beta for d in dist]
        probs = [p * h if idx not in visited else 0 for idx, (p, h) in enumerate(zip(pheromone, heuristic))]
        total = sum(probs)
        if total == 0:
            return random.choice([i for i in range(len(dist)) if i not in visited])
        probs = [p / total for p in probs]
        return self.random_choice(probs)

    def random_choice(self, probs):
        r = random.random()
        cumulative = 0
        for idx, prob in enumerate(probs):
            cumulative += prob
            if r <= cumulative:
                return idx
        return len(probs) - 1

    def spread_pheromone(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in range(len(path) - 1):
                self.pheromone[path[move]][path[move+1]] += 1.0 / dist
            self.pheromone[path[-1]][path[0]] += 1.0 / dist


# Example usage
distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

aco = AntColony(distances, n_ants=10, n_best=5, n_iterations=100, decay=0.95, alpha=1, beta=2)
shortest_path = aco.run(start=0)
print("Optimal Route:", shortest_path[0])
print("Total Distance:", shortest_path[1])
