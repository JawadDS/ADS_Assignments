# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:32:36 2023

@author: Jay

This Code Draw a line plot of the number of internet user accross 
4 countries Afghanistan, Australia, Canada and Spain during 1990 to 2020.

The Data has been taken from the website https://ourworldindata.org/grapher/number-of-internet-users

"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas DataFrame from your CSV file
countries_data = pd.read_csv("D:/MSC Data Science/ADS/Practical/Assignment1/InternetUsers_data.csv")

# Extract relevant columns for line plot
years =  countries_data['Year']  
afghanistan =  countries_data['AFG']  
australia =  countries_data['AUS']  
canada =  countries_data['CAN'] 
spain =  countries_data['ESP'] 

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(years, afghanistan, label='Afghanistan')
plt.plot(years, australia, label='Australia')
plt.plot(years, canada, label='Canada')
plt.plot(years, spain, label='Spain')


# Add labels and title
plt.xlabel('Year')
plt.ylabel('Number of People')
plt.yticks([0, 10000000, 20000000, 30000000, 40000000], ['0 million', '10 million', '20 million', '30 million', '40 million'])
plt.title('Numnber of Internet users')

# Add a legend
plt.legend()

# Display the plot
plt.show()
