"""
A name is in the format of

<first name> <last name> 
For example, a valid name would be something like Jamie Oliver. 

Lucky Number = (F + 7*L) % R + F 
where F = Length of first name 
L = Length of last name 
R = random number between 1 to 100

a)	Write a function calcLuckyNum that takes name as a parameter to calculate and return the lucky number using the formula given. E.g. calcLuckyNum("Jamie Oliver") will return the lucky number for Jamie Oliver.

b)	Write a program to request a name from the user, call the function calcLuckyNum and print the lucky number you have computed.

"""

import random

def calcLuckyNum(name):
    nameList=name.split()
    firstname=nameList[0]
    lastname=nameList[1]
    
    F=len(firstname)
    L=len(lastname)
    R=random.randint(1,100)
    
    LuckyNum=(F+7*L)%R + F
    
    return LuckyNum

name=input("Enter your full name(First Name and Last Name):- ")

print("Your lucky number is:-", calcLuckyNum(name))