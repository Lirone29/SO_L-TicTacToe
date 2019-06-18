
import numpy as matrix
import random as ran
import unittest

from Tools.scripts.treesync import raw_input

player = "O"
opponent = "X"
e = "_"

def print_board(board):
    ticTacToeBoard = matrix.array(board)
    for i in range(len(ticTacToeBoard)):
        for j in range(len(ticTacToeBoard)):
            value = ticTacToeBoard[i][j]
            print("{}".format(value).rjust(4), end='')
        print("")

def does_player_win(whichPlayer, board):
    ticTacToeBoard = matrix.array(board)
    counter = 0

    #vertically
    for i in range(0,ticTacToeBoard.shape[0]):
        for j in range(0, ticTacToeBoard.shape[0]):
            if(ticTacToeBoard[i][j] == whichPlayer):
                counter += 1
        if(counter ==3):
            return True
        else:
            counter = 0

    counter = 0
    # horizontally
    for i in range(0, ticTacToeBoard.shape[0]):
        for j in range(0, ticTacToeBoard.shape[0]):
            if (ticTacToeBoard[j][i] == whichPlayer):
                    counter += 1
        if (counter == 3):
            return True
        else:
            counter = 0

    counter = 0
    #diagonally
    for i in range(0, ticTacToeBoard.shape[0]):
        for j in range(0, ticTacToeBoard.shape[0]):
            if(i == j):
                if(ticTacToeBoard[j][i] == whichPlayer):
                    counter += 1
    if (counter == 3):
        return True
    else:
        counter = 0

    #print(ticTacToeBoard.shape[0])
    i = ticTacToeBoard.shape[0] -1
    j = 0
    # diagonally
    while(i >= 0 and j < (ticTacToeBoard.shape[0])):
        if (ticTacToeBoard[j][i] == whichPlayer):
            counter +=1
        i -=1
        j +=1

    if (counter == 3):
        return True

    return False


def ai_move_next_player(board):
    ticTacToeBoard = matrix.array(board)
    saveX = -1
    saveY = -1
    for i in range(0, ticTacToeBoard.shape[0]):
        for j in range(0, ticTacToeBoard.shape[0]):
                if(ticTacToeBoard[i][j] == player):
                    saveX = i
                    saveY = j
                    if(saveX +1 >0 and saveX+1 <  ticTacToeBoard.shape[0]):
                        ticTacToeBoard[saveX][saveY] = opponent
                    else:
                        if (saveX - 1 > 0 and saveX - 1 < ticTacToeBoard.shape[0]):
                            ticTacToeBoard[saveX][saveY] = opponent




#czy pononwie zwracac jak zajete??

    return ticTacToeBoard


def ai_move(board):
    ticTacToeBoard = matrix.array(board)
    move_X = ran.randint(0,ticTacToeBoard.shape[0])
    move_Y = ran.randint(0,ticTacToeBoard.shape[0])

    for i in range(0, ticTacToeBoard.shape[0]):
        for j in range(0, ticTacToeBoard.shape[0]):
            if( i == move_X and j == move_Y):
                if(ticTacToeBoard[i][j] == e):
                    ticTacToeBoard[i][j] = opponent
    #czy pononwie zwracac jak zajete??

    return ticTacToeBoard


def get_user_move(board):
    ticTacToeBoard = matrix.array(board)
    #print()
    player_X = raw_input("Give value for X move %d to %d" % (0, ticTacToeBoard.shape[0]-1))
    player_Y = raw_input("Give value for Y move %d to %d" % (0, ticTacToeBoard.shape[0]-1))
    player_move_X = int(player_X)
    player_move_Y = int(player_Y)
    oneMoreTime = True
    for i in range(0, ticTacToeBoard.shape[0]):
        for j in range(0, ticTacToeBoard.shape[0]):
            if (i==player_move_X):
                if (j == player_move_Y):
                    #print("IN")
                    if (ticTacToeBoard[i][j] == "_"):
                        ticTacToeBoard[i][j] = "O"
                        oneMoreTime = False
    if(oneMoreTime == True):
        print("Not empty space!!! One more time:")
        get_user_move(ticTacToeBoard)

    return ticTacToeBoard

def tie(board):
    playerWin = does_player_win(player, board)
    opponentWin = does_player_win(opponent, board)

    if(playerWin == True):
        if(opponentWin == True):
            return True
    return False

if __name__ == '__main__':
    board =[[e,e,e],
            [e,e,e],
            [e,e,e]]

    #print(board)
    #print_board(board)
    randStart = ran.randint(0,1)

    result = False
    resultTie = False

    ticTacToeBoard = matrix.array(board)
    while(result!=True):
        if(randStart == 0):
            print_board(ticTacToeBoard)
            ticTacToeBoard = get_user_move(ticTacToeBoard)
            result = does_player_win(player, ticTacToeBoard)
            resultTie = tie(ticTacToeBoard)

            if(result == True):
                break
            ticTacToeBoard = ai_move(ticTacToeBoard)
            result = does_player_win(opponent, ticTacToeBoard)
            resultTie = tie(ticTacToeBoard)
            if (result == True):
                break
        else:
            print_board(ticTacToeBoard)
            ticTacToeBoard = ai_move(ticTacToeBoard)
            result = does_player_win(opponent, ticTacToeBoard)
            resultTie = tie(ticTacToeBoard)
            if (result == True):
                break
            ticTacToeBoard = get_user_move(ticTacToeBoard)
            result = does_player_win(player, ticTacToeBoard)
            resultTie = tie(ticTacToeBoard)

            if (result == True):
                break



