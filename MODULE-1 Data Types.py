# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:58:17 2021

@author: Avishek
"""

#-----------------------ASSIGNMENT-1 Data Types------------------------------#


#Name :- AVISHEK KUMAR VERMA
#Batch :- 05012021_10A.M


#----------------------Problem 1---------------------------------------------#

#problem - 1. Construct 2 lists containing all the available data types 
#(integer, float, string, complex and Boolean) and do the following..
#a.	Create another list by concatenating above 2 lists
#b.	Find the frequency of each element in the concatenated list.
#c.	Print the list in reverse order.

list1 = [ 27.4, 14, 'Avishek', True, 8+9j]   #Creating first list
list2 = [False,35,27.4,'Data Science',8+9j]   #Creating second list

l3 = list1+list2        #creating new list concatination of list1 and list2
print(l3)               #printing new list

#using count function to get frequency of each element

l3.count(27.4)          
l3.count(14)
l3.count('Avishek')
l3.count( True)
l3.count(8+9j)
l3.count(False)
l3.count('Data Science')
l3.count(35)

#list l3 is combination of str and complex so, no sorting

list3 = [7,98,45,23,80,54,7,3,13]       #Defining new list
list3.sort(reverse =True)       #sorting list using sort function
print(list3)                    #printing list3 after sorting


#----------------------Problem 2---------------------------------------------#

#Problem 2 2.	Create 2 Sets containing integers (numbers from 1 to 10 in one 
# set and 5 to 15 in other set)
#a.	Find the common elements in above 2 Sets.
#b.	Find the elements that are not common.
#c.	Remove element 7 from both the Sets.

set1 = {1,2,3,4,5,6,7,8,9,10}               #crating first set
set1
set2 = {5,6,7,8,9,10,11,12,13,14,15}        #creating second set
set2

comm = set1.intersection(set2)     #using intersection function to get common elements
comm

not_comm1 = set1-comm       #finding not common elements
not_comm1
not_comm2 = set2-comm
not_comm2

#removing 7 from both sets

not_7 = set1 - {7}
not_7
not7 = set2 - {7}
not7



#----------------------Problem 3---------------------------------------------#

#Problem -3. Create a data dictionary of 5 states having state name as key and
# number of covid-19 cases as values.
#a.	Print only state names from the dictionary.
#b.	Update another country and it’s covid-19 cases in the dictionary.

#creating a dictionary
dic = {"Andhra Pradesh":888350,"Bihar":260095,"Delhi":635916,"Karnataka":942031,"Maharashtra":2041398}

dic.keys()          #printng only state names using key function

dic["United"] = 27519636   #adding new data to dictionary
dic
