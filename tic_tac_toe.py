some_game_state = [['x','o','o'], ['o','x','o'],['o','x','x']]
def eval_func(game_state: list):
    """
    eval function takes a game state to determine if it has won.
    game_state represents a 3x3 matrix 
    """
    if game_state[0][0] == game_state[0][1] == game_state[0][2] == 'x':
        return 10
    elif game_state[0][0] == game_state[0][1] == game_state[0][2] == 'o':
        return -10
    elif game_state[0][0] == game_state[1][1] == game_state[2][2] == 'o':
        return -10
    elif game_state[0][0] == game_state[1][1] == game_state[2][2] == 'x':
        return 10
    elif game_state[2][0] == game_state[1][1] == game_state[0][2] == 'x':
        return 10
    elif game_state[2][0] == game_state[1][1] == game_state[0][2] == 'o':
        return -10        
    elif game_state[1][0] == game_state[1][1] == game_state[1][2] == 'x':
        return 10
    elif game_state[1][0] == game_state[1][1] == game_state[1][2] == 'o':
        return -10
    elif game_state[2][0] == game_state[2][1] == game_state[2][2] == 'x':
        return 10
    elif game_state[2][0] == game_state[2][1] == game_state[2][2] == 'o':
        return -10
    elif game_state[0][0] == game_state[1][0] == game_state[2][0] == 'x':
        return 10
    elif game_state[0][0] == game_state[1][0] == game_state[2][0] == 'o':
        return -10
    elif game_state[0][1] == game_state[1][1] == game_state[2][1] == 'x':
        return 10
    elif game_state[0][1] == game_state[1][1] == game_state[2][1] == 'o':
        return -10
    elif game_state[0][2] == game_state[1][2] == game_state[2][2] == 'x':
        return 10
    elif game_state[0][2] == game_state[1][2] == game_state[2][2] == 'o':
        return -10

print(eval_func([['o','x','o'], ['x','x','o'],['o','x','o']]))
