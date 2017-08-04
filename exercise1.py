from sklearn import tree

features = [
    # horsepower and the number of seats
    [300, 2], 
    [450, 2], 
    [200, 8], 
    [150, 9]
]

# 0  for "sport-cars", 1 for "minivan"
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# pass in horsepower (150)  and the number of seats
print clf.predict([[160, 4]])
