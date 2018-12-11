#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL')
data = featureFormat(data_dict, features)

all_data_in_tuples = data_dict.items()
### your code below
all_bonus = []
import matplotlib.pyplot as plt
for point in data:
    salary = point[0]
    bonus = point[1]
    all_bonus.append(bonus)
    plt.scatter(salary, bonus)

plt.xlabel("Salary")
plt.ylabel("Bonus")
plt.show()

# find an outlier
all_bonus = sorted(all_bonus,reverse= True)
max_bonus = max(all_bonus)
second_max_bonus = all_bonus[1]

for person in all_data_in_tuples:
    if(person[1]['salary'] > 1000000 and person[1]['bonus'] > 5000000 and person[1]['bonus'] != 'NaN'):
        print person[0], " bonus:", person[1]['bonus'], " Salary:", person[1]['salary']




