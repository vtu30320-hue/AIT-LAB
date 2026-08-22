import math

def minimax(node, depth, alpha, beta, maximizingPlayer, game_tree):
    if depth == 0 or node not in game_tree:
        return node  # terminal node value

    if maximizingPlayer:
        maxEval = -math.inf
        bestMove = None
        for child in game_tree[node]:
            eval = minimax(child, depth-1, alpha, beta, False, game_tree)
            if eval > maxEval:
                maxEval = eval
                bestMove = child
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval if depth > 1 else bestMove
    else:
        minEval = math.inf
        bestMove = None
        for child in game_tree[node]:
            eval = minimax(child, depth-1, alpha, beta, True, game_tree)
            if eval < minEval:
                minEval = eval
                bestMove = child
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval if depth > 1 else bestMove


# Example game tree (attack vs defense strategies)
game_tree = {
    'Attack': ['Aggressive', 'Balanced'],
    'Aggressive': [3, 5],   # payoff values
    'Balanced': [2, 9],
}

best_strategy = minimax('Attack', 2, -math.inf, math.inf, True, game_tree)
print("Optimal Attack Strategy:", best_strategy)
