from sklearn import tree
# 1 for "smooth", 0 for "bumpy"
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# 1  for "oranges", 0 for "apples"
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# pass in weight (150) of the fruit and the texture (0 for bumpy)
print clf.predict([[160, 0]])
