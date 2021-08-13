# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 15:48:44 2021

@author:Avishek
"""

#------------------------MODULE 5 LOOPS and Functions---------------------#

#Name:- Avishek Kymar Verma
#Batch:- 05012021_10A.M


#----------------------------Problem 1---------------------------------------#


#Problem 1
            #A) list1=[1,5.5,(10+20j),’data science’].
            # Print default functions and parameters exists in list1.
            #B) How do we create a sequence of numbers in Python.
            #C)  Read the input from keyboard and print a sequence of numbers up to that number
#A.
list1 = [1,5.5,(10+20j),'data science']

for i in list1:
    print(i)
    
#B.
[x for x in range(1,29,3)]      #creating sequence 

#C.
num = int(input("Enter a number:- ")) #taking input from keyboard

[x for x in range(1,1+num)]             #printing sequence up to entered number


#---------------------------- Problem2---------------------------------------#

#Problem2  Create 2 lists. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
#list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
#Create a dictionary such that list2 are keys and list 1 are values..

list1 =[x for x in range(1,10)]
list1
list2 = ['zero','one','two','three','four','five','six','seven','eight','nine']
list2

dic = {"one":1,"two":2,"three":3,"four" :4,"five":5,"six":6, "saven":7, "eight":8,"nine":9,"ten":10}
dic.keys()


#----------------------------Problem 3---------------------------------------#

#Problem 3 Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10
#          to the even number and multiply with 5 if it is odd number in the list1..


list1 = [3,4,5,6,7,8]

for i in list1:
    if i%2==0:
        print(i+10)
    else:
        print(i*5)


#----------------------------Problem 4---------------------------------------#

#Problem 4  Write a simple user defined function that greets a person in such a way that :
            #i) It should accept both name of person and message you want to deliver.
            #ii) If no message is provided, it should greet a default message ‘How are you’
            #Ex: Hello ---xxxx---, How are you  -🡪 default message.
            #Ex: Hello ---xxxx---, --xx your message xx---


def greet(name,b= 'how are you'): #Defining function
    print(name,b)
    
greet('Avishek')            #Calling defined function
    

