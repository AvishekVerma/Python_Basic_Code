# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:37:39 2021

@author: Avishek
"""

#------------------------MODULE 6 PACKAGES-------------------------#

#Name:- Avishek Kymar Verma
#Batch:- 05012021_10A.M


#----------------------------Problem 1---------------------------------------#


#Problem 1 
#For the dataset “Indian_cities”, 
#a. Find out top 10 states in female-male sex ratio
#b. Find out top 10 cities in total number of graduates
#c. Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

import pandas as pd
cities = pd.read_csv("C:\\Users\\admin\\Desktop\\D.S-360\\1.Python\\Python Assignment\\Indian_cities.csv")
type(cities)
cities

#a.    #sorting sex_ratio column 
sex_ratio_values = cities.sort_values(by="sex_ratio",ascending = False).sex_ratio
sex_ratio_values[0:10] 
sex_ratio = cities.sort_values(by="sex_ratio",ascending = False).name_of_city
sex_ratio[0:10]

#b.
graduates_value = cities.sort_values(by="total_graduates",ascending = False).total_graduates
graduates_value[0:10]
graduates_top_cities = cities.sort_values(by = "total_graduates",ascending = False).name_of_city
graduates_top_cities[0:10]

literracy_value = cities.sort_values(by="effective_literacy_rate_total",ascending = False).effective_literacy_rate_total
literracy_value[0:10]
literracy_cities = cities.sort_values(by="effective_literacy_rate_total",ascending = False).name_of_city
literracy_cities[0:10]
literracy_location = cities.sort_values(by="effective_literacy_rate_total",ascending = False).location
literracy_location[0:10]



#----------------------------Problem 2---------------------------------------#

#Problem 2 For the data set “Indian_cities”
#a. Construct histogram on literates_total and comment about the inferences
#b. Construct scatter  plot between  male graduates and female graduates

import matplotlib.pyplot as plt
#a. Histogram
plt.hist(cities['literates_total'])
#histogram is positively scwed i.e mean>median>mode
#there is also persence of Outliers
#b. Scatter plot

plt.scatter(cities['male_graduates'],cities['female_graduates'])


#----------------------------Problem 3---------------------------------------#

#Problem 3 For the data set “Indian_cities”
#a. Construct Boxplot on total effective literacy rate and draw inferences
#b. Find out the number of null values in each column of the dataset and delete them.

#a. Boxplot
plt.boxplot(cities['effective_literacy_rate_total'])
#distribution is little negetively scwed, and there is also persence of outliers.

#b. null values

cities.isna()
cities.dropna()











