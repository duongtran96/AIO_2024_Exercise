from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris_dataset = load_iris()
data = iris_dataset.data
data = iris_dataset.data[:, : 2]

plt.scatter(data[:, 0], data[:, 1], c = 'gray')
plt.title('Initial Dataset')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()