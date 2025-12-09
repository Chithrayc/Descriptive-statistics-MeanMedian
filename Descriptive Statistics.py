import pandas as pd #useful for loading dataset

#load dataset
dataset=pd.read_csv('C:\\Users\\User\\Desktop\\DA 30Days\\dataset\\statistics(d6)dataset.csv')     #read the dataset
datasetwithNaN=dataset
print("DATASET :",dataset)

#load summarize
print("Count:",dataset.shape)
print("MMM:",dataset.describe())

#checking for NaN values
dataset.isna().any() #checks if any column in null values

#filing NaN values with the mean
#problem-new value becomes high coz of outliers(large value scale)

Mean=dataset.price.fillna(dataset.price.mean())
print("Mean", Mean)

#solution-filling NaN value with Median
Median=dataset.price.fillna(dataset.price.median())
print("Median", Median)

#identifying and removing the outlier - huge difference in value
dataset.describe()

percentile=dataset.price.quantile(1.0) #100%
print("PERCENTILE :", percentile)

datasetNoOutlier =dataset[dataset.price < percentile]
print("DNO ", datasetNoOutlier)





















