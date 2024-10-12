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


def batch_gradient_descent(X_b, y, n_epochs = 100, learning_rate = 0.01):
    # thetas = np.random.randn(4, 1)
    thetas = np . asarray ([[1.16270837], [-0.81960489], [1.39501033], [0.29763545]])

    thetas_path = [thetas]
    losses = []

    for i in range(n_epochs):
        # compute output
        output = X_b.dot(thetas)

        # compute loss
        loss = (output  - y)**2

        # compute loss's derivative
        loss_derivative = 2 * (output - y)

        # compute parameter's derivative
        gradients = X_b.T.dot(loss_derivative) / N

        # update parameters
        thetas = thetas - learning_rate * gradients 
        thetas_path.append(thetas)

        mean_loss = np.sum(loss) / N 
        losses.append(mean_loss)
    
    return thetas_path, losses 

def plot_result(range_data, losses):
    x_axis = list(range(range_data))
    plt.plot(x_axis, losses[:range_data], color = 'r')
    plt.show()

if __name__ == "__main__":

    data = np.genfromtxt('...\AIO_2024_Exercise\Module_4\Week_2\Data\Advertising.csv', delimiter = ',', skip_header = 1)
    N = data.shape[0]
    X = data[:,:3]
    y = data[:,3:]
    X_b, maxi, mini, avg = mean_normalization(X)

    bgd_thetas, losses = batch_gradient_descent(X_b, y, n_epochs =100, learning_rate = 0.01)
    print(round(sum(losses), 2))

    # plot result
    bgd_thetas, losses = batch_gradient_descent(X_b, y, n_epochs =100, learning_rate = 0.01)    
    plot_result(range_data = 100, losses = losses)
