from sklearn import datasets
iris=datasets.load_iris()


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.1)


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(x_train, y_train)

y_pred=classifier.predict(x_test)


print("Results of Classification using K-nn") 
for r in range(0,len(x_test)):
    print(" Sample:", str(x_test[r]),
          " Actual-label:", str(y_test[r]),
          " Predicted-label:", str(y_pred[r]))

    print("Classification Accuracy :" , classifier.score(x_test,y_test))
