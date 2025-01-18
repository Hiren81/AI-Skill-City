#Conditional Statements
#in different languages &&= and ||=or!=Not
#In python we use (and,or,not)
# if, else

#Syntax#

#if conditions:
#statement

#elif conditions:
#statement

#else 
#statement

email="hirenmoghe@gmail.com"
password="123456"

if email=="hirenmoghe@gmail.com" and password=="123456":
   print("login is successfull")
else:
	print("login is not successful")


#Example practice
#write a progrma in python that take inputs from user and determine if the given number is odd or even  
#like 2,4,6,8 and 2,3,5,7 in python code make it very simple to understand line by line 

# # Step 1: Ask the user to enter a number
# number = int(input("Enter a number: "))  # Converts the user input to an integer

# # Step 2: Check if the number is even
# if number % 2 == 0:  # If the remainder when dividing by 2 is 0, the number is even
#     print(f"The number {number} is even.")
# else:
#     # Step 3: If the above condition is false, the number is odd
#     print(f"The number {number} is odd.")

# Explanation:
# input("Enter a number: ") - Prompts the user to enter a number.
# int() - Converts the input string into an integer for mathematical operations.
# number % 2 - Calculates the remainder when the number is divided by 2.
# If the remainder is 0, the number is even.
# Otherwise, the number is odd.
# if and else - Use conditional statements to print the appropriate message based on the check.

number= int(input("Enter number "))
if number%2==0:
    print("number is even")
else:
     print("number is odd")      



