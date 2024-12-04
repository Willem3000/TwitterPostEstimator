import sklearn
from sklearn.linear_model import ElasticNet
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
import numpy as np

def Build_Data_Set():
    # gets data frame
    datapath = "../data/"
    df = pd.read_csv("combined_csv.csv")

    # shuffles our data
    df = sklearn.utils.shuffle(df)

    # removes n/a values
    df = df.dropna()

    # converts our wished features to a 2d list
    _df = df.drop(['date', 'time', 'hashtags', 'cashtags', 'username', 'likes_count', 'photos', 'video'], 1)
    X = np.array(_df)

    # gets status data
    y = np.array(df['likes_count'])

    # preprocessing your data | normalization
    # X = preprocessing.scale(X)

    return X, y

def analyse():
    # call the Build_Data_Set() function to get X, y
    X, y = Build_Data_Set()

    # communication is important
    print("X std: ", X.std())  # since we preprocessed our data "std" should be close to 1.0
    print("len of x: ", len(X))  # the len of our example size
    print("------------------------------------------")

    # print(np.count_nonzero(y_train == -1))
    # print(np.count_nonzero(y_train == 1))

    # build our svm model
    # clf = svm.SVC(kernel="linear", C=1.0, verbose=1)
    regr = ElasticNet(random_state=0)

    acc = []
    for i in range(100):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.01)
        # trains our model
        regr = regr.fit(X, y)
        # predicts training samples
        pred = regr.predict(X)
        print(i)
        # print(np.count_nonzero(pred == -1))
        # print(np.count_nonzero(pred == 1))
        print(accuracy_score(x_test, y_test))
        print("-------------------------")