# Cau trac nghiem 1

import math


def cal_f1_score(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    F1_score = 2 * precision * recall / (precision + recall)
    return F1_score


assert round(cal_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
print(round(cal_f1_score(tp=2, fp=4, fn=5), 2))

# Cau trac nghiem 2


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))
print(is_number('n'))

# Cau trac nghiem 4


def sigmoid_calculate(n):
    result = 1 / (1 + math.exp(-n))
    return result


assert round(sigmoid_calculate(3), 2) == 0.95
print(round(sigmoid_calculate(2), 2))

# Cau trac nghiem 5


def elu_calculate(n):
    alpha = 0.01
    if n <= 0:
        result = alpha * (math.exp(n) - 1)
    else:
        result = n
    return result


assert round(elu_calculate(1)) == 1
print(round(elu_calculate(-1), 2))

# Cau trac nghiem 6

# check a given input is number or not
# return: true if n is number, False otherwise


# take input x and type of cativation function,
# then calculates and print the activation value

# function calculate Sigmoid activation function
def sigmoid_calculate(n):
    result = 1 / (1 + math.exp(-n))
    return result

# function calculate Relu activation function


def relu_calculate(n):
    if n <= 0:
        result = 0
    else:
        result = n
    return result

# function calculate Elu activation function


def elu_calculate(n):
    alpha = 0.01
    if n <= 0:
        result = alpha * (math.exp(n) - 1)
    else:
        result = n
    return result

# check type of activation function sigmoid, relu or elu


def calculate_activation_func(n, act_name):
    result = None
    if act_name == 'sigmoid':
        result = sigmoid_calculate(n)
    elif act_name == 'relu':
        result = relu_calculate(n)
    elif act_name == 'elu':
        result = elu_calculate(n)
    return result


assert calculate_activation_func(n=1, act_name='relu') == 1
print(round(calculate_activation_func(n=3, act_name='sigmoid'), 2))

# Cau trac nghiem 7


def calc_ae(y, y_hat):
    result = abs(y - y_hat)
    return result


y = 1
y_hat = 6
assert calc_ae(y, y_hat) == 5
y = 2
y_hat = 9
print(calc_ae(y, y_hat))

# Cau trac nghiem 8


def calc_se(y, y_hat):
    result = (y - y_hat) ** 2
    return result


y = 4
y_hat = 2
assert calc_se(y, y_hat) == 4
print(calc_se(2, 1))

# Cau trac nghiem 9


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += (-1)**i * (x ** (2*i)) / factorial(2*i)
    return result


assert round(approx_cos(x=1, n=10), 2) == 0.54
print(round(approx_cos(x=3.14, n=10), 2))

# Cau trac nghiem 10


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def approx_sin(x, n):
    result = 0
    for i in range(n):
        result += (-1)**i * (x ** (2*i + 1)) / factorial(2*i + 1)
    return result


assert round(approx_sin(x=1, n=10), 4) == 0.8415
print(round(approx_sin(x=3.14, n=10), 4))

# cau trac nghiem 11


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result


assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))
