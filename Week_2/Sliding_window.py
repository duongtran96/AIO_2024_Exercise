def sliding_window(num_list, k):
    """
    run 2 for loop.
    """
    result = []
    len_list = len(num_list)
    for i in range(0, len_list - k + 1):
        max_value = 0
        for j in range(i, i + k):
            if num_list[j] > max_value:
                max_value = num_list[j]
        result.append(max_value)
    return result


k = 4
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
result1 = sliding_window(num_list, k)
print(result1)
