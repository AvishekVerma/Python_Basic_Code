# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:31:07 2021

@author: Avishek
"""

#-----------------------MODULE-2 OPERATORES----------------------------------#


#Name :- AVISHEK KUMAR VERMA
#Batch :- 05012021_10A.M


#------------------------Problem 1 ------------------------------------------#

#Problem 1 
#A. Write an equation which relates 399, 543 and 12345 
#B. “When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2
# —How would you justify it.

#assigning values to variables
a = 399
b = 543
c = 12345
#constructing an equation to relates all three
c > a + b    

a = 5
b = 3
c = -5

d = 5 // 3
d          #Out[25]: 1
e = -5 //3
e          #Out[27]: -2
#when we take floor division of negative number it returns Quotient as one higher digit


#------------------------Problem 2 ------------------------------------------#


#Problem 2.  a=5,b=3,c=10.. What will be the output of the following:
#            A. a/=b
#            B. c*=5  
a=5
b=3
c=10
# a/=b means a = a/b
# c = c*5
d = 5/3
d       #Out[36]: 1.6666666666666667
e = c*5
e       #Out[38]: 50


#------------------------Problem 3 ------------------------------------------#


#Problem 3. A. How to check the presence of an alphabet ‘s’ in word “Data Science” .
#           B. How can you obtain 64 by using numbers 4 and 3 .

#A. we can check alphabet 's' in word "Data Science" using Membership operator
#If output is True then alphabet is present in string; 
#if output is False then alphabet is not present in that string

's' in 'Data Science'       #Out[42]: False
#'s' is not present in "Data Science"
#Python is case sensiive so 's' is not equal to 'S'

#B. we can obtain 64 using 4 and 3 by expoonential operator 
exp = 4**3
print(exp)          #Output 64



