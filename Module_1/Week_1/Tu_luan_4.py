import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def exercise_4():
    x = input("Input number that want to calculate: ")
    n = input("Input number of iteration : ")
    n = int(n)
    x = float(x)

    name_approximate = input(
        "input function approximate (sin| cos| sinh| cosh):")

    if name_approximate == "sin":
        print("Approximate sin( x = ", x, "n =", n)
        print(approx_sin(x, n))

    if name_approximate == "cos":
        print("Approximate cos( x = ", x, "n =", n)
        print(approx_cos(x, n))

    if name_approximate == "sinh":
        print("Approximate sinh( x = ", x, "n =", n)
        print(approx_sinh(x, n))

    if name_approximate == "cosh":
        print("Approximate cosh( x = ", x, "n =", n)
        print(approx_cosh(x, n))

    if n <= 0:
        print("n must be positive interfer ")
    return -1


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


def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += (-1)**i * (x ** (2*i)) / factorial(2*i)
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / factorial(2 * i)
    return result


if __name__ == "__main__":
    exercise_4()
