################################
# 1. Import Libralies and load dataset
################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = ".\Module_3\Week_1\Data\IMDB-Movie-Data.csv" # put the correct path in here

# Read data form csv.file
data = pd.read_csv(DATA_PATH)

data_indexed = pd.read_csv(DATA_PATH, index_col = 'Title')


print(data_indexed)
################################
# 2. View the data
################################

# Preview top 5 rows using head()
print(data.head())


################################
# 3. Understand basic information of data
################################

print(data.info())
print(data.describe())


################################
# 4. Data Selection- Indexing and slicing data
################################

# Extract data as series
genre = data['Genre']
print(genre)
print(data[['Genre']])

# Select and split multiple columns at once, thus creating a new DataFrame
some_cols = data[['Title', 'Genre', 'Actors', 'Director', 'Rating']]
print(f"New DataFrame :\n{some_cols}")

# Slicing from row 10 and row 15
print(f"Slicing :\n {data.iloc[10:15][['Title', 'Rating', 'Revenue (Millions)']]}")


################################
# 5. Data Selection – Based on Conditional filtering
################################

# Take film form 2010 to 2020, with rating < 0.6, revenue top 5%
print("Select data based on conditions \n")
print(data[((data['Year'] >= 2010) & (data['Year'] <= 2015))
        & (data['Rating'] < 6.0)
        & (data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))])


################################
# 6. Groupby Operations
################################

# Find the average rating achieved by directors by grouping the Ratings of movies by Director.
print("Data after group by Rating and Director")
print(data.groupby('Director')[['Rating']].mean().head())


################################
# 7. Sorting Operations
################################

# Sorting value by Rating in ascending/descending order 
print("Sorting top 5 Directors")
print(data.groupby('Director')[['Rating']].mean().sort_values(['Rating'], ascending = False).head())


################################
# 8. View missing values
################################

# To check null values row wise
print("Check NULL")
print(data.isnull().sum())


################################
# 9. Deal with missing values - Deleting
################################

# Use drop function to drop columns
print(data.drop('Metascore', axis = 1).head())
print("New DataFrame")
print(drop_columns.head())

# Drop null rows
drop_rows = data.dropna()
print("New DataFrame")
print(f"{drop_rows.head()}")


################################
# 10. Dealing with missing values - Filling
################################

# Some rows have Revenue with null value, we can assign it average value
revenue_mean = data_indexed['Revenue (Millions)'].mean()
print('The mean revenue is: ', revenue_mean)

# we can fill the null values with this mean revenue
data_indexed['Revenue (Millions)'].fillna(revenue_mean, inplace = True)


################################
# 11. apply() functions:
################################

# Classify movies based on ratings
def rating_group(rating):
    if rating >= 7.5:
        return "Good"
    elif rating >= 6.0:
        return "Average"
    else:
        return "Bad"

# Lets apply this functions on our movies data
# creating a new variable in the dataset to hold the rating category
data['Rating_category'] = data['Rating'].apply(rating_group)

print(f"New DataFrame :\n {data[['Title', 'Director', 'Rating', 'Rating_category']].head(5)}")



