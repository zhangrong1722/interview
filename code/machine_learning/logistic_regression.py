"""
reference: https://www.cnblogs.com/luozeng/p/8605140.html
           https://towardsdatascience.com/building-a-logistic-regression-in-python-301d27367c24
"""
import numpy as np

class LogisticRegression(object):
    def __init__(self, learning_rate=0.01, n_iterations=2000, log_intervals=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.log_intervals = log_intervals

    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-x))

    def init_weights(self, n_features):
        self.w = np.random.normal(size=(n_features, 1))

    def cross_entropy(self, pred, y):
        return -np.mean(y * np.log(pred) + (1 - y) * np.log(1 - pred))

    def fit(self, X, y):
        self.init_weights(n_features = X.shape[1])
        training_error = list()
        for idx in range(self.n_iterations):
            pred = self.sigmoid(X.dot(self.w))
            loss = self.cross_entropy(pred, y)
            training_error.append(loss)
            grad = X.T.dot(pred - y)
            self.w = self.w - self.learning_rate * grad
            if idx % self.log_intervals == 0:
                print('training loss=%.4f' % loss)

    def predict(self, X):
        return self.sigmoid(X.dot(self.w))

    def coef_(self):
        return self.w.flatten()