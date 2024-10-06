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

def initialize_params():
    w1, w2, w3, b = (0.016992259082509283, 0.0070783670518262355, -0.002307860847821344, 0)
    return w1, w2, w3, b

def predict(x1, x2, x3, w1, w2, w3, b):
    result = x1 * w1 + x2 * w2 + x3 * w3 + b
    return result

def compute_loss(y_hat, y, loss_type):
    if loss_type == "MSE":
        loss = np.pow(y_hat - y, 2)
    elif loss_type == "MAE":
        loss = np.abs(y_hat - y)
    return loss

def compute_gradient_wi(xi, y, y_hat):
    dl_dwi = 2 * xi * (y_hat - y)
    return dl_dwi

def compute_gradient_b(y, y_hat):
    dl_db = 2 * (y_hat - y)
    return dl_db

def update_weight_wi(wi, dl_dwi, lr):
    wi = wi - lr * dl_dwi
    return wi

def update_weight_b(b, dl_db, lr):
    b = b - lr * dl_db
    return b

def implement_linear_regression_nsamples(X_data, y_data, epoch_max = 50, lr = 1e-5, loss_type = "MSE"):
    losses = []

    w1, w2, w3, b = initialize_params()
    N = len(y_data)

    for epoch in range(epoch_max):

        loss_total = 0.0
        dw1_total = 0.0
        dw2_total = 0.0
        dw3_total = 0.0
        db_total = 0.0

        for i in range(N):
            # get a sample
            x1 = X_data[0][i]
            x2 = X_data[1][i]
            x3 = X_data[2][i]

            y = y_data[i]

            # compute ouput
            y_hat = predict(x1, x2, x3, w1, w2, w3, b)

            # compute loss
            loss = compute_loss(y, y_hat, loss_type = loss_type)
            loss_total = loss_total + loss

            # accumulate loss

            # compute gradient w1, w2, w3, b
            dl_dw1 = compute_gradient_wi(x1, y, y_hat)
            dl_dw2 = compute_gradient_wi(x2, y, y_hat)
            dl_dw3 = compute_gradient_wi(x3, y, y_hat)
            dl_db = compute_gradient_b(y, y_hat)

            # accumulate gradient w1, w2, w3, b
            dw1_total = dw1_total + dl_dw1
            dw2_total = dw2_total + dl_dw2
            dw3_total = dw3_total + dl_dw3
            db_total = db_total + dl_db

        # update parameters
        w1 = update_weight_wi(w1, dw1_total/N, lr)
        w2 = update_weight_wi(w2, dw2_total/N, lr)
        w3 = update_weight_wi(w3, dw3_total/N, lr)
        b = update_weight_b(b, db_total/N, lr)

        # logging
        losses.append(loss_total/N)

    return (w1, w2, w3, b, losses)

def plot_result(losses, num_sample = 100):
    plt.plot(losses[:num_sample])
    plt.xlabel('#epoch')
    plt.ylabel("Loss")
    plt.show()

if __name__ == "__main__":
    X, y = prepare_data(".\Module_4\Week_1\data\Advertising.csv")
    # for MSE loss function
    (w1, w2, w3, b, losses) = implement_linear_regression_nsamples(X, y, loss_type = "MSE", epoch_max = 1000, lr = 1e-5)
    # print(losses)
    print(f"w1, w2, w3 = {w1, w2, w3}")
    plot_result(losses, num_sample = 100)

    # for MAE loss function
    (w1, w2, w3, b, losses) = implement_linear_regression_nsamples(X, y, loss_type = "MAE", epoch_max = 1000, lr = 1e-5)
    plot_result(losses, num_sample = 100)