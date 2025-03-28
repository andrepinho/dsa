from typing import List
from collections import defaultdict


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sideLength = len(board)
        boardSize = sideLength ** 2
        validBoard = True

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(boardSize):
            rowIndex = i // sideLength
            colIndex = i % sideLength
            squareIndex = (rowIndex//3, colIndex//3)

            value = board[rowIndex][colIndex]

            if value == '.':
                continue

            seenInrow = value in rows[rowIndex]
            seenInColumn = value in cols[colIndex]
            seenInSquare = value in squares[(squareIndex)]

            if seenInrow or seenInColumn or seenInSquare:
                validBoard = False

                break

            rows[rowIndex].add(value)
            cols[colIndex].add(value)
            squares[squareIndex].add(value)

        return validBoard
