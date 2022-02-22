'''
The Objective is to make a program that can convert miles to yards, feet and inches.
Created on Feb 21, 2022

@author: Sylvia Meza
'''

#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.
miles = int(input("How many miles would you like to convert?"))
#Convert miles to yards, using the following:
# 1 mile = 1760 yards.
yards = miles * 1760
#Store the value in a variable called yards and print it out with a 
#simple statement.
print(str(miles) + "miles converts to" + str(yards) + "yards.")
#Convert miles to feet, using the following:
# 1 mile = 5280 feet.
feet = miles * 5280
#Store the value in a variable called feet and print it out with a 
#simple statement.
print(str(miles) + " miles converts to " + str(feet) + " feet. ")
#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.
inches = miles * 63,360
#Store the value in a variable called inches and print it out with a 
#simple statement.
print(str(miles) + "miles converts to " + str(inches) + "inches.")