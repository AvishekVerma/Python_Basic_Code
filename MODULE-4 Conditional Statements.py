# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:48:20 2021

@author: Avishek
"""

#------------------------MODULE-4 Conditional Statements---------------------#

#Name:- Avishek Kymar Verma
#Batch:- 05012021_10A.M


#----------------------------Problem 1---------------------------------------#

#Problem 1 Take a variable ‘age’ which is of positive value and check the following:
#a. If age is less than 10, print “Children”.
#b. If age is more than 60 , print ‘senior citizens’
#c. If it is in between 10 and 60, print ‘normal citizen’
 
age = 22                         

if age<10:                              
    print("Children")
elif age >60:
    print("Senior Citizen")
elif age >10 and age < 60:
    print("Normal Citizen")
 
age = 8             #Output: Children
age = 22            #Output: Normal Citizen
age = 76            #Output: Senior Citizen


#----------------------------Problem 2---------------------------------------#


#Problem 2 Find  the final train ticket price with the following conditions. 
#a. If male and sr.citizen, 70% of fare is applicable
#b. If female and sr.citizen, 50% of fare is applicable.
#c. If female and normal citizen, 70% of fare is applicable
#d. If male and normal citizen, 100% of fare is applicable
#[Hint: First check for the gender, then calculate the fare based on age factor.
#For both Male and Female ,consider them as sr.citizens if their age >=60]

gender = str(input("Male or Female:- "))

while gender == "male":
    age = int(input("Your age :- "))
    if age >= 60:
        print("Only 70% of fare is applicable")
    else:
        print("100% of fare is applicable")
else:
    age = int(input("Your age:- "))
    if age >= 60:
        print("Only 50% of fare is applicable")
    else:
        print("Only 70% of fare is applicable")



#----------------------------Problem 3---------------------------------------#


#Problem 3 Check whether the given number is positive and divisible by 5 or not.  
  
num = int(input("Enter your no:- "))

if num >0:
    if num%5==0: 
        print('Entered number is Positive and Divisible of 5')
    else:
        print("Entered number is positive but not divisible of 5")
else:
    if num%5==0:
        print("Entered number is Negative and Divisible of 5")
    else:
        print("Entered number is Negative and not divisible of 5")
   
