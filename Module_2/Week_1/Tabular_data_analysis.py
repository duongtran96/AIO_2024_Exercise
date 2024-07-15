# DOWNLOAD DATA
#!gdown 1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq
import pandas as pd
import numpy as np
df = pd.read_csv('/content/advertising.csv')
data = df.to_numpy()

sale_column = data[:, 3]
max_sale_column = sale_column.max()
index = np.where(data == max_sale_column)[0][0]
print(max_sale_column, index)
# 15. Answer C

# 16. Giá trị trung bình của cột TV là:
TV_column = data[:, 0]
average_TV_column = np.mean(TV_column)
print(average_TV_column)
# 16:  Answer B

# 17. Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20 là:
data = data[data[:, 3] >= 20]
print(data.shape)
# 17: answer A

# 18. Tính giá trị trung bình của cột Radio thoả mãn điều kiện giá trị tương ứng trên cột Sales lớn hơn hoặc bằng 15:
data = data[data[:, 3] >= 15]
average = np.mean(data[:, 1])
print(average)
# 18. Answer B

# 19. Tính tổng các hàng của cột Sales với điều kiện giá trị Newspaper lớn hơn giá trị trung bình của cột Newspaper:


def sum_sales_by_ave_new(data):
    a = np.mean(data[:, 2])
    data = data[data[:, 2] > a]
    sum_sales_by_ave_new = data[:, 3].sum()
    return sum_sales_by_ave_new


sum_sales = sum_sales_by_ave_new(data)
print(sum_sales)
# 19: Answer C

"""
Câu hỏi 20: Gọi giá trị trung bình của cột Sales là A. Tạo ra mảng mới scores chứa các
giá trị Good, Average và Bad sao cho: nếu giá trị hiện tại > A => giá trị trong mảng mới
là Good, < A thì sẽ là Bad và = A sẽ là Average. Sau đó in ra kết quả scores[7:10]
"""


def mean_sale(data):
    mean = np.mean(data[:, 3])
    condition_1 = data[:, 3] < mean
    scores = np.where(condition_1, "Bad", "Good")
    return scores


print(mean_sale(data)[7:10])
# 20: anwer C

"""
Câu hỏi 21: Gọi giá trị trên cột Sales gần nhất với giá trị trung bình cũng chính cột
Sales là A. Tạo ra mảng mới scores chứa các giá trị Good, Average và Bad sao cho: nếu
giá trị hiện tại > A => giá trị trong mảng mới là Good, < A thì sẽ là Bad và = A sẽ là
Average. Sau đó in ra kết quả scores[7:10]
"""


def nearest_value(data):
    mean = np.mean(data[:, 3])
    idx = (np.abs(data[:, 3] - mean)).argmin()
    return data[idx, 3]


def score(data):
    nearest_value = nearest_value(data)
    scores = np.where(data[:, 3] < nearest_value, 'Bad', "Good")
    return scores


a = score(data)
print(a[7:10])
# 21: answer C
