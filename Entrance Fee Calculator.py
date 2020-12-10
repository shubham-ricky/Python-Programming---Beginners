"""
a)	The entrance fee of the SuperPark Singapore is based on the age and membership of the person. See table below: 

Age\Membership	Member	Public
>12	         35	  48
<=12	         30	  42

Write a function named calcPrice() that takes in membership and age parameters to determine and return the price that a person has to pay for an entry. 

b)	Write the code to do the following: 
•	Calculate the total cost for a group of tourists using the calcPrice() function that you have defined in Q2(a). 
•	Display the total cost for the entrance fees for this group

Name	Membership	Age
Emma	      Yes	21
Jim	      No	18
Meg	      No	9
Cleo	      No	11

"""

def calcPrice(membership, age):                         #....Part a)
    if membership == "Yes":
        if age>12:
            return 35
        else:
            return 30
    elif membership == "No":
        if age>12:
            return 48
        else:
            return 42

total_cost = 0

for i in range(4):
    
    name = input("Please enter your name : ")

    age = int(input("Please enter your age : "))

    membership = input("Are you member (Yes/No): ")
    
    total_cost = total_cost + calcPrice(membership,age)      #...Part b)
    
print("The total cost for the entrance fee is: ", total_cost)
    


        