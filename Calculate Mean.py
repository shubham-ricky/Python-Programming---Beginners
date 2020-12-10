"""
a)	Write a function calcMean that take in a list with 18 random numbers that are between 1 to 999 as parameter, and return the mean using a For-loop. 

b)	Generate a list of 18 random integers that are between 1 to 999. Print the outcome of the function written in Q5(a).  

"""

import random

def calcMean(NumList):
    sum = 0
    
    for i in range(0,18,1):
        sum = sum + NumList[i]
        
    mean = sum/18
    return mean
    
RanList = []

for k in range(0,18,1):
    n=random.randint(1,999)
    RanList.append(n)
   
print("List of Random Intergers:- " +str(RanList))

print("Mean of the random intergers is:- " +str(calcMean(RanList)))



        
        
