import numpy as np
import matplotlib.pyplot as plt
import random

def get_column(data, index):
    result = [row[index] for row in data]
    return result

def prepare_data(file_data_dataset):
    data = np.genfromtxt(file_data_dataset, delimiter = ',', skip_header = 1).tolist()

    # get tv(index = 0)
    tv_data = get_column(data, 0)

    # get radio(index = 1)
    radio_data = get_column(data, 1)

    # get newspaper(index = 0)
    newspaper_data = get_column(data, 2)

    # get sales(index = 3)
    sales_data = get_column(data, 3)

    # building X input and y output for training
    # Create list of features for input
    X = [[1, x1, x2, x3] for x1, x2, x3 in zip(tv_data, radio_data, newspaper_data)]
    y = sales_data

    return X, y

def initialize_params():
    bias = 0
    w1 = random.gauss(mu = 0.0, sigma = 0.01)
    w2 = random.gauss(mu = 0.0, sigma = 0.01)
    w3 = random.gauss(mu = 0.0, sigma = 0.01)
    
    # comment this line for real applications
    return [0, -0.01268850433497871, 0.004752496982185252, 0.0073796171538643845]
    # return [bias, w1, w2, w3]

# Predict output by using y = x0 * b + x1 * w1 + x2 * w2 + x3 * w3
def predict(X_features, weights):
    result = np.dot(X_features, weights)
    return result

def compute_loss(y_hat, y):
    return (y_hat - y)**2

# compute gradient:
def compute_gradient_w(X_features, y, y_hat):
    X_features = np.array(X_features)
    dl_dweights = 2 * X_features * (y_hat - y)
    return dl_dweights

def update_weight(weights, dl_dweights, lr):
    weights = weights - dl_dweights * lr
    return weights


def implement_linear_regression(X_feature, y_output, epoch_max = 50, lr =1e-5):

    losses = []
    weights = initialize_params()
    N = len(y_output)
    
    for epoch in range(epoch_max):
        # print("epoch", epoch)
        for i in range(N):
            # get a sample - row i
            features_i = X_feature[i]
            y = y_output[i]

            # compute output
            y_hat = predict(features_i, weights)

            # compute loss
            loss = compute_loss(y, y_hat)

            # compute gradient w1, w2, w3, b
            dl_dweights = compute_gradient_w(features_i, y, y_hat)

            # update parameters
            weights = update_weight(weights, dl_dweights, lr)

            # logging
            losses.append(loss)
    
    return weights, losses

def plot_result(losses, num_sample = 100):
    plt.plot(L[0: num_sample])
    plt.xlabel("#Iteration")
    plt.ylabel("Loss")
    plt.show()

if __name__== "__main__":

    # Question 12
    X, y = prepare_data(".\Module_4\Week_1\data\Advertising.csv")
    W, L = implement_linear_regression(X, y, epoch_max= 50, lr = 1e-5)
    print("Answer question 12 is", L[9999]) # 31.33922340810991

    plot_result(L, 100)
