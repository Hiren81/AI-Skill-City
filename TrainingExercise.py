# #Example practice -1
# #write a progrma in python that take inputs from user and determine if the given number is odd or even  
# #like 2,4,6,8 and 2,3,5,7 in python code make it very simple to understand line by line 

# # # Step 1: Ask the user to enter a number
# # number = int(input("Enter a number: "))  # Converts the user input to an integer

# # # Step 2: Check if the number is even
# # if number % 2 == 0:  # If the remainder when dividing by 2 is 0, the number is even
# #     print(f"The number {number} is even.")
# # else:
# #     # Step 3: If the above condition is false, the number is odd
# #     print(f"The number {number} is odd.")

# # Explanation:
# # input("Enter a number: ") - Prompts the user to enter a number.
# # int() - Converts the input string into an integer for mathematical operations.
# # number % 2 - Calculates the remainder when the number is divided by 2.
# # If the remainder is 0, the number is even.
# # Otherwise, the number is odd.
# # if and else - Use conditional statements to print the appropriate message based on the check.

# number= int(input("Enter number "))
# if number%2==0:
#     print("number is even")
# else:
#      print("number is odd")      

# #Example practice-2
# #A company decided to give bonus of 7% to employee if his/her year 
# # of serviceis more then 3years,ask user for their salary  and year of service and 
# # print the new bonus amount

# #write in psesudo code 

# # Ask user to enter their current salary any guess amount
# salary=input("enter current salary:")

# # Ask user to enter their years of service
# years_of_job=input("enter years of job:")

# # Convert input values to an int types
# salary=float(salary)
# years_of_job=int(years_of_job)

# # Check if the employee is eligible for a bonus
# #Print the bonus amount guess again 
# if years_of_job>3:
#      print("you bonus is +3000")

# if years_of_job>3:
#      print("you bonus is +3000" , salary)
# else:
#      print("years of service is less so no bonus ")



# #how amny input we need 2
# # what kind of data we need intergr= yer of service float=salary
# # condition if year of service >3 bonus is 7% or else no bonus


# salary=float(input("please enter your current salary?"))
# YeaarsOfService=int(input("Please enter your years of service?")) #2021,2022,2023,2024

# if YeaarsOfService<2022:
#      bonus= salary*0.07
#      print("net bonus is " , bonus)
# else:
#      print("sorry no bonus")

#12/01/2025 -> Assignment
#Create a Python program that asks the user three simple questions. 
#The program will track the user's score and display the results at the end.

# Step 1: Print three statements
print("Welcome to the Quiz Game!")
print("You will be asked 3 questions. Each correct answer will give you 1 point and if you answer wrong then 0 points.")
print("Let's begin!")

# Step 2: Initialize Score = 0 because 0 or 1 point will be added in quiz 
Score = 0

# Step 3: Print and ask user questions and possible answers
Q1 = "What is the capital of Japan?"
A_1 = "Tokyo"
print(Q1)
print("a) Madrid")
print("b) Tokyo")
print("c) New Delhi")
answer1 = input("Your answer: ").lower()

# Step 4: Check the 1st answer and update the score
if answer1 == "b":
    print("Correct!")
    Score += 1
else:
    print(f"Wrong. The correct answer is '{A_1}'.")

Q2 = "What is the capital of India?"
A_2 = "New Delhi"
print(Q2)
print("a) Madrid")
print("b) Prague")
print("c) New Delhi")
answer2 = input("Your answer: ").lower()

# Step 5: Check the 2nd answer and update the score
if answer2 == "c":
    print("Correct!")
    Score += 1
else:
    print(f"Wrong. The correct answer is '{A_2}'.")

Q3 = "What is the capital of Pakistan?"
A_3 = "Karachi"
print(Q3)
print("a) Karachi")
print("b) Prague")
print("c) Lahore")
answer3 = input("Your answer: ").lower()

# Step 6: Check the 3rd answer and update the score
if answer3 == "a":
    print("Correct!")
    Score += 1
else:
    print(f"Wrong. The correct answer is '{A_3}'.")

# Step 7: Display the final score
print("\nQuiz Complete!")
print(f"Your final score is {Score} out of 3.")

# Step 8: Provide feedback based on the score
if Score == 3:
    print("Excellent work! You're a genius!")
elif Score == 2:
    print("Good job!")
else:
    print("Better luck next time. Keep practicing!")



