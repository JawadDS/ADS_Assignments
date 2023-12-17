# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:52:54 2023

@author: Jay

This Code plot a bar chart of the Average daily hours spent engaging with digital media (e.g., images and videos, web pages, social media apps, etc.) 
The data for 'other connected devices' includes game consoles. Mobile includes smartphones & tablets.
All data includes usage at home and work for people 18+.
The Data has been taken from the website https://ourworldindata.org/grapher/daily-hours-spent-with-digital-media-per-adult-user
Due to the large size of the data, a subset containing information for 9 countries over 4 years has been saved to a file ('Access_to_Electricity').
This file is hosted on my GitHub repository, and to run this code, you can access it from the following link:
https://github.com/JawadDS/ADS_Assignments/blob/main/barchart.py


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
data_file_path = 'digital_media_data.csv'
social_media_data = read_data(data_file_path)

# Set the index to 'Year'
social_media_data.set_index('Year', inplace=True)

# Plot bar plots for each category
plt.figure()
social_media_data.plot(kind='bar', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Hours')
plt.title('Social Media Users in the United States (2008-2018)')
plt.legend(title='Category')
# Set the y-axis range from 0.3 to 4
plt.ylim(0, 4) 
# Show the plot
plt.show()
