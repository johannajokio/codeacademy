import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

#open files
files = glob.glob('states*.csv')
#loop through, open files and append to list
df_list =[]
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
#concatenate list of dataframes together and #drop Unnamed column created
us_census = pd.concat(df_list)#.reset_index(drop=True).drop('Unnamed: 0', axis =1)
#ValueError: could not convert string to float: 'Alabama'

print(us_census.columns)
print(us_census.dtypes)
print(us_census.head())

#regex to turn income into numeric
us_census['Income'] = us_census.Income.replace('\$', '', regex=True)

us_census['Income'] = pd.to_numeric(us_census.Income)

#separate gender into columns
split = us_census.GenderPop.str.split("_")

us_census['Men'] = split.str.get(0)
us_census['Women'] = split.str.get(1)
print(split)
#take out character at the end and convert to numeric
us_census.Men = us_census.Men.replace('M','',regex=True)
us_census.Women = us_census.Women.replace('F','', regex=True)

#us_census['Men'] = us_census.Men.str[:-1]
#us_census['Women'] = us_census.Women.str[:-1]

us_census['Men'] = pd.to_numeric(us_census.Men)
us_census['Women'] = pd.to_numeric(us_census.Women)

print(us_census.Men, us_census.Women)
print(us_census.dtypes)
us_census = us_census.drop(columns=['GenderPop'])
#men is int, women float(decimal point)


# fill missings by an estimate of totalpop - men

us_census['Women'] =  us_census.fillna(value = {'Women': us_census.TotalPop - us_census.Men})

print(us_census['Women'])

#scatterplot
plt.scatter(us_census.Women, us_census.Income) 
plt.show()



# #check for duplicates
# duplicates = us_census.duplicated(subset=['State'])
# print(duplicates.value_counts())
# us_census = us_census.drop_duplicates()

# #scatterplot
# plt.scatter(us_census.Women, us_census.Income) 
# plt.show()
