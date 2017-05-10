import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from config import *
from sklearn.metrics import roc_auc_score
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import datetime
import sys
from sklearn.externals import joblib

def read_data(datapath):
    df = pd.read_csv(datapath, header = None)
    return df

def get_label_feat(df):
    x = df.drop([0], axis=1)
    y = df[0]
    return x, y

def randomforest():
    print >> sys.stderr, "This Classifier is RandomForest", datetime.datetime.now()
    print >> sys.stderr, "TrainingSet Feature Extraction... ", datetime.datetime.now()
    train_df = read_data(traindata_path)
    train_x, train_y = get_label_feat(train_df)
    """
    mp = {}
    for item in train_y:
        if mp.has_key(item):
            mp[item] = mp[item] + 1
    else:
        mp[item] = 1
    for key in mp:
        print mp[key]
    """
    print >> sys.stderr, "TestingSet Feature Extraction... ", datetime.datetime.now()
    test_df = read_data(testdata_path)
    test_x, test_y = get_label_feat(test_df)
    clf = RandomForestClassifier(n_estimators=100, max_depth=7)
    rf = clf.fit(train_x.values, train_y.values)
    score = cross_val_score(clf, train_x, train_y, cv=3)
    print >> sys.stderr, "Cross Validation" ,score ,datetime.datetime.now()
    print clf.score(test_x.values, test_y.values)
    joblib.dump(rf, './model/rf.model',compress=3)

def knn():
    print >> sys.stderr, "This Classifier is KNN", datetime.datetime.now()
    print >> sys.stderr, "TrainingSet Feature Extraction... ", datetime.datetime.now()
    train_df = read_data(traindata_path)
    train_x, train_y = get_label_feat(train_df)
    print >> sys.stderr, "TestingSet Feature Extraction... ", datetime.datetime.now()
    test_df = read_data(testdata_path)
    test_x, test_y = get_label_feat(test_df)
    knn_clf = KNeighborsClassifier(n_neighbors=5, algorithm='kd_tree', weights='distance', p=3)
    knn_clf.fit(train_x.values,train_y.values)
    score = cross_val_score(knn_clf,train_x,train_y,cv=3)
    print >> sys.stderr,"Cross Validation", score, datetime.datetime.now()
    print knn_clf.score(test_x.values, test_y.values)
def main():
    randomforest()
    knn()
if __name__ == '__main__':
    main()
