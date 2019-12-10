"""
reference: https://github.com/RRdmlearning/Machine-Learning-From-Scratch/blob/master/decision_tree/decision_tree_model.py
"""
import numpy as np

class DecisionNode(object):
    def __init__(self, split_feature_idx=None, leaf_value=None, threshold=None, left_children=None, right_children=None):
        self.split_feature_idx = split_feature_idx
        self.leaf_value = leaf_value
        self.threshold = threshold
        self.left_children = left_children
        self.right_children = right_children

class DecisionTree(object):
    def __init__(self, min_leaves=5, impurity_calculation=None, leaf_value_calculation=None, min_impurity=1e-7):
        """
        :param min_leaves: 建立决策树的最少样本个数
        :param impurity_calculation: GINI系数/MSE
        :param leaf_value_calculation: 计算叶子节点值 均值（回归树）/出现次数最多的标签（分类树）
        :param min_impurity: 最小纯度：GINI系数/MSE
        """
        self.min_leaves = min_leaves
        self.min_impurity = min_impurity
        self.impurity_calculation = impurity_calculation
        self.leaf_value_calculation = leaf_value_calculation

    def split_features(self, feature_idx, X, y, threshold):
        """
        根据threshold将数据分为两部分
        :param feature_idx: feature index
        :param X: 数据
        :param y: 标签
        :param threshold: 阈值
        :return: 两部分索引
        """
        return None, None

    def check_datatype(self, x):
        assert isinstance(x, np.ndarray) and x.dtype in [int, float]

    def predict(self):
        pass

    def fit(self, X, y):
        n_sample, n_features = X.shape[0], X.shape[1]
        if len(y.shape) == 1:
            y = np.reshape(y, (n_sample, 1))
        self.check_datatype(X)
        self.check_datatype(y)
        best_split_feature, largest_impurity, split_var, best_left_idx, best_right_idx = None, 0.0, None, None, None
        if n_sample > self.min_leaves:
            for feature_idx in range(n_features):
                unique_values = np.unique(X[: , feature_idx])
                for threshold in unique_values:
                    # 根据threshold将样本分为left和right两部分
                    left_idx, right_idx = self.split_features(feature_idx, X, y, threshold)
                    # 对每个属性计算信息增益/信息增益率/GINI系数
                    score = self.impurity_calculation(y, left_idx, right_idx)
                    # 更新best_split_feature, largest_impurity, split_var参数
                    if score > largest_impurity:
                        best_split_feature, largest_impurity, split_var, best_left_idx, best_right_idx = \
                            feature_idx, score, feature_idx, left_idx, right_idx

        if largest_impurity > self.min_impurity:
            left_subtree_x = np.delete(X[best_left_idx, :], best_split_feature, axis=1)
            left_subtree_y = y[best_left_idx, :]

            right_subtree_x = np.delete(X[best_right_idx, :], best_split_feature, axis=1)
            right_subtree_y = y[best_right_idx, :]
            left_subtree = self.fit(left_subtree_x, left_subtree_y)
            right_subtree = self.fit(right_subtree_x, right_subtree_y)
            return DecisionNode(split_feature_idx=best_split_feature, threshold=split_var,
                                left_children=left_subtree,
                                right_children=right_subtree)

        # 叶子节点 计算叶子节点值 均值（回归树）/出现次数最多的标签（分类树）
        return DecisionNode(leaf_value=self.leaf_value_calculation(y))

class RegressionTree(DecisionTree):
    def fit(self, X, y):
        pass

class ClassifierTree(DecisionTree):
    def __init__(self):
        super().__init__()