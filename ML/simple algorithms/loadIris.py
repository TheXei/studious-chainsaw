import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from perceptron import Perceptron as perc
from adaline import AdalineGD as AGD
from adaline import AdalineSGD as ASGD

# s = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# print('From URL:', s)

df = pd.read_csv('C:\\Users\Marcus\Documents\studious-chainsaw\ML\iris.csv', header=None, encoding='utf-8')

# select setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', 0, 1)
# extract sepal length and petal length
X = df.iloc[0:100, [0, 2]].values
# plot data
# plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='Setosa')
# plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='s', label='Versicolor')

# plt.xlabel('Sepal length [cm]')
# plt.ylabel('Petal length [cm]')
# plt.legend(loc='upper left')

# plt.show()

# ppn = perc(eta=0.1, n_iter=10)
# ppn.fit(X, y)
# # plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
# # plt.xlabel('Epochs')
# # plt.ylabel('Number of updates')
# # plt.show()

def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers = ('o', 's', '^', 'v', '<')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    lab = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    lab = lab.reshape(xx1.shape)
    plt.contourf(xx1, xx2, lab, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x = X[y == cl, 0],
                    y = X[y == cl, 1],
                    alpha = 0.8,
                    c = colors[idx],
                    marker = markers[idx],
                    label = f'Class {cl}',
                    edgecolor = 'black')
        
# plot_decision_regions(X, y, classifier=ppn)
# plt.xlabel('Sepal length [cm]')
# plt.ylabel('Petal length [cm]')
# plt.legend(loc='upper left')
# plt.show()

# fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,4))
# ada1 = AGD(n_iter=15, eta=0.1).fit(X, y)
# ax[0].plot(range(1, len(ada1.losses_) + 1), np.log10(ada1.losses_), marker='o')
# ax[0].set_xlabel('Epochs')
# ax[0].set_ylabel('log(Mean squared error)')
# ax[0].set_title('Adaline - Learning rate 0.1')

# ada2 = AGD(n_iter=15, eta=0.0001).fit(X, y)
# ax[1].plot(range(1, len(ada2.losses_) + 1), ada2.losses_, marker='o')
# ax[1].set_xlabel('Epochs')
# ax[1].set_ylabel('Mean squared error')
# ax[1].set_title('Adaline - Learning rate 0.0001')
# plt.show()

X_std = np.copy(X)
X_std[:,0] = (X[:,0] - X[:,0].mean()) / X[:,0].std()
X_std[:,1] = (X[:,1] - X[:,1].mean()) / X[:,1].std()

# ada_gd = AGD(n_iter=20, eta=0.5)
# ada_gd.fit(X_std, y)

# plot_decision_regions(X_std, y, classifier=ada_gd)
# plt.title('Adaline - Gradient descent')
# plt.xlabel('Sepal length [standardized]')
# plt.ylabel('Petal length [standardized]')
# plt.legend(loc='upper left')
# plt.tight_layout()
# plt.show()

# plt.plot(range(1, len(ada_gd.losses_) + 1), ada_gd.losses_, marker='o')
# plt.xlabel('Epochs')
# plt.ylabel('Mean squared error')
# plt.tight_layout()
# plt.show()

ada_sgd = ASGD(n_iter=15, eta=0.01, random_state=1)
ada_sgd.fit(X_std, y)

plot_decision_regions(X_std, y, classifier=ada_sgd)
plt.title('Adaline - Stochastic gradient descent')
plt.xlabel('Sepal length [standardized]')
plt.ylabel('Petal length [standardized]')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()

plt.plot(range(1, len(ada_sgd.losses_) + 1), ada_sgd.losses_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Mean squared error')
plt.tight_layout()
plt.show()