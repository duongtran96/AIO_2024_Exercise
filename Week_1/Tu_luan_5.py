import math


def md_nre_single_sample(y, y_hat, n, p):
    result = (y ** (1/n) - y_hat ** (1/n)) ** p
    return result


def exercise_5():
    y = float(input("input value y = "))
    y_hat = float(input("input value y_hat = "))
    n = int(input("Input value n = "))
    p = int(input("Input value p = "))
    print("md_nre_single_sample ( y = ", y, ", y_hat = ",
          y_hat, ", n = ", n, ", p = ", p, ")")
    print(md_nre_single_sample(y, y_hat, n, p))


if __name__ == "__main__":
    exercise_5()
