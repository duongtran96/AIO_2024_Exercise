import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def mean_normalization(X):
    N = len(X)
    maxi = np.max(X)
    mini = np.min(X)
    avg = np.mean(X)
    X = (X - avg)/ (maxi - mini)
    X_b = np.c_[np.ones((N, 1)), X]

    return X_b, maxi, mini, avg

def stochastic_gradient_descent(X_b, y, n_epochs = 50, learning_rate = 0.00001):

    # thetas = np.random.randn(4, 1)
    thetas = np.asarray ([[1.16270837], [-0.81960489], [1.39501033], [0.29763545]])

    thetas_path = [thetas]
    losses = []

    for epoch in range(n_epochs):
        for i in range(N):
            # select random number in N
            # random_index = np.random.randn(N) # In real application, you shoule use this code

            random_index = i # this code for this assignment only

            xi = X_b[random_index: random_index + 1]
            yi = y[random_index: random_index + 1]

            # compute output
            output = xi.dot(thetas)

            # compute loss li
            loss = (yi - output)**2/ 2

            # compute gradient for loss
            g_l_i =  (output - yi)
            gradient =  xi.T.dot(g_l_i)

            # update theta
            thetas = thetas - learning_rate * gradient

            # logging
            thetas_path.append(thetas)
            losses.append(loss[0][0])

    return thetas_path, losses

def plot_result(range_data, losses):
    x_axis = list(range(range_data))
    plt.plot(x_axis, losses[:range_data], color = 'r')
    plt.show()

if __name__== "__main__":

    data = np.genfromtxt('...\AIO_2024_Exercise\Module_4\Week_2\Data\Advertising.csv', delimiter = ',', skip_header = 1)
    N = data.shape[0]
    X = data[:,:3]
    y = data[:,3:]
    X_b, maxi, mini, avg = mean_normalization(X)
    sgd_theta , losses = stochastic_gradient_descent (X_b, y, n_epochs = 1, learning_rate =0.01 )
    print(np.sum(losses))

    # plot result
    sgd_theta , losses = stochastic_gradient_descent (X_b, y, n_epochs = 50, learning_rate =0.01 )
    plot_result(range_data = 500, losses = losses)