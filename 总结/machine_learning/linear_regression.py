"""
reference: https://github.com/RRdmlearning/Machine-Learning-From-Scratch/blob/master/linear_regression/linear_regression.py

    https://towardsdatascience.com/building-a-logistic-regression-in-python-301d27367c24
loss function: l=\frac{1}{m}\sum _{i=1}^{m}(x_iw - y_i)^2
matrix form: l=(y-xw)^T(y-xw)
SGD: \frac{\partial{l}}{\partial w}=x^T(y-xw)
least square method: w^*=(X^TX)^{-1}X^Ty
"""
import numpy as np
from sklearn.datasets import make_regression

def split_train_test(x, y, seed=0, training_ratio=0.8):
    if seed:
        np.random.seed(seed)
    idx = np.arange(x.shape[0])
    np.random.shuffle(idx)
    x, y = x[idx], y[idx]
    train_counts = int(x.shape[0] * training_ratio)
    train_x, train_y = x[: train_counts, :], y[: train_counts]
    test_x, test_y = x[train_counts, :], y[train_counts:]
    return train_x, train_y, test_x, test_y


class L1Regularation(object):
    def __init__(self, alpha=0.1):
        self.alpha = alpha

    def __call__(self, w):
        reg_loss = np.sum(np.fabs(w))
        return reg_loss * self.alpha

    def grad(self, w):
        return self.alpha * np.sign(w)


class L2Regularation(object):
    def __init__(self, alpha=0.1):
        self.alpha = alpha

    def __call__(self, w):
        reg_loss = w.T.dot(w)
        return self.alpha * reg_loss

    def grad(self, w):
        return 2.0 * self.alpha * w


class LinearRegression(object):
    def __init__(self, learning_rate=0.01, n_iterations=2000, solver='sgd', regularization=None):
        """
        :param learning_rate:
        :param n_iterations:
        :param solver: optimize algorithm: [sgd, lsm] least square method/stochastic gradient descent
        :param regularization:
        """
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.solver = solver
        if regularization is None:
            self.regularization = lambda x: 0
            self.regularization.grad = lambda x: 0
        else:
            self.regularization = regularization
        assert self.solver in ['sgd', 'lsm']

    def init_weights(self, n_features):
        self.w = np.random.normal(size=(n_features, 1))

    def fit(self, X, y):
        """
        :param X: (m, n)
        :param y: (m, 1)
        :return:
        """
        training_errors = list()
        y = np.reshape(y, (-1, 1))
        assert 2 == len(X.shape) and 2 == len(y.shape)
        self.init_weights(n_features=X.shape[1])
        if self.solver == 'sgd':
            for idx in range(1, 1 + self.n_iterations):
                y_pred = X.dot(self.w)
                training_loss = np.mean(0.5 * (y_pred - y) ** 2) + self.regularization(self.w)
                training_errors.append(training_loss)
                grad = X.T.dot(y_pred - y) + self.regularization.grad(self.w)
                self.w = self.w - self.learning_rate * grad
                if idx % 50 == 0:
                    print('training loss=%.4f' % training_loss)
        elif self.solver == 'lsm':
            X, y = np.matrix(X), np.matrix(y)
            if abs(np.linalg.det(X.T.dot(X))) < 1e-8:
                print('the matrix was irreversible.')
                return
            X_T_X_I = (X.T.dot(X)).I
            X_T_Y = X.T.dot(y)
            self.w = X_T_X_I.dot(X_T_Y)
        else:
            raise ValueError('')

    def predict(self, X):
        X = np.matrix(X)
        return X.dot(self.w)

    def coef_(self):
        return self.w.flatten()


if __name__ == '__main__':
    X, y = make_regression(n_samples=100, n_features=10, noise=20)
    # train_x, train_y, test_x, test_y = split_train_test(X, y)
    model = LinearRegression(regularization =L2Regularation())
    # model.fit(train_x, train_y)

    model.fit(X, y)
