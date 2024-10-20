import numpy as np 
import matplotlib.pyplot as plt 
import random

random.seed(0)
# matplotlib inline

def load_data_from_file(fileName = "D:\AIO2024\Home_work\AIO_2024_Exercise\Module_4\Week_3\Data\Advertising.csv"):
    data = np.genfromtxt(fileName, dtype = None, delimiter = ',', skip_header = 1)
    features_X = data[:, : 3]
    sales_Y = data[:, 3]
    features_X = np.hstack((np.ones((features_X.shape[0], 1)), features_X))
    
    return features_X, sales_Y

if __name__ == "__main__":
    features_x, sale_y = load_data_from_file()
    # question 2
    print(features_x[:5, :])
    # question 3
    print(sale_y.shape)    