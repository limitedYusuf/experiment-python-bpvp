import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('diabetes.csv')

X = data.drop('Outcome', axis=1)
y = data['Outcome']

def gini_impurity(y):
    _, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    gini = 1 - np.sum(probabilities**2)
    return gini

def gini_gain(y, left_y, right_y):
    p = len(left_y) / len(y)
    gini_before = gini_impurity(y)
    gini_left = gini_impurity(left_y)
    gini_right = gini_impurity(right_y)
    gain = gini_before - p * gini_left - (1 - p) * gini_right
    return gain

def split_data(X, y, feature_index, threshold):
    left_mask = X[:, feature_index] <= threshold
    right_mask = X[:, feature_index] > threshold
    left_y = y[left_mask]
    right_y = y[right_mask]
    left_X = X[left_mask]
    right_X = X[right_mask]
    return left_X, left_y, right_X, right_y

def build_decision_tree(X, y, depth=0, max_depth=None, min_samples_split=2):
    num_samples, num_features = X.shape
    unique_classes, counts = np.unique(y, return_counts=True)
    default_class = unique_classes[np.argmax(counts)]
    
    if depth == max_depth or num_samples < min_samples_split or len(np.unique(y)) == 1:
        return default_class
    
    best_gain = 0
    best_feature = None
    best_threshold = None
    best_left_X = None
    best_left_y = None
    best_right_X = None
    best_right_y = None
    
    for feature_index in range(num_features):
        thresholds = np.unique(X[:, feature_index])
        for threshold in thresholds:
            left_X, left_y, right_X, right_y = split_data(X, y, feature_index, threshold)
            if len(left_y) == 0 or len(right_y) == 0:
                continue
            gain = gini_gain(y, left_y, right_y)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature_index
                best_threshold = threshold
                best_left_X = left_X
                best_left_y = left_y
                best_right_X = right_X
                best_right_y = right_y
                
    if best_gain > 0:
        left_subtree = build_decision_tree(best_left_X, best_left_y, depth + 1, max_depth, min_samples_split)
        right_subtree = build_decision_tree(best_right_X, best_right_y, depth + 1, max_depth, min_samples_split)
        return (best_feature, best_threshold, left_subtree, right_subtree)
    else:
        return default_class

def predict_tree(node, X):
    if isinstance(node, tuple):
        feature, threshold, left_subtree, right_subtree = node
        if X[feature] <= threshold:
            return predict_tree(left_subtree, X)
        else:
            return predict_tree(right_subtree, X)
    else:
        return node

def accuracy_score(y_true, y_pred):
    return np.mean(y_true == y_pred)

def plot_tree(node, depth=0, feature_names=None, class_names=None, indent="  "):
    if isinstance(node, tuple):
        feature, threshold, left_subtree, right_subtree = node
        if feature_names is not None:
            feature_name = feature_names[feature]
        else:
            feature_name = f"feature {feature}"
        print(indent * depth + f"if {feature_name} <= {threshold}:")
        plot_tree(left_subtree, depth + 1, feature_names, class_names, indent)
        print(indent * depth + f"else:  # if {feature_name} > {threshold}")
        plot_tree(right_subtree, depth + 1, feature_names, class_names, indent)
    else:
        class_name = class_names[node] 
        print(indent * depth + f"class: {class_name}")

if __name__ == "__main__":
    decision_tree = build_decision_tree(X.values, y.values, max_depth=3)
    
    def plot_tree_matplotlib(node, feature_names, class_names):
        if isinstance(node, tuple):
            feature, threshold, left_subtree, right_subtree = node
            feature_name = feature_names[feature]
            plt.figure(figsize=(12, 6))
            plt.title(f"Decision Tree: {feature_name} <= {threshold}")
            
            plt.subplot(1, 2, 1)
            plot_tree_matplotlib(left_subtree, feature_names, class_names)
            plt.title(f"if {feature_name} <= {threshold}")
            
            plt.subplot(1, 2, 2)
            plot_tree_matplotlib(right_subtree, feature_names, class_names)
            plt.title(f"else:  # if {feature_name} > {threshold}")
        else:
            class_name = class_names[node]
            plt.text(0.5, 0.5, class_name, ha='center', va='center', fontsize=20)
            plt.axis('off')
    
    feature_names = X.columns
    class_names = ["No Diabetes", "Diabetes"]
    plot_tree_matplotlib(decision_tree, feature_names, class_names)
    
    plt.savefig("decision_tree.png", bbox_inches='tight')
    
    y_pred = [predict_tree(decision_tree, x) for x in X.values]
    
    accuracy = accuracy_score(y, y_pred)
    print("Akurasi:", accuracy)

plt.show()
