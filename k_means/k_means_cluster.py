#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

keys = data_dict.keys()
stocks = []
salaries = []
for person in keys:
    stock = data_dict[person]['exercised_stock_options']
    salary = data_dict[person]['salary']
    if(stock != 'NaN'):
        stocks.append(stock)
    if(salary != 'NaN'):
        salaries.append(salary)

# print 'exercised_stock_options MAX:', max(stocks)
# print 'exercised_stock_options MIN:', min(stocks)

# print 'Salary MAX:', max(salaries)
# print 'Salary MIN:', min(salaries)

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
# feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

# sacled data before running
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaledData = scaler.fit_transform(finance_features)


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)

###
#### For EX-16 compare the index and step to get the answer easily
###

# WITHOUT scaled data
# step = 0
# for f1, f2 in finance_features:
#     plt.scatter( f1, f2 )
    # if(f2 >= 1000000 and f2 <= 1500000):
    #     print step, ": ", f1
    # step = step + 1
# plt.show()

# WITH scaled data
index =0 
for f1, f2 in scaledData:
    plt.scatter( f1, f2 )
    # print index, ": ", f2
    # index = index + 1
# plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

# WITHOUT scaled data
# from sklearn.cluster import KMeans
# kmeans = KMeans(n_clusters=2).fit(finance_features)
# pred = kmeans.predict(finance_features)

#  WITH sclaed data

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(scaledData)
pred = kmeans.predict(scaledData)



### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    # WITHOUT scaled data
    # Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
    
    # WITH scaled data
    Draw(pred, scaledData, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
