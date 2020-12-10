"""
Gravitational force can be measured by how every particle attracts every other particle in the universe with a force that is directly proportional to the product of their masses and inversely proportional to the square of the distance between their centres. 

The formula for the gravitational force is given as: 
 F = G(m1*m2)/r^2

where  
F is the gravitational force
G is the gravitational constant
m1 is the mass of the first object
m2 is the mass of the second object
r is the distance between the centres of their masses

Assuming the followings are entered:

G = 6.674×10-11 Nm2/kg2
m1 = 5.98 x 1024 kg
m2 = 70 kg 
r = 6.38 x 106 m

Here is a sample calculation for the gravitation force: 

F = (6.674e-11 * 5.98e24 * 70) / 6.38e6**2 = 686.35 N

Write a program that allows a user to enter the values for m1, m2 and r, which are float data types. Calculate and print the value of the gravitational force in kilonewton [kN]. Note that the program should run continuously until the ‘x’ key is entered. 

a) Draw the flowchart for the program requirements stated above 


b) Using the flowchart from Q8(a), write the Python program to print the result of the gravitation force computed using a While-Loop.

"""

def force_calc():
    m1 = float(input("Enter the mass of the first object, m1 (kg) = "))
    m2 = float(input("Enter the mass of the second object, m2 (kg) = "))
    r= float(input("Enter the radius between the centres of masses on both object, r (m) = ")) 
    
    G = 6.674*10**-11
    F= (G*m1*m2*0.001)/(r**2) 
    
    return F
    
print("This program is to calculate Force in kilonewton(kN), please provide below inputs: ")

user_input=force_calc()
print(str(user_input)+" kN")

while user_input != "X" or user_input != "x":
        
    user_input = input("If u wish to stop, Press X/x. To run program again, give any other input:- ")
    
    if user_input == "X" or user_input == "x":
        exit()
    else :
        user_input = force_calc()
        print(str(user_input)+" kN")



