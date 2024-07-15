import math

# check a given input is number or not
# return: true if n is number, False otherwise


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# take input x and type of cativation function,
# then calculates and print the activation value


def number_actiavtion():
    x = input("input x = ")
    if is_number(x) == False:
        print("x must be a number")
        return

    x = float(x)
    act_name = input("activation function name (sigmoid| relu| elu): ")
    result = calculate_activation_func(x, act_name)

    if (act_name != 'sigmoid') and (act_name != 'relu') and (act_name != 'elu'):
        print(act_name, "is not supported")
    else:
        print(act_name, ' f{x} =', result)

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


if __name__ == "__main__":
    number_actiavtion()
