import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression

def FeaturesAndValues(values, features, notKnownnumber):
    indices = []
    ind = 'ind'
    df = pd.DataFrame()
    for f in range(0, features + 1):
        indices.append(ind+str(f))
    for v in range(0, values):
        inpt = input('Enter the features with a single space between everyone:')
        num = [int(n) for n in inpt.split()]
        length = len(num)
        if(length > features + 1 or length < features + 1):
            print('The number of feature does not match either they are less or extra!!')
            break
        else:
            df = df.append(pd.Series(num, index=indices), ignore_index=True)
    indices2 = [str(i) for i in indices]
    indices2.pop(-1)
    classFeature = df.iloc[:,-1]
    y = classFeature
    X = df[indices2].values
    regr = linear_model.LinearRegression()
    regr.fit(X,y)
    predicted = []
    for i in range(0, notKnownnumber):
        unknown = input('Enter the feature value which are not classified or you want to predict with spaces: ')
        unknum = [int(n) for n in unknown.split()]
        l = len(unknum)
        if(l > features or l < features):
            print("The number of features does not match either they are less or more!!")
            break
        else:
            uknum = [unknum]
            p = regr.predict(uknum)
            predicted.append(p)
    print(predicted)
