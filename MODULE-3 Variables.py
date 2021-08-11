# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:23:27 2021

@author: Avishek
"""

#------------------------MODULE 3 Variables---------------------------------#


#Name :- AVISHEK KUMAR VERMA
#Batch :- 05012021_10A.M


#------------------------Problem 1 ------------------------------------------#


#Problem 1 What will be the output of the following (can/cannot):
#   Age1=5
#B  5age=55

Age = 5
Age             #Out[48]: 5

 5age=55        #SyntaxError: invalid syntax

#As we know in python while assigning any variables we can use Alphanumeric values
#but we can not initiate a variable name with Numbers.
#that's why, In above case its showing Syntax Error 


#------------------------Problem 2 ------------------------------------------#

#Problem 2  What will be the output of following (can/cannot):
#a.  Age_1=100
#b.  age@1=100

Age_1=100
Age_1           #Out[51]: 100

age@1=100       #SyntaxError: cannot assign to operator
#As we know in Python we can not use special Character while assigning  variables
#except "_" and "."
#This is the reason in above case its showing Syntax error


#------------------------Problem 3 ------------------------------------------#

#Problem 3 How can you delete variables in Python ?

var = [11,2,3,4,5,6]     #declearing a variable

del(var)                #deleting variable using del() function
var                     #Check for var in output   
        #Output: NameError: name 'var' is not defined




