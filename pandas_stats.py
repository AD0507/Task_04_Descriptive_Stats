#!/usr/bin/env python
# coding: utf-8


import pandas as pd

# Load the uploaded CSV file with pandas
import sys
DATA_PATH = '2024_tw_posts_president_scored_anon.csv'
if len(sys.argv) > 1:
    DATA_PATH = sys.argv[1]
df = pd.read_csv(DATA_PATH)

# Basic dataset overview
shape = df.shape
print(shape)



columns = df.columns.tolist()
print(columns)



# Descriptive stats for numeric columns
numeric_summary = df.describe()
print(numeric_summary)



# Unique counts for each column
nunique = df.nunique()
print(nunique)



# Most frequent values for non-numeric columns
top_values = {col: df[col].value_counts().head(1).to_dict() for col in df.select_dtypes(include='object').columns}
print(top_values)



import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Select top numeric columns for histograms and boxplots
top_numeric = ['retweetCount', 'replyCount', 'likeCount', 'viewCount']

# Histogram
for col in top_numeric:
    plt.figure(figsize=(10, 4))
    sns.histplot(df[col], bins=50, kde=True)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()



# Boxplots
for col in top_numeric:
    plt.figure(figsize=(10, 2))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()




# Categorical count: source
plt.figure(figsize=(12, 5))
sns.countplot(data=df, y='source', order=df['source'].value_counts().index)
plt.title("Distribution of Tweet Sources")
plt.xlabel("Count")
plt.ylabel("Source")
plt.tight_layout()
plt.show()



# In[19]:


# Categorical count: month_year
plt.figure(figsize=(12, 5))
sns.countplot(data=df, x='month_year', order=sorted(df['month_year'].dropna().unique()))
plt.title("Tweet Count by Month")
plt.xlabel("Month-Year")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

