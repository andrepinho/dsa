from neetcode.testRunner import TestRunner
from typing import List
from collections import defaultdict


class Solution:
    # https://neetcode.io/problems/valid-sudoku

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


if __name__ == "__main__":
    test_cases = [
        {'inputs': {
            'board': [["1", "2", ".", ".", "3", ".", ".", ".", "."],
                      ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                      [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                      ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                      [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                      [".", ".", ".", ".", ".", ".", "2", ".", "."],
                      [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        }, 'expected': True},
        {'inputs': {
            'board': [["1", "2", ".", ".", "3", ".", ".", ".", "."],
                      ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                      [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                      ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                      [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                      [".", ".", ".", ".", ".", ".", "2", ".", "."],
                      [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        }, 'expected': False},
        {'inputs': {
            'board': [["1", "2", ".", ".", "3", ".", ".", ".", "."],
                      ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                      [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                      ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                      [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                      ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                      [".", ".", ".", ".", ".", ".", "2", ".", "."],
                      [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                      [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        }, 'expected': False},
    ]

    TestRunner.run_tests(Solution().isValidSudoku, test_cases)
