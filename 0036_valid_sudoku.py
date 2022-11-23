def is_valid_sudoku(board):
    # check rows
    for row in board:
        if any(tile for tile in row if tile.isnumeric() and row.count(tile) > 1):
            return False

    # check columns
    for col_i in range(9):
        col = [row[col_i] for row in board]
        if any(tile for tile in col if tile.isnumeric() and col.count(tile) > 1):
            return False

    # check squares
    square_offsets = [[0, 0], [0, 3], [0, 6],
                      [3, 0], [3, 3], [3, 6],
                      [6, 0], [6, 3], [6, 6]]
    for x_off, y_off in square_offsets:
        square = []
        for i in range(x_off, x_off+3):
            for j in range(y_off, y_off+3):
                square.append(board[i][j])
        if any(tile for tile in square if tile.isnumeric() and square.count(tile) > 1):
            return False

    return True


def main():
    tests = [
        [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                                      "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
        [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                                      "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ]
    for test in tests:
        print(is_valid_sudoku(test))


if __name__ == '__main__':
    main()


"""
i forgot that i could invert a 2d array with zip(*board)
also the square checking was a bit messy
also i could have wrote a function for the testing of a group of 9
"""
