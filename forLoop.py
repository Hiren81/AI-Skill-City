# #For Loop
# #for loop- printing numbers from 1 to 10
# #syntax
# #for condition
# #    statements....

# for i in range(1,11):
#     print(i)

# i=1
# while i<50:
#     print(i)
#     i=i+1     #incrementing the value of i by 1
#     i+=1      #

#     #eg1 factorial of 5=5*4*3*2*1=120
#     # Calculate the factorial of 5
# number = 1
# for i in range(1,6):
#     number = number * i
#     print(number)
# #same eg by different way 

# myFirstName = "Muhammed"
# for character in myFirstName:
#     print(character)
# myList = [1,2,3,4,5,6,7,8,9,10]
# for number in myList:
#     print(number)
# mySet = {1,2,3,4,5,6,7,8,9,10}
# for number in mySet:
#     print(number)
# myTuple = (1,2,3,4,5,6,7,8,9,10)
# for number in myTuple:
#     print(number)    

#break= to break the loop
#continue= to skip the currentiteration and move to next iteration
#pass= to do nothing 

# #Activity
# countryLists=["Japan","Philipines","Spain","China"]
# for i in range(1,5):
#     if countryLists=="Spain":
#     print("yay Spain the 3rd in you list of favourate countries")
# else:
#     print("Boo")

# countryList = ["USA", "UK", "Spain", "France"]
       
# for country in countryList:
#     print(country)
# if countryList[2] == "Spain":
#     print("Yaaay Spain is 3rd in your list of favourite countries")
# else:
#     print("message")    

#Activity
#Name="Hiren"
myFirstName = "Hiren" #N,E,R,I,H
for name in myFirstName[::-1]:
    print(name)


