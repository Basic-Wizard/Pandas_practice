#!/usr/bin/env python


# Import pandas
import pandas as pd

# Read data from a CSV file
df = pd.read_csv('dnd_stats.csv')

# Display the first 5 rows of the DataFrame
df.head()