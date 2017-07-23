

import pandas as pd

data = pd.read_csv('train.csv')
data.head()


Y_train = data.iloc[:,9].values

data = data.drop('offerid',axis = 1)

data = data.drop('merchant',axis = 1)


X_train = data.iloc[:,2:7].values

from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()
X_train[:,2] = label.fit_transform(X[:,2])
X_train[:,2] = label.fit_transform(X_train[:,2])

label_browser = LabelEncoder()
label_dev = LabelEncoder()
X_train[:,3] = label_browser.fit_transform(X_train[:,3])
X_train[:,4] = label_dev.fit_transform(X_train[:,4])

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)
imputer = imputer.fit(X_train[:, 0:5])
X_train[:, 0:5] = imputer.transform(X_train[:, 0:5])


"""from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder()"""

onehotencoder = OneHotEncoder(categorical_features = [2,3,4])
X_train = onehotencoder.fit_transform(X_train).toarray()
len(X_train)
len(X_train[1,:])

onehotencoder1 = OneHotEncoder(categorical_features = [1])
X_train = onehotencoder.fit_transform(X_train).toarray()


onehotencoder2 = OneHotEncoder(categorical_features = [0])
X_train = onehotencoder.fit_transform(X_train).toarray()


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, Y_train)
