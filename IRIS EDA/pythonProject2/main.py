import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")


#functions used

df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()

data = df.drop_duplicates(subset="Species",)
data

df.value_counts("Species")

#Finaloutputvalues


print(df.head)
print(df.shape)
print(df.info)
print(df.describe)
print(df.isnull().sum())
print(data)
print(df.value_counts("Species"))


# Visualize key statistics and distributions to gain insights into the dataset.

sns.countplot(x='Species', data=df)
plt.show()

#scatter plot comparing sepal length and width

sns.scatterplot(x='SepalLengthCm', y='SepalWidthCm',hue='Species', data=df, )

plt.legend(bbox_to_anchor=(1,1), loc=2)

plt.show()

#multivariate analysis all coloumn realationship

sns.pairplot(df.drop(['Id'], axis = 1),hue='Species', height=2)
plt.show()

#histograms

fig, axes = plt.subplots(2,2, figsize=(10,10))
axes[0,0].set_title("Sepal Length")
axes[0,0].hist(df['SepalWidthCm'],bins=7);

axes[0, 1].set_title("Sepal Width")
axes[0, 1].hist(df['SepalWidthCm'], bins=5);

axes[1, 0].set_title("Petal Length")
axes[1, 0].hist(df['PetalLengthCm'], bins=6);

axes[1, 1].set_title("Petal Width")
axes[1, 1].hist(df['PetalWidthCm'], bins=6);

plt.show()


