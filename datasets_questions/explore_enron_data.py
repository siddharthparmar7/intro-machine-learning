#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(
    open("../final_project/final_project_dataset.pkl", "r"))

# knowSalary = 0
# knownEmailAdd = 0
# for person in enron_data:
#     if enron_data[person]["salary"] != 'NaN':
#         knowSalary += 1
#     if enron_data[person]["email_address"] != 'NaN':
#         knownEmailAdd += 1

# print ('Know Salary:', knowSalary, ' Known Email Addresses:', knownEmailAdd)

# print (enron_data['LAY KENNETH L'])

# count = 0
# for person in enron_data:
#     if enron_data[person]["total_payments"] == 'NaN':
#         count += 1

# print count * 100 / len(enron_data)

count = 0
for person in enron_data:
    if enron_data[person]["poi"] == True and enron_data[person]["total_payments"] == 'NaN':
        count += 1

print count
