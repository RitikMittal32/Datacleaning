import pandas as pd
import numpy as np
import seaborn as sns
import os

dfd = pd.read_csv("50_Startups.csv")
print(dfd)

#Handling the problem

#step1 -> Detecting the n/a and 0 values

missing_value = ['0']
df = pd.read_csv("50_Startups.csv", na_values = missing_value)
p = df.isnull().sum()
print(p)

c = df.isnull().any()
print(c)

m = sns.heatmap(df.isnull() , yticklabels=False, annot=True) # To visualize the datasheet which you have
print(m)

#step2 -> lets learn how to remove this values

a = df.dropna(how= 'all')
print(a)

f = df.fillna(method='ffill')
print(f)

b = df.fillna(method='bfill')
print(b)

i = df.interpolate()
print(i)

cf = df.fillna({
    'R&D Spend' : 2,
    'Marketing Spend':  1
})
print(cf)

df11 = pd.DataFrame(data={
    "New York":[],
    "California" : [],
    "Florida": []
})

print(df11)