"""
neetcode - arrays & hashing - 7

sol 1:
check for dupes in rows, then columns, then squares

sol 2:
go tile by tile, checking if num in set for row, col, or square; then add it to each set
"""


# def is_valid_sudoku(board):
#     # check rows
#     for row in board:
#         if any(tile for tile in row if tile.isnumeric() and row.count(tile) > 1):
#             return False
#
#     # check columns
#     for col_i in range(9):
#         col = [row[col_i] for row in board]
#         if any(tile for tile in col if tile.isnumeric() and col.count(tile) > 1):
#             return False
#
#     # check squares
#     square_offsets = [
#         [0, 0],
#         [0, 3],
#         [0, 6],
#         [3, 0],
#         [3, 3],
#         [3, 6],
#         [6, 0],
#         [6, 3],
#         [6, 6],
#     ]
#     for x_off, y_off in square_offsets:
#         square = []
#         for i in range(x_off, x_off + 3):
#             for j in range(y_off, y_off + 3):
#                 square.append(board[i][j])
#         if any(tile for tile in square if tile.isnumeric() and square.count(tile) > 1):
#             return False
#
#     return True


from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set[str])
        rows = defaultdict(set[str])
        squares = defaultdict(set[str])  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                tile = board[r][c]
                if (
                    tile in rows[r]
                    or tile in cols[c]
                    or tile in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


def main():
    tests = [
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
    ]
    for test in tests:
        print(is_valid_sudoku(test))


if __name__ == "__main__":
    main()
