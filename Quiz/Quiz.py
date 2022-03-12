'''
Created on Mar 11, 2022
@author: Sylvia Meza
Objective: Quiz users on basic high school trivia with 4 simple questions.
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.
score = 0
#Ask the user question one. And store the users answer.
x = input("What is the powerhouse of the cell? A mitochondria, B nucleus or C ribosome")
Answer = "A"
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if(x.upper() == "A":
   score = 1
   print("Correct")
 else:
     print("Incorrect, the correct answer is A")  
#Ask the user question two. And store the users answer.
x = input("How many states comprise the United States? A 13, B 45, or C 50")
Answer = "C"
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if(x.upper() == "C":
  score =2
   print("Correct")
else:
    print("Incorrect, the correct answer is C")
#Ask the user question three. And store the users answer.
x = input("In y=mx+b, what does m stand for? A slope, B output or C I don't understand math")
Answer = "A"
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if(x.upper() == "A":
   score = 3
   print("Correct")
else:
    print("Incorrect, the correct answer is A")
#Ask the user question four. And store the users answer.
x = input("In English, a person, place or thing is called: A verb, B adjective or C noun")
Answer = "C"
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if(x.upper() == "C":
   score = 4
   print("Correct")
else:
    print("Incorrect, the correct answer is C")
#Calculate the percentage the user got. And store it in a variable called p
p =  [score]/4 * 100
#Print out the users score: "You got a [score]/4. Or a [p]%."
print("You got a [p]%")