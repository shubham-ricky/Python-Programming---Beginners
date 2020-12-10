"""
a)	Write a function larger_num() that takes in two number parameters to determine and return the larger number of the two.
b)	Write a program to do the followings: 
•	Ask user for two numbers
•	Use the function in Q1(a) to determine the larger number and display the result.
"""

def larger_num(number1, number2):
    if number1 > number2:
        return number1
    elif number1 < number2:
        return number2
    else:
        print("Both numbers are equal")
        return('')
        
a=int(input("Enter the first number:- "))
      
b=int(input("Enter the second number:- "))
      
print(larger_num(a,b))