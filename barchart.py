# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:52:54 2023

@author: Jay

This Code plot a bar chart of the Average daily hours spent engaging with digital media (e.g., images and videos, web pages, social media apps, etc.) 
The data for 'other connected devices' includes game consoles. Mobile includes smartphones & tablets.
All data includes usage at home and work for people 18+.
The Data has been taken from the website https://ourworldindata.org/grapher/daily-hours-spent-with-digital-media-per-adult-user


"""
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the provided data
social_media_data = pd.read_csv('D:/MSC Data Science/ADS/Practical/Assignment1/daily-hours-spent-with-digital-media-per-adult-user.csv')

social_media_data.set_index('Year', inplace=True)

# Plot bar plots for each category
plt.figure(figsize=(10, 6))
social_media_data.plot(kind='bar', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Hours')
plt.title('Social Media Users in the United States (2008-2018)')
plt.legend(title='Category')
# Set the y-axis range from 0.3 to 4
plt.ylim(0, 4) 
# Show the plot
plt.show()
