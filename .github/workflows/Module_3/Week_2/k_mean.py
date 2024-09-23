from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

iris_dataset = load_iris()
data = iris_dataset.data
data = iris_dataset.data[:, :2]

# Plot data
plt.scatter(data[:, 0], data[:, 1], c='gray')
plt.title("Initial Dataset")
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()

class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = None
        self.clusters = None
    
     def initialize_centroids(self, data):
        """
        Khởi tạo tâm cụm ngẫu nhiên
        Parameters:
            data (numpy.ndarray): Dữ liệu đầu vào cần phân cụm
        Return:
            None
        """

        np.random.seed(42)
        self.centroids = data[np.random.choice(data.shape[0], self.k, replace = False)]

    def euclidean_distance(self, x1, x2):
        """
        Tính khoảng cách Euclid giữa các điểm giữa liệu
        Parameters:
            x1 (numpy.ndarray): điểm dữ liệu 1
            x2 (numpy.ndarray): điểm dữ liệu 2
        Return:
            float Euclid
        """
        return np.sqrt(np.sum(np.power(x1 - x2, 2)))

    def assign_clusters(self, data):
        """"
        Phân cụm dữ liệu
        Parameters:
            data (numpy.ndarray): dữ liệu vào cần phân cụm
        Return:
            numpy.ndarray: mảng chứa cluster của từng điểm dữ liệu
        """

        # Tính toán khoảng cách giữa mổi điễm dữ liệu (data points) và tâm (centroids) bằng cách
        # sử dụng hàm euclidean_distance

        distances = np.array([[self.euclidean_distance(x, centroid) for centroid in self.centroids] for x in data])

        # print(np.argmin(distances, axis = 1)) # Có thể in ra
        return np.argmin(distances, axis = 1)

    def update_centroids(self, data):
        """
        Cập nhật tâm cụm
        Parameters:
            data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
        return:
            None
        """
        return np.array([data[self.cluster == i].mean(axis = 0) for i in range(self.k)])

    def fit(self, data):
        """"
        Hàm huấn luyên
        Parameters:
            data (numpy.ndarray): Dữ liệu đầu vào cần phân cụm
        Return:
            None
        """

        # gọ tới phương thức tạo ngẫu nhiên tâm cụm
        self.initialize_centroids(data)
        self.plot_cluster(data, 0)

        for i in range(self.max_iters):
            # Gán cụm cho các data point gần nhất
            self.cluster = self.assign_clusters(data)

            # Visualize các cụm và tâm cụm tại iteration
            self.plot_cluster(data, i)

            # Dựa vào các data point của từng cụm, dich chuyển tâm tới vị trí trung tâm (tính mean)
            new_centroids = self.update_centroids(data)

            # Nếu tâm cụm không di chuyển, dừng lại
            if np.all(self.centroids == new_centroids):
                break

            # Nếu tâm cụm di chuyển, thực hiện lại vòng lặp với các giá trị tâm cụm mới
            self.centroids = new_centroids
            self.plot_cluster(data, i)

        self.plot_final_cluster(data)

    def plot_cluster(self, data, iteration):
        """
        Vẽ các cụm và tâm cụm sau mỗi iteration
        Parameters:
            data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
            iteration (int): iteration hiện tại

        Return:
            None
        """
        plt.scatter(data[:, 0], data[:, 1], c = self.cluster, cmap = 'viridis', marker = 'o', alpha = 0.6)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s = 300, c = 'red', marker = 'x')
        plt.title(f"Iteration {iteration + 1}")
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.show()

    def plot_final_cluster(self, data):
        """"
        Vẽ các cụm và tâm cụm cuối cùng
        Parameters:
            data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
        return:
            None
        """
        plt.scatter(data[:, 0], data[:, 1], c = self.cluster, cmap = 'viridis', marker = 'o', alpha = 0.6)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s = 300, c = 'red', marker = 'x')
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.show()

if __name__ == "__main__":
    data = load_iris_data()

    kmeans = Kmeans()
    kmean.fit(data)