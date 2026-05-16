from os import *
from sys import *
from collections import *
from math import *


def nQueens(n):
    result = []

    def is_valid(board, row, col):
        # check queen for the upper column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # check queen for the left upper diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # check queen for the right upper diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1
        
        return True


    def solve(board, row):
        if row == n:
            temp = []
            for i in range(n):
                for j in range(n):
                    temp.append(board[i][j])
            result.append(temp)
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1
                solve(board, row+1)
                board[row][col] = 0
        
    board = [[0 for _ in range(n)] for _ in range(n)]

    solve(board, 0)

    return result
