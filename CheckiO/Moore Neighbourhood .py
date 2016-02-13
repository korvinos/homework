def count_neighbours(grid, row, col):
    top, bottom, left, right = -1, 2, -1, 2
    if grid[row][col] == 1:
        count = -1
    else:
        count = 0

    if row == len(grid) - 1:
        bottom = 1
    if row == 0:
        top = 0
    if col == 0:
        left = 0
    if col == len(grid[0]) - 1:
        right = 1

    for i in range(left, right):
        for j in range(top, bottom):
            if grid[row + i][col + j] == 1:
                count += 1
    print(count)
    return count



count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"