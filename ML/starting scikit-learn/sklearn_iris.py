from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt
from pdr import PlotDecisionRegions as PDR
from adaline_sklearn import LogisticRegressionGD as LRGD

pdr = PDR()

iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y)

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# ppn = Perceptron(eta0=0.1, random_state=1)
# ppn.fit(X_train_std, y_train)

# print('Misclassified: %d' % (y_test != y_pred).sum())
# y_pred = ppn.predict(X_test_std)

X_combined_std = np.vstack((X_train_std, X_test_std))
X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))
# pdr.plot_decision_regions_idx(X=X_combined_std, y=y_combined, classifier=ppn, test_idx=range(105, 150))

# X_train_01_subset = X_train_std[(y_train == 0) | (y_train == 1)]
# y_train_01_subset = y_train[(y_train == 0) | (y_train == 1)]

# lrgd = LRGD(eta=0.3, n_iter=1000, random_state=1)
# lrgd.fit(X_train_01_subset, y_train_01_subset)
# pdr.plot_decision_regions(X=X_train_01_subset, y=y_train_01_subset, classifier=lrgd)

# lr = LogisticRegression(C=100.0, solver='lbfgs', multi_class='ovr')
# lr.fit(X_train_std, y_train)
# pdr.plot_decision_regions_idx(X_combined_std, y_combined, classifier=lr, test_idx=range(105, 150))

# weights, params = [],[]
# for c in np.arange(-5, 5):
#     lr = LogisticRegression(C=10.**c, multi_class='ovr')
#     lr.fit(X_train_std, y_train)
#     weights.append(lr.coef_[1])
#     params.append(10.**c)

# weights = np.array(weights)
# plt.plot(params, weights[:, 0], label='Petal length')
# plt.plot(params, weights[:, 1], linestyle='--', label='Petal width')

# plt.ylabel('Weigth coefficient')
# plt.xlabel('C')
# plt.legend(loc='upper left')
# plt.xscale('log')
# plt.show()

# svm = SVC(kernel='rbf', C=1.0, gamma=100.0, random_state=1)
# svm.fit(X_train_std, y_train)
# pdr.plot_decision_regions_idx(X_combined_std, y_combined, classifier=svm, test_idx=range(105,150))

# tree_model = tree.DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=1)
# tree_model.fit(X_train, y_train)
# X_combined = np.vstack((X_train, X_test))
# pdr.plot_decision_regions_idx(X_combined, y_combined, classifier=tree_model, test_idx=range(105, 150))

# feature_names = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']
# tree.plot_tree(tree_model, feature_names=feature_names, filled=True)
# plt.show()

# forest = RandomForestClassifier(n_estimators=25, random_state=1, n_jobs=2)
# forest.fit(X_train, y_train)
# pdr.plot_decision_regions_idx(X_combined, y_combined, classifier=forest, test_idx=range(105,150))

knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn.fit(X_train_std, y_train)
pdr.plot_decision_regions_idx(X_combined_std, y_combined, classifier=knn, test_idx=range(105,150))


plt.xlabel('Petal length [standardized]')
plt.ylabel('Petal width [standardized]')
plt.legend(loc='upper left')
# plt.xlabel('Petal length [cm]')
# plt.ylabel('Petal width [cm]')
# plt.legend(loc = 'upper left')


plt.tight_layout()
plt.show()