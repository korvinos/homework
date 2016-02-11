def count_neighbours(grid, row, col):

    if grid[row][col] == 1:
        count = -1
    else:
        count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):

            if grid[row + i][col + j] == 1:
                count += 1
    print(count)
    return count



count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"