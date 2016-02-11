weak_point = [[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]

min_row_value = min_column_value = 100

for row in range(0, len(weak_point[0])):

    if sum(weak_point[row]) < min_row_value:
        min_row_index = row
        min_row_value = sum(weak_point[row])

    current_column_sum = 0

    for col in range(0, len(weak_point)):
        current_column_sum += weak_point[col][row]
   # print(current_column_sum, row, 'col')
    if current_column_sum < min_column_value and current_column_sum != 0:
        min_column_index = row
        min_column_value = current_column_sum

print(min_row_index, min_column_index)
