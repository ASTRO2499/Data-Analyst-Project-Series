#packages

import pandas as pd
import seaborn as sns
import matplotlib as plt
import RandomUnderSampler,RandomOverSampler

#clean and preproccess
#EDA
df = pd.read_csv("weather.csv")


A=df.head()
B=df.info()
C=df.isnull().sum()
D=df.duplicated().sum()
E=df.describe([x*0.1 for x in range (10)])
print(A,B,C,D,E);

#MISSING DATAS

df['Sunshine'].fillna(df['Sunshine'].mean())
df['Sunshine'].fillna(df['Sunshine'].median())

df['WindSpeed9am'].fillna(df['WindSpeed9am'].mean())
df['WindSpeed9am'].fillna(df['WindSpeed9am'].median())

#Duplicates &Outliers

df = df.drop_duplicates()

#outliers
df = df[df.MinTemp<=0]

#inconsistencies

# undersampling
from imblearn.over_sampling
undersample = RandomUnderSampler(sampling_strategy='majority')
X_train, y_train = undersample.fit_resample(df_train.drop(['y'],axis=1),df_train['y'])
# oversampling
oversample = RandomOverSampler(sampling_strategy='minority')
X_train, y_train = oversample.fit_resample(df_train.drop(['y'],axis=1),df_train['y'])





