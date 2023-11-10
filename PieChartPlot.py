# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:09:00 2023

@author: Jay


This Code Draw a pie chart plot of the share of global population affiliated with major 
religious groups in 2022, by religion.

The Data has been taken from the website https://www.statista.com/statistics/374704/share-of-global-population-by-religion/
"""
import pandas as pd
import matplotlib.pyplot as plt

#extract data from file named world_religions 
religions_data = pd.read_csv('https://github.com/JawadDS/ADS_Assignments/blob/main/world_religions.csv')

#define figure size
plt.figure(figsize=(11, 11))
#plot the pie chart
plt.pie(religions_data['Percentage'], labels=(religions_data["Percentage"]))
#add title
plt.title("Global population affiliated with major religious groups in 2022")
#add legends to the plot
plt.legend(religions_data['Religion'])
plt.show()