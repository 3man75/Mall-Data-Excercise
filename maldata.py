import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np



m_data = 'Mall_Customers.csv' #filelocation is with program

df = pd.read_csv(m_data,sep=',') #pandas dataframe that goes into variable

age_min = 19 #the ages I want to filter data by

age_max = 24

df_age_19_24 = df.query("@age_min <= Age <= @age_max") #filtered csv by age

print(df_age_19_24) #print list by age


total = df('Annual Income').sum()
print(total)



np_1 = df.to_numpy() #numpy array made from dataframe




#Problem: look through list and print out a list of all customers who are between ages of 19-24 and make a list of it.
    
    





#Problem: add to an append() and sum ages 19-24 annual income for total purchasing power

#Problem: pie chart of male female breakdown
   





