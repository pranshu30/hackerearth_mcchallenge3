
import pandas as pd
#Read File
data = pd.read_csv('train.csv')
#data.head()


data = data.drop('offerid',axis = 1)
data = data.drop('merchant',axis = 1)


X_train = data.iloc[:,2:7].values
Y_train = data.iloc[:,9].values

#Label Encoding
from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()
X_train[:,2] = label.fit_transform(X_train[:,2])
label_browser = LabelEncoder()
label_dev = LabelEncoder()
X_train[:,3] = label_browser.fit_transform(X_train[:,3])
X_train[:,4] = label_dev.fit_transform(X_train[:,4])

#Handling missing values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)
imputer = imputer.fit(X_train[:, 0:5])
X_train[:, 0:5] = imputer.transform(X_train[:, 0:5])

#OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
"""onehotencoder = OneHotEncoder()"""

onehotencoder = OneHotEncoder() #For all categorical features
X_train = onehotencoder.fit_transform(X_train).toarray()

num_col = len(X_train[1,:])

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, Y_train)
