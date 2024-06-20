def count_word_txt(file):
    # print(type(file.read()))                    # type of "file.read()" in string, type of "file.read().split()" = list
    data = file.read().lower().split()                  # split data to list
    # print(type(data))
    word_count = {}                             # empty dictonrary to store work cound
    for word in data:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    # print('word_count') why use print exist value None?????
    return word_count


  # open file to read
with open('D:\AIO2024\Home_Work\Week_2\P1_data.txt', 'r') as file:
    text_txt = count_word_txt(file)
    print(text_txt)
