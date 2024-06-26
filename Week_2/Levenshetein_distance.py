def my_function(source, target):
    rows = len(source) + 1
    columns = len(target) + 1

    Matrix = [[0] * columns for _ in range(rows)]
    for cols in range(columns):
        Matrix[0][cols] = cols

    for row in range(rows):
        Matrix[row][0] = row

    for row in range(1, rows):
        for col in range(1, columns):
            if source[row - 1] == target[col - 1]:
                sub_cost = 0
            else:
                sub_cost = 1
            Matrix[row][col] = min(
                Matrix[row-1][col] + 1, Matrix[row][col - 1] + 1, Matrix[row-1][col - 1] + sub_cost)
    return Matrix[rows-1][columns - 1]


result = my_function("abcd", "aa")
print(result)
