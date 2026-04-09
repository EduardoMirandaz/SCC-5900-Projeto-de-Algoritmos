def fill_the_board(row, grid, cols, diag1, diag2):
    if row == 8:
        return 1  # found a valid state

    count = 0

    for col in range(8):
        if grid[row][col] == '*':
            continue

        # check if column or diagonals are occupied
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue

        # place queen
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

        count += fill_the_board(row + 1, grid, cols, diag1, diag2)

        # backtrack
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)

    return count


# input
grid = [list(input().strip()) for _ in range(8)]

# start recursion
print(fill_the_board(0, grid, set(), set(), set()))