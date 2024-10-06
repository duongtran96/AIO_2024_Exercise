import numpy as np
import matplotlib.pyplot as plt
import random
from prepare_data import prepare_data

# def initialize_params():
#     w1 = random.gauss(mu = 0.0, sigma = 0.01)
#     w2 = random.gauss(mu = 0.0, sigma = 0.01)
#     w3 = random.gauss(mu = 0.0, sigma = 0.01)
#     b = 0
#     return w1, w2, w3, b


# 2.1: Complete function inialize_params() 
def initialize_params():
    w1, w2, w3, b = (0.016992259082509283, 0.0070783670518262355, -0.002307860847821344, 0)
    return w1, w2, w3, b

# 2.2 Complete function predict(x1, x2, x3, w1, w2, w3, b)
def predict(x1, x2, x3, w1, w2, w3, b):
    result = x1 * w1 + x2 * w2 + x3 * w3 + b
    return result

# 2.3 Complete function compute_loss()
def compute_loss(y_hat, y, loss_type):
    if loss_type == "MSE":
        loss = np.pow(y_hat - y, 2)
    elif loss_type == "MAE":
        loss = np.abs(y_hat - y)
    return loss

# 2.4 Complete function compute_gradient_wi() and function compute_gradient_b():
def compute_gradient_wi(xi, y, y_hat):
    dl_dwi = 2 * xi * (y_hat - y)
    return dl_dwi

def compute_gradient_b(y, y_hat):
    dl_db = 2 * (y_hat - y)
    return dl_db

# 2.5 Compute function update_weight_wi() and function update_weight_b():
def update_weight_wi(wi, dl_dwi, lr):
    wi = wi - lr * dl_dwi
    return wi

def update_weight_b(b, dl_db, lr):
    b = b - lr * dl_db
    return b

# Compute function implement_linear_regression():
def implement_linear_regression(X_data, y_data, epoch_max = 50, lr = 1e-5, loss_type = "MSE"):
    losses = []

    w1, w2, w3, b = initialize_params()
    N  = len(y_data)
    for epoch in range(epoch_max):
        for i in range(N):

            # get a smaple
            x1 = X_data[0][i]
            x2 = X_data[1][i]
            x3 = X_data[2][i]

            y = y_data[i]

            # compute ouput
            y_hat = predict(x1, x2, x3, w1, w2, w3, b)

            # compute loss
            loss = compute_loss(y, y_hat, loss_type = loss_type)

            # compute gradient w1, w2, w3, b
            dl_dw1 = compute_gradient_wi(x1, y, y_hat)
            dl_dw2 = compute_gradient_wi(x2, y, y_hat)
            dl_dw3 = compute_gradient_wi(x3, y, y_hat)
            dl_db = compute_gradient_b(y, y_hat)

            # update parameters
            w1 = update_weight_wi(w1, dl_dw1, lr)
            w2 = update_weight_wi(w2, dl_dw2, lr)
            w3 = update_weight_wi(w3, dl_dw3, lr)
            b = update_weight_b(b, dl_db, lr)

            # logging
            losses.append(loss)

    return (w1, w2, w3, b, losses)

def plot_result(losses, num_sample):
    plt.plot(losses[:num_sample])
    plt.xlabel('#iteration')
    plt.ylabel("Loss")
    plt.show()

if __name__=="__main__":
    
    # Question 2: 
    y = predict(x1 = 1, x2 = 1, x3 = 0, w1 = 0, w2 = 0.5, w3 = 0, b = 0.5)
    print("Answer question 2 is ", y) # Answer question 2 is  1.0
    
    # Question 3:
    l = compute_loss(y_hat = 1, y = 0.5, loss_type = "MSE")
    print("Answer question 3 is ", l) # Answer question 3 is  0.25

    # Question 4:
    g_wi = compute_gradient_wi(xi = 1.0, y = 1.0, y_hat = 0.5)
    print("Answer question 4 is ", g_wi) # Answer question 4 is  -1.0

    # Question 5:
    g_b = compute_gradient_b(y = 2.0, y_hat = 0.5)
    print("Answer question 5 is ", g_wi) # Answer question 5 is  -1.0

    # Question 6:
    after_wi = update_weight_wi(wi = 1.0, dl_dwi = -0.5, lr = 1e-5)
    print("Answer question 6 is ", after_wi) # Answer question 6 is  1.000005

    # Question 7:
    after_b =  update_weight_b(b = 0.5, dl_db = -1.0, lr = 1e-5)
    print("Answer question 7 is ", after_b) # Answer question 7 is  0.50001

    # plot 100 sample 
    X, y = prepare_data(".\Module_4\Week_1\data\Advertising.csv")
    (w1, w2, w3, b, losses) = implement_linear_regression(X, y)
    plot_result(losses, num_sample = 100)
    
    # Question 8:
    (w1, w2, w3, b, losses) = implement_linear_regression(X, y)
    print("Answer question 8")
    print(w1, w2, w3) # 0.07405984066396477 0.15917360263437663 0.017561197559948935
    
    # Question 9:
    tv = 19.2
    radio = 35.9
    newspaper = 51.3
    sales = predict(tv, radio, newspaper, w1, w2, w3, b)
    print("Answer question 9")
    print(f"predicted sales is {sales}") # 8.176413319549823
    
    # Question 10: Calculate by MAE 
    l_MAE = compute_loss(y_hat = 1, y = 0.5, loss_type = "MAE")
    print("Answer question 10 is ", l_MAE) # 0.5
    
    