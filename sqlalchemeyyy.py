import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Replace the following with your database connection details
username = 'root'  # Your MySQL username
password = 'varshitha'  # Your MySQL password
host = 'localhost'  # Your MySQL host, e.g., 'localhost' or an IP address
database = 'test'  # Your MySQL database name

# Create a connection string using SQLAlchemy
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'

# Create an engine
engine = create_engine(connection_string)

# Read data from MySQL into a pandas DataFrame
df_sql = pd.read_sql('SELECT * FROM product', engine)

# Display the DataFrame
print(df_sql)
print("dtypes:",df_sql.dtypes)
df=pd.read_csv("titanic.csv")
print("df_sql columns:", df_sql.columns)
print("df columns:", df.columns)
#to rename the passesngerId to get the common columns
df.rename(columns={'PassengerId': 'productId'}, inplace=True)

# Ensure both 'productId' columns have the same data type
df_sql['productId'] = df_sql['productId'].astype(int)
df['productId'] = df['productId'].astype(int)

# Merge the two DataFrames on 'productId' with an outer join
merged = pd.merge(df_sql, df, on='productId', how='outer')

# Display the merged DataFrame
print(merged)

#reading excel filee
exc=pd.read_excel("FSI-2023-DOWNLOAD.xlsx")
# print("excel columns are:",exc.columns)
print(exc.dtypes)
exc.rename(columns={'S1: Demographic Pressures': 'productId'}, inplace=True)
exc['productId'] = exc['productId'].astype(int)
merged = pd.merge(merged, exc, on='productId', how='outer')
print(merged)

print(df_sql.dtypes, '\n')
print('Before : Memory Usage for id (int64)\n', df_sql['productId'].memory_usage(deep=True), '\n')
df_sql['productId'] = df_sql['productId'].astype(np.int16)
print(df_sql.dtypes, '\n')
print('After : Memory for id (int16)\n', df_sql['productId'].memory_usage(deep=True), '\n')


print(df_sql.isnull().sum)