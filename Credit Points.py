"""
The health promotion board has engaged smokers by persuading them to quit smoking.  Participants who are taking part in a series of activities will be awarded credit points. These credit points accumulated can be used to exchange for discount vouchers in the shopping centres.

The allocation of credit points for each activity to quit smoking is as follows:


Period of Activity (minutes)	Points
>= 180	                         5
>= 120 and < 180	                 3
>= 60 and < 120	                 2
>= 30 and < 60	                 1
< 30	                         0

a) From the table provided above, write a function called getCredits that takes in one parameter duration as the time of the activity. The function returns the credit points to be awarded based on the duration (in minutes). The program shall return zero if less than 30 minutes of the activity are logged. The program shall also return zero if negative time is entered. 

b) Write a Python program according to the requirements in Q7. Note that your program must call the function getCredits you produced in Q7(a). 

"""


def getCredits(duration):
    if duration >= 180:
        return 5
    elif duration >= 120 and duration < 180:
        return 3
    elif duration >= 60 and duration < 120:
        return 2
    elif duration >=30 and duration<60:
        return 1
    else:
        return 0
    
num=int(input("Enter the number of activities you have attended: "))
tot_duration = 0
for i in range(1,(num+1),1):
    d=int(input("What is the duration for Activity (mins)"+str(i)+": "))
    act_dur = getCredits(d)
    print("Credit points awarded for Activity " +str(i)+ " is: ", act_dur)
    tot_duration = tot_duration + act_dur
    
print("Total credit points obtained is ", tot_duration)


    
