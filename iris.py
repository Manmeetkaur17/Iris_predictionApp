# -*- coding: utf-8 -*-
"""iris.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RXKDOKCKOhfcTY8YCDsku7fSUdiY0VTT
"""

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

iris = sns.load_dataset('iris')

# iris.shape

# iris.info()

# iris.head()

# iris.describe()

target=iris['species']
features=iris.drop(['species'],axis=1)

#train test split
xtrain,xtest,ytrain,ytest=train_test_split(features,target,test_size=0.2,random_state=42)

# xtrain.shape,xtest.shape,ytrain.shape,ytest.shape

rfc=RandomForestClassifier()
rfc.fit(xtrain,ytrain)

y_pred=rfc.predict(xtest)
y_pred

train_acc=round((rfc.score(xtrain,ytrain))*100,2)
test_acc=round((rfc.score(xtest,ytest))*100,2)

print("train accuracy: ",train_acc)
print("Test accuracy: ",test_acc)

from sklearn.metrics import accuracy_score

acc_score = accuracy_score(ytest, y_pred)
print(acc_score)

joblib.dump(rfc,"MY_Iris_Model.sav")            #save model on disk

!pip install predictions

!pip install streamlit



import streamlit as st     #to deploy the model
from prediction import predict

st.title("Iris Flowers Predictions")
st.markdown('Toy model to play to classify iris flowers\ satosa, Versicolor, virginica')

st.header('Flowers features')
col1,col2 = st.columns(2)

with col1:
  st.text('Sepal characteristics')
  sepal_length =st.slider('sepal length (cm)', 1.0,8.0,0.5)
  sepal_width = st.slider('sepal width (cm)',2.0,4.4,0.5)

with col2:
  st.text('Petal characteristics')
  petal_length =st.slider('Petal length (cm)', 1.0,7.0,0.5)
  petal_width = st.slider('Petal width (cm)',0.1,2.5,0.5)

st.button('Predict Flower Type')

# !streamlit run iris.py &>/content/logs.txt &

# !npx localtunnel --port 8501

import sklearn
sklearn.__version__

import joblib
joblib.__version__

import pandas
pandas.__version__

!pip install streamlit
import streamlit
streamlit.__version__

