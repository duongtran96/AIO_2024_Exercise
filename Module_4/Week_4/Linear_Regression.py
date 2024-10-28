import numpy as np

class CustiomLinearRegression:
    def __init__(self, X_data, y_target, learning_rate = 0.01, num_epochs = 10000):
        self.num_sample = X_data.shape[0]
        self.X_data = np.c_[((self.num_sample, 1)), X_data]
        self.y_target = y_target
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs

        self.theta = np.random.randn(self.X_data.shape[1], 1)
        self.losses = []

    def compute_loss(self, y_pred, y_target):
        loss = (y_pred - self.y_target)**2
        return loss
    
    def predict(self, theta, X_data):
        y_pred = X_data.dot(self.theta)
        return y_pred

    def fit(self):
        for epoch in range(self.num_epochs):
            # predict 
            y_pred = self.predict(self.X_data)

            # compute loss
            loss = self.compute_loss(y_pred, self.y_target)

            # compute gradient
            loss_grd = 2 * (y_pred - self.y_target) / self.num_epochs
            gradient = self.X_data.T.dot(loss_grd)

            # update weight
            self.theta = self.theta - self.learning_rate * gradient

            if (epoch % 50) == 0:
                print(f"Epoch: {epoch} - Loss: {loss}")
        
        return {
            'loss': sum(self.losses)/ len(self.losses),
            'weight': self.theta
        }

def r2_score(y_pred, y):
    rss = np.sum((y_pred - y)**2)
    tss = np.sum((y - y.mean())**2)
    r2 = 1 - (rss / tss)
    return r2

if __name__ =="__main__":
    y_pred = np.array([1, 2, 3, 4, 5])
    y = np.array([1, 2, 3, 4, 5])
    print(r2_score(y_pred, y))

    y_pred = np.array([1, 2, 3, 4, 5])
    y = np.array([3, 5, 5, 2, 4])
    print(r2_score(y_pred, y))
