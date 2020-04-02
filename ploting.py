# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:05:59 2020

@author: Admin
"""

import seaborn as sns
df=sns.load_dataset("tips")

df.head()   

df.corr()

sns.heatmap(df.corr())

# ************ for continous ploting of variables **************
"""

1) Jointplot
2) Pairplot
3) Distplot

"""

# total bill vs tip (Joint plot)
sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')

sns.jointplot(x='tip',y='total_bill',data=df,kind='reg')

# this plot is between 2 features of int or float data from the dataframe 2^features plots will be there
sns.pairplot(df)

# can be done for catogories like specifically we want to know the 
# total bill vs tip plot for different sex or for if one smokes or not than we can do this

sns.pairplot(df,hue='smoker')

sns.pairplot(df,hue='sex')

sns.distplot(df['tip'],bins=10)

sns.distplot(df['tip'],bins=10,kde=False)

# *************till here ********************

# ************ for discrete(categorical) ploting of variables **************
"""
1) Countplot
2) boxplot
3) Violinplot
4) barplot
"""
sns.countplot('sex',data=df) # default it will take x='sex' (vertical)

sns.countplot(y='sex',data=df) # for horizontal 

sns.boxplot(x='sex',y='total_bill',data=df)
sns.boxplot(x='sex',y='total_bill',data=df,palette='rainbow')

sns.boxplot(data=df)  # for whole data

sns.boxplot(y='day',x='total_bill',hue='sex',data=df,palette='rainbow')

sns.violinplot(y='day',x='total_bill',hue='sex',data=df,palette='rainbow')

sns.barplot(y='total_bill',x='sex',data=df)

import IPython.nbformat.current as nbf
nb = nbf.read(open('ploting.py', 'r'), 'py')
nbf.write(nb, open('ploting1.ipynb', 'w'), 'ipynb')
