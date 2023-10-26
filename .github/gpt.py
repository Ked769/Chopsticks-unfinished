#Make a dataset with the steps to solve the game "chopsticks" from all 625 possible configurations

import sys

# Define the initial game state
game_state = [[1, 1], [1, 1]]

# Define the heuristic function to evaluate game states
def evaluate(game_state):
    # Return the difference in the number of active hands between the players
    return game_state[0].count(0) - game_state[1].count(0)

# Define the minimax algorithm
def minimax(game_state, depth, maximizing_player):
    # Check if the game is over or the search depth has been reached
    if depth == 0 or all(hand == [0, 0] for hand in game_state):
        return evaluate(game_state)

    # Generate possible moves for the active player
    possible_moves = []
    for i in range(2):
        for j in range(2):
            if game_state[i][j] > 0:
                for k in range(2):
                    if i != k:
                        new_state = [hand[:] for hand in game_state]
                        new_state[k][(j + game_state[i][j]) % 2] += game_state[i][j]
                        if new_state[k][(j + game_state[i][j]) % 2] >= 5:
                            new_state[k][(j + game_state[i][j]) % 2] = 0
                        possible_moves.append(new_state)

    # Apply the minimax algorithm recursively
    if maximizing_player:
        max_eval = -sys.maxsize
        for move in possible_moves:
            eval = minimax(move, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = sys.maxsize
        for move in possible_moves:
            eval = minimax(move, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def opt_Move(game_state):
    # Determine the optimal move for the active player
    optimal_move = None
    max_eval = -sys.maxsize
    for i in range(2):
        for j in range(2):
            if game_state[i][j] > 0:
                for k in range(2):
                    if i != k:
                        new_state = [hand[:] for hand in game_state]
                        new_state[k][(j + game_state[i][j]) % 2] += game_state[i][j]
                        if new_state[k][(j + game_state[i][j]) % 2] >= 5:
                            new_state[k][(j + game_state[i][j]) % 2] = 0
                        eval = minimax(new_state, 4, False)
                        if eval > max_eval:
                            optimal_move = [[i, j], [k, (j + game_state[i][j]) % 2]]
                            max_eval = eval

    # Apply the optimal move and print the new game state
    game_state[optimal_move[1][0]][optimal_move[1][1]] += game_state[optimal_move[0][0]][optimal_move[0][1]]
    if game_state[optimal_move[1][0]][optimal_move[1][1]] >= 5:
        game_state[optimal_move[1][0]][optimal_move[1][1]] = 0
    print("Optimal move:", optimal_move)
    print("New game state:", game_state)
    return optimal_move, game_state

while game_state[0] != [5,5] and game_state[1] != [5,5]:
    op, game_state = opt_Move(game_state)
    game_state = [k.split(" ") for k in [i for i in input("Enter new gamestate as 'Plh Prh|Olh Orh' : ").split("|")]]
    for j in game_state:
        for i in j:  
            game_state[game_state.index(j)][game_state[game_state.index(j)].index(i)] = int(i)