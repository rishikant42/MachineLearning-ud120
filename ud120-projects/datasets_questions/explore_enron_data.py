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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#print enron_data
#print len(enron_data)
#print enron_data['DONAHUE JR JEFFREY M']

#print len(enron_data['DONAHUE JR JEFFREY M'])

for k, v in enron_data.iteritems():
    print k, " ==> ", v
    print "\n"

no_of_poi = 0

#for k1, v1 in enron_data.iteritems():
#    if v1['poi'] == True:
#        no_of_poi += 1
#
#print no_of_poi

#print enron_data['PRENTICE JAMES']
#print enron_data['PRENTICE JAMES']['total_stock_value']

#print enron_data['COLWELL WESLEY']
#print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

#print enron_data['SKILLING JEFFREY K']
#print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
