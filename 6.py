import pandas as pd

from sklearn.naive_bayes import GaussianNB


data = pd.read_csv('6.csv')

print(data.describe())

x = data.iloc[:, :-1]
print(x.head())

y = data.iloc[:, -1]
print( y.head())


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.20)

print("Total Available Instances: ", len(x))

print("Training Examples = {0}\nTesting Examples = {1}".format(len(X_train), len(X_test)))


classifier = GaussianNB()
classifier.fit(X_train, y_train)


print("Accuracy of classifier  is:",classifier.score(X_test, y_test))




###############################################################################


  6         148          72  ...       0.627          50           1
count  766.000000  766.000000  766.000000  ...  766.000000  766.000000  766.000000
mean     3.845953  120.895561   69.100522  ...    0.471879   33.232376    0.348564
std      3.371511   31.983485   19.380782  ...    0.331666   11.754161    0.476827
min      0.000000    0.000000    0.000000  ...    0.078000   21.000000    0.000000
25%      1.000000   99.000000   62.000000  ...    0.243250   24.000000    0.000000
50%      3.000000  117.000000   72.000000  ...    0.372500   29.000000    0.000000
75%      6.000000  140.000000   80.000000  ...    0.625500   41.000000    1.000000
max     17.000000  199.000000  122.000000  ...    2.420000   81.000000    1.000000

[8 rows x 9 columns]
   6  148  72  35    0  33.6  0.627  50
0  1   85  66  29    0  26.6  0.351  31
1  8  183  64   0    0  23.3  0.672  32
2  1   89  66  23   94  28.1  0.167  21
3  0  137  40  35  168  43.1  2.288  33
4  5  116  74   0    0  25.6  0.201  30
0    0
1    1
2    0
3    1
4    0
Name: 1, dtype: int64
Total Available Instances:  766
Training Examples = 612
Testing Examples = 154
Accuracy is: 0.7597402597402597
