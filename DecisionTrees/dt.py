import numpy as np

from sklearn.tree import DecisionTreeClassifier

features_train = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2], [4, 5], [6, 7], [-1, 5], [30, 20], [-4, 15], [6, 12], [-3, 6]])
labels_train = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3])

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)

features_test = [[1, 1], [2, 6], [-1, -1], [8, 9], [3, 7]]
labels_test = [2, 3, 2, 3, 3]

pred = clf.predict(features_test)

print "Predict [3, 7] Result: ", clf.predict([[3, 7]])

from sklearn.metrics import accuracy_score
print "Accuracy: ", accuracy_score(labels_test, pred)
