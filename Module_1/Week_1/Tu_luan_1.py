import math


def cal_f1_score(tp, fp, fn):
    if (type(tp) != int) or (type(fp) != int) or (type(fn) != int):
        # if (isinstance(tp, int) == 0) or (isinstance(fp, int) == 0) or (isinstance(fn, int) == 0):
        if type(tp) != int:
            print("tp must be int")
        if type(fp) != int:
            print("fp must be int")
        if type(fn) != int:
            print("fn must be int")
        return

    # check tp, fp, fn is zero or not
    if (tp <= 0) or (fp <= 0) or (fn <= 0):
        print("tp and fp and fn must be greater then zero ")
        return
    else:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        F1_score = 2 * (precision * recall) / (precision + recall)
        print("precision is ", precision)
        print("recall is ", recall)
        print("F1_score is ", F1_score)
        return


if __name__ == "__main__":
    cal_f1_score(tp=4, fp=3, fn=1)
