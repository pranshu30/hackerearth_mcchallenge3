import pandas as pd

data = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

import numpy as np
import time
import datetime


#Convert train time to timestamp(unix code)
def convert_to_timestamp(date):
    date_as_string = str(date).strip()
    return time.mktime(datetime.datetime.strptime(date_as_string,"%d-%m-%Y %H:%M").timetuple())

    
data['datetime']= data['datetime'].apply(convert_to_timestamp)
test['datetime']= test['datetime'].apply(convert_to_timestamp)

#Train
Y_train = data.iloc[:,9].values
X_train = data.iloc[:,1:9].values

from sklearn.preprocessing import LabelEncoder
label1 = LabelEncoder()
label2 = LabelEncoder()
label3 = LabelEncoder()
label4 = LabelEncoder()
label5 = LabelEncoder()
label6 = LabelEncoder()
label7 = LabelEncoder()
X_train[:,1] = label1.fit_transform(X_train[:,1])
X_train[:,2] = label2.fit_transform(X_train[:,2])
X_train[:,3] = label3.fit_transform(X_train[:,3])
X_train[:,4] = label4.fit_transform(X_train[:,4])
X_train[:,5] = label5.fit_transform(X_train[:,5])
X_train[:,6] = label6.fit_transform(X_train[:,6])
X_train[:,7] = label7.fit_transform(X_train[:,7])

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)
imputer = imputer.fit(X_train[:, 0:8])
X_train[:, 0:8] = imputer.transform(X_train[:, 0:8])


#Test
X_test = test.iloc[:,1:9].values
label1t = LabelEncoder()
label2t = LabelEncoder()
label3t = LabelEncoder()
label4t = LabelEncoder()
label5t = LabelEncoder()
label6t = LabelEncoder()
label7t = LabelEncoder()
X_test[:,1] = label1t.fit_transform(X_test[:,1])
X_test[:,2] = label2t.fit_transform(X_test[:,2])
X_test[:,3] = label3t.fit_transform(X_test[:,3])
X_test[:,4] = label4t.fit_transform(X_test[:,4])
X_test[:,5] = label5t.fit_transform(X_test[:,5])
X_test[:,6] = label6t.fit_transform(X_test[:,6])
X_test[:,7] = label7t.fit_transform(X_test[:,7])

imputert = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)
imputert = imputert.fit(X_test[:, 0:8])
X_test[:, 0:8] = imputert.transform(X_test[:, 0:8])


#--------------XGBOOST MODEL------------------
from xgboost import XGBClassifier
 classifier = XGBClassifier()
classifier.fit(X_train, Y_train)


y_pred = classifier.predict_proba(X_test)


df = pd.DataFrame(y_pred[:,1])


df.to_csv('C:\Users\pranshu30\Documents\Hackerearth\#3\output.txt',sep=' ',index=False, header=False)

