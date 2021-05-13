# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

sns.boxplot(heart.thalach, heart.heart_disease)
plt.show()

#thalach: maximum heart rate achieved in exercise test

thalach_hd = heart.thalach[heart.heart_disease == 'presence']
thalach_no_hd = heart.thalach[heart.heart_disease == 'absence']

mean_diff = np.mean(thalach_hd) - np.mean(thalach_no_hd)
print(mean_diff)

median_diff = np.median(thalach_hd) - np.median(thalach_no_hd)
print(median_diff)

from scipy.stats import ttest_ind

t, pval = ttest_ind(thalach_hd, thalach_no_hd)
print(pval)

plt.clf()
sns.boxplot(heart.thalach, heart.cp)
plt.show()

#ANOVA 

thalach_typical = heart.thalach[heart.cp == 'typical angina']
thalach_asymptom = heart.thalach[heart.cp == 'asymptomatic']
thalach_nonangin = heart.thalach[heart.cp == 'non-anginal pain']
thalach_atypical = heart.thalach[heart.cp == 'atypical angina']

from scipy.stats import f_oneway

f, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print(pval)

from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey_results = pairwise_tukeyhsd(endog = heart.thalach, groups = heart.cp)
print(tukey_results)

#Heart Disease and Chest Pain

Xtab = pd.crosstab(heart.cp, heart.heart_disease)
print(Xtab)

from scipy.stats import chi2_contingency

chi2, pval, dof, exp = chi2_contingency(Xtab)
print(pval)
