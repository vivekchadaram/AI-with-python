"""
Tic Tac Toe Player
"""

import math
from os import access
from sys import path

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
    next=0
    if board==initial_state():
        return X
    else:
        for i in board:
            for j in i:
                if j is not EMPTY:
                    next+=1
    return X if next%2==0 else O
    raise NotImplementedError
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    li=[]
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==EMPTY:
                li.append([i,j])
    return li
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    playe=player(board)
    new_board=[[],[],[]]
    for i in range(0,3):
        for j in range(0,3):
            new_board[i].append(board[i][j])
    if playe==X:
        new_board[action[0]][action[1]]=X
    else:
        new_board[action[0]][action[1]]=O
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0]==board[0][1]==board[0][2]==X) or (board[1][0]==board[1][1]==board[1][2]==X) or (board[2][0]==board[2][1]==board[2][2]==X) or(board[0][0]==board[1][0]==board[2][0]==X) or (board[0][1]==board[1][1]==board[2][1]==X) or (board[0][2]==board[1][2]==board[2][2]==X) or (board[0][0]==board[1][1]==board[2][2]==X) or (board[0][2]==board[1][1]==board[2][0]==X):
        return X
    elif (board[0][0]==board[0][1]==board[0][2]==O) or (board[1][0]==board[1][1]==board[1][2]==O) or (board[2][0]==board[2][1]==board[2][2]==O) or (board[0][0]==board[1][0]==board[2][0]==O) or (board[0][1]==board[1][1]==board[2][1]==O) or (board[0][2]==board[1][2]==board[2][2]==O) or (board[0][0]==board[1][1]==board[2][2]==O) or (board[0][2]==board[1][1]==board[2][0]==O):
        return O
    else:
        return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if ((board[0][0]==board[0][1]==board[0][2]==X) or (board[0][0]==board[0][1]==board[0][2]==O) or (board[1][0]==board[1][1]==board[1][2]==X) or (board[1][0]==board[1][1]==board[1][2]==O) or (board[2][0]==board[2][1]==board[2][2]==X) or (board[2][0]==board[2][1]==board[2][2]==O) or (board[0][0]==board[1][0]==board[2][0]==X) or (board[0][0]==board[1][0]==board[2][0]==O) or (board[0][1]==board[1][1]==board[2][1]==X) or (board[0][1]==board[1][1]==board[2][1]==O) or (board[0][2]==board[1][2]==board[2][2]==X) or (board[0][2]==board[1][2]==board[2][2]==O) or (board[0][0]==board[1][1]==board[2][2]==X) or (board[0][0]==board[1][1]==board[2][2]==O) or (board[0][2]==board[1][1]==board[2][0]==X) or (board[0][2]==board[1][1]==board[2][0]==O)) or (board[0].count(EMPTY)==0 and board[1].count(EMPTY)==0 and board[2].count(EMPTY)==0):
        return True
    else:
        return False
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (board[0][0]==board[0][1]==board[0][2]==X) or (board[1][0]==board[1][1]==board[1][2]==X) or (board[2][0]==board[2][1]==board[2][2]==X) or(board[0][0]==board[1][0]==board[2][0]==X) or (board[0][1]==board[1][1]==board[2][1]==X) or (board[0][2]==board[1][2]==board[2][2]==X) or (board[0][0]==board[1][1]==board[2][2]==X) or (board[0][2]==board[1][1]==board[2][1]==X):
        return 1
    elif (board[0][0]==board[0][1]==board[0][2]==O) or (board[1][0]==board[1][1]==board[1][2]==O) or (board[2][0]==board[2][1]==board[2][2]==O) or (board[0][0]==board[1][0]==board[2][0]==O) or (board[0][1]==board[1][1]==board[2][1]==O) or (board[0][2]==board[1][2]==board[2][2]==O) or (board[0][0]==board[1][1]==board[2][2]==O) or (board[0][2]==board[1][1]==board[2][1]==O):
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    vmain=0
    alpha=float("inf")
    beta=-float("inf")
    actualaction=""
    if player(board)==X:
        v=-float("inf")
        for action in actions(board):
            vmain=max(vmain,minivalue(result(board,action),alpha,beta))
            alpha=max(alpha,vmain)
            if vmain>v:
                v=vmain
                actualaction=action
    else:
        v=float("inf")
        for action in actions(board):
            vmain=min(vmain,minivalue(result(board,action),alpha,beta))
            beta=min(beta,vmain)
            if vmain<v:
                v=vmain
                actualaction=action
    return actualaction
    raise NotImplementedError
def minivalue(board,alpha,beta):
    if terminal(board):
        return utility(board)
    else:
        v=float("inf")
        for action in actions(board):
            v=min(v,maxvalue(result(board,action),alpha,beta))
            beta=min(beta,v)
            if alpha>=beta:
                break
    return v
def maxvalue(board,alpha,beta):
    if terminal(board):
        return utility(board)
    else:
        v=-float("inf")
        for action in actions(board):
            v=max(v,minivalue(result(board,action),alpha,beta))
            alpha=max(alpha,v)
            if alpha>=beta:
                break
    return v