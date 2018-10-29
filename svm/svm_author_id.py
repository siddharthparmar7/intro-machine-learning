#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
# pylint: disable=E0401
from email_preprocess import preprocess


# features_train and features_test are the features for the training
# and testing datasets, respectively
# labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

from sklearn import svm

# These lines effectively slice the training dataset down to 1% of its original size,
# tossing out 99% of the training data. You can leave all other code unchanged.

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf = svm.SVC(kernel='rbf', gamma="auto", C=10000)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
predictions = clf.predict(features_test)
print "predictions: ", predictions

chris_emails = filter(lambda (label): label == 1, predictions)
print "Number of emails by Chris: ", len(chris_emails)
# print "prediction for 10th element: ", predictions[10]
# print "prediction for 26th element: ", predictions[26]
# print "prediction for 50th element: ", predictions[50]
print "prediction time:", round(time()-t0, 3), "s"

acc = clf.score(features_test, labels_test)
print "accuracy", acc
#########################################################
