'''
This outline will help solidify concepts from the Conditionals lesson.
Fill in this outline as the instructor goes through the lesson.
'''
from _ast import If
from builtins import True

#1) Make a int variable named a. Now make an if statement, and if a is more than
#5, print out "a is more than 5."
 = if
 a = 9
 if a>5:
     print("a is more than 5")


#2) Make a boolean variable named b. Now make an if statement, and if b is True
#print out "b is True."
= if
b = "I like dogs"
x = True
if x:
    print("b is True")

#3) Make an int variable named c. Now make an if/elif statement, and if c is 
#more than 0, print "c is positive". Else if c is less than 0, print "c is
#negative".
= if, else

c = -1
if c > 0:
    print("c is positive")
    
else:
    print("c is negative")


#4) Make an int variable named d. Now make an if/elif/else statement, and if 
#d is more than 0, print "d is positive". Else if d is less than 0, print "c is
#negative". Else, print "d is zero".
= if, else

d = 5
if d > 0:
    print("d is positive")
    
elif d == 0:
    print("d is zero")
    
 else:
     print("d is negative")   

#5) Make an if statement with any comparison, with a common SYNTAX error.
= if
s = 7
if s > 3
print("more than 3")

