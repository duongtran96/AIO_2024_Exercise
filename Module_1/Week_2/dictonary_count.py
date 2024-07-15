def get_lecter(get_string):
    # get leeter and count number
    letters = {}
    for char in get_string:
        # using if... in to check value exist or not
        if char in letters:
            letters[char] = letters[char] + 1
        else:
            letters[char] = 1

    # using item() to get all items
    # lambda function is passed in the key to perform sort by key
    letters = {key: val for key, val in sorted(
        letters.items(), key=lambda ele: ele[0])}
    # add "reserved = True" for reserved order
    return letters


get_string = 'Happiness'
result1 = get_lecter(get_string)
print(result1)
print("----")
get_string = 'smiles'
result2 = get_lecter(get_string)
print(result2)
