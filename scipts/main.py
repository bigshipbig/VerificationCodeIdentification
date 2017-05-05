import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from config import *
from sklearn.metrics import roc_auc_score
from sklearn.cross_validation import cross_val_score
import time
import datetime
import sys

def read_data(datapath):
    df = pd.read_csv(datapath, header = None)
    return df

def get_label_feat(df):
    x = df.drop([0], axis=1)
    y = df[0]
    return x, y

def main():
    print >> sys.stderr, "TrainingSet Feature Extraction... ", datetime.datetime.now()
    train_df = read_data(traindata_path)
    train_x, train_y = get_label_feat(train_df)
    print >> sys.stderr, "TestingSet Feature Extraction... ", datetime.datetime.now()
    test_df = read_data(testdata_path)
    test_x, test_y = get_label_feat(test_df)
    print train_y.shape
    print train_x.shape
    clf = RandomForestClassifier(n_estimators = 100, max_depth = 7)
    clf.fit(train_x.values,train_y.values)
    score = cross_val_score(clf,train_x,train_y,cv=3)
    print score
    print clf.score(test_x.values,test_y.values)
if __name__ == '__main__':
    main()