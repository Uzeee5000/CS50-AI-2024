"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flattened_grid = [item for sublist in board for item in sublist]
    x = flattened_grid.count('X')
    o = flattened_grid.count('O')

    if terminal(board):
        return "Game Over"
    elif x==o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return "Game Over" 
    
    action=set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] ==EMPTY:
                action.add((i,j))
    
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise NameError("Invalid action")
    
    copied_board=copy.deepcopy(board)
    i,j=action
    copied_board[i][j]=player(board)
    return copied_board

    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Checking win column-wise
    for i in range(len(board[0])):
        all_x = True
        all_o = True
        for row in board:
            if row[i] != X:
                all_x = False
            if row[i] != O:
                all_o = False
        if all_x:
            return X
        if all_o:
            return O

    # Checking win row-wise
    for row in board:
        all_x = True
        all_o = True
        for cell in row:
            if cell != X:
                all_x = False
            if cell != O:
                all_o = False
        if all_x:
            return X
        if all_o:
            return O

    # Checking win diagonal-wise
    n = len(board)

    # Check main diagonal (from top-left to bottom-right)
    if board[0][0] != EMPTY:
        main_diagonal_winner = board[0][0]
        if all(board[i][i] == main_diagonal_winner for i in range(n)):
            return main_diagonal_winner

    # Check anti-diagonal (from top-right to bottom-left)
    if board[0][n-1] != EMPTY:
        anti_diagonal_winner = board[0][n-1]
        if all(board[i][n-1-i] == anti_diagonal_winner for i in range(n)):
            return anti_diagonal_winner

    # No winner found
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in board:
        for x in range(3):
            if i[x] not in [O,X]:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board)==X:
        moves=[]
        for action in actions(board):
            moves.append([min_value(result(board,action)),action])
        return sorted(moves,key=lambda x: x[0], reverse=True)[0][1]
    
    elif player(board)==O:
        moves=[]
        for action in actions(board):
            moves.append([max_value(result(board,action)),action])
        return sorted(moves,key=lambda x: x[0])[0][1]
         
def max_value(board):

    v= -math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):

    v= math.inf

    if terminal(board):
        return utility(board)
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
