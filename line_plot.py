# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:32:36 2023

@author: Jay

This Code Draw a line plot of the number of internet user across 
4 countries Afghanistan, Australia, Canada and Spain during 1990 to 2020.

The Data has been taken from the website https://ourworldindata.org/grapher/number-of-internet-users
Due to the large size of the data, a subset containing information for 9 countries over 4 years has been saved to a file ('Access_to_Electricity').
This file is hosted on my GitHub repository, and to run this code, you can access it from the following link:
https://github.com/JawadDS/ADS_Assignments/blob/main/line_plot.py
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
data_file_path = "InternetUsers_data.csv"
countries_data = read_data(data_file_path)

# Extract relevant columns for the line plot
years =  countries_data['Year']  
afghanistan =  countries_data['AFG']  
australia =  countries_data['AUS']  
canada =  countries_data['CAN'] 
spain =  countries_data['ESP'] 

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(years, afghanistan, label = 'Afghanistan')
plt.plot(years, australia, label = 'Australia')
plt.plot(years, canada, label = 'Canada')
plt.plot(years, spain, label = 'Spain')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of People')
plt.yticks([0, 10000000, 20000000, 30000000, 40000000], ['0 million', '10 million', '20 million', '30 million', '40 million'])
plt.title('Evolution of Internet users')

# Add a legend
plt.legend()

# Display the plot
plt.show()
