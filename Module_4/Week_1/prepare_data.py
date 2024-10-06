import numpy as np

def get_column(data, index):
    result = [row[index] for row in data]
    return result

def prepare_data(file_data_dataset):
    data = np.genfromtxt(file_data_dataset, delimiter = ',', skip_header = 1).tolist()

    N = len(data)

    # get tv(index = 0)
    tv_data = get_column(data, 0)

    # get radio(index = 1)
    radio_data = get_column(data, 1)

    # get newspaper(index = 0)
    newspaper_data = get_column(data, 2)

    # get sales(index = 3)
    sale_data = get_column(data, 3)

    # building X input y out for training
    X = [tv_data, radio_data, newspaper_data]
    y = sale_data

    return X, y

if __name__ == "__main__":

    get_data = ".\Module_4\Week_1\data\Advertising.csv"
    X, y = prepare_data(get_data)
    list = [sum(X[0][:5]), sum(X[1][:5]), sum(X[2][:5]), sum(y[:5])]
    print(list)

    # Answer [624.1, 175.1, 300.5, 78.9]
    