# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:09:00 2023

@author: Jay


This Code Draw a pie chart plot of the share of the global population affiliated with major 
religious groups in 2022, by religion.

The Data has been taken from the website https://www.statista.com/statistics/374704/share-of-global-population-by-religion/
Due to the large size of the data, a subset containing information for 9 countries over 4 years has been saved to a file ('Access_to_Electricity').
This file is hosted on my GitHub repository, and to run this code, you can access it from the following link:
https://github.com/JawadDS/ADS_Assignments/raw/main/world_religions.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    """
    Read data from a CSV file and return a DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: A DataFrame containing the read data.
    """
    data = pd.read_csv(file_path)
    return data

# Use the function to read the data
data_path = 'world_religions.csv'
religions_data = read_data(data_path)

# Define figure size
plt.figure(figsize = (11, 11))

# Plot the pie chart
plt.pie(religions_data['Percentage'], labels = religions_data['Religion'])

# Add title
plt.title("Global population affiliated with major religious groups in 2022")

# Add legends to the plot
plt.legend(religions_data['Religion'])

# Show the plot
plt.show()
