import math
import random

# check a given input is number or not
# return: true if n is number, False otherwise


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def exercise_3():
    x = input("Input number of samples (interger number) which are generated: ")
    if is_number(x) == False:
        print("number of samples be an integer number")
        return

    loss_name = input("Write you loss name (RMSE| MAE| MSE): ")
    predict = []
    target = []

    # convert to integer to user for loop
    x = int(x)
    for i in range(x):
        pred = random.uniform(0, 10)
        targ = random.uniform(0, 10)
        loss_per_sample = (pred - targ)**2
        if loss_name == "MAE":
            loss_per_sample = abs(pred - target)

        print("loss name:", loss_name, ", sample:", i, ", pred:",
              pred, ", target:", targ, ", loss:", loss_per_sample)
        predict.append(pred)
        target.append(targ)

    loss_final = 0

    if loss_name == "RMSE":
        loss_final = RMSE_function(x, predict, target)
    if loss_name == "MAE":
        loss_final = MAE_function(x, predict, target)
    if loss_name == "MSE":
        loss_final = MSE_function(x, predict, target)
    print(f"Final {loss_name}:", loss_final)


def MAE_function(n, predict, target):
    result = 0
    for i in range(n):
        result += abs(predict[i] - target[i])
    return (result / n)


def MSE_function(n, predict, target):
    result = 0
    for i in range(n):
        result += (predict[i] - target[i])**2
    return (result / n)


def RMSE_function(n, predict, target):
    result_1 = 0
    for i in range(n):
        result_1 += (predict[i] - target[i])**2
    result = math.sqrt(result_1/n)
    return (result/n)


if __name__ == "__main__":
    exercise_3()
