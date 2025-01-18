# LIST, TUPLE,SETS,DICTIONARIES
#[]=lIST
#{}=Sets
#()=Tuples
#{ "key": value,
# xxxxxxxx
# }=Dictionaries, key value pair
# List=[1,2,3,4,5]
# List_fruit=["apple","banana","cherry","mango"]#List of strings oredered, changable ,duplicates 
# print(List_fruit)
# List_fruit.append("banana")
# List_fruit.remove("orange")
# print(List_fruit)

# List_fruit.pop(len(List_fruit-1)) #3-1=2
# #extend= to menrge two list
# #insert= to instert
# #pop=to remove element at specific index 


# #Tuples
# #always small brackets
# # #eg 
# fruit=("apple", "banana", "Cherry") # tuple of strings ordered unchangable, duplicates, indexed
# #they are not changable 
# fruit[0]= "pear" # Type error :tuple object does not support item assignment 

fruit=("apple", "banana", "Cherry")
print(fruit)

#Now to change tupple to List from (), to [] 
print(type(fruit))
print(list(fruit))

#Sets
#what are Sets 
#unordered, unchangable,unindexed
# #no duplicates 
#eXAMPLE CASINO GAMES 

fruit={"apple", "banana", "Cherry"}
fruit.add("kiwi")
print(fruit)
fruit.clear()
print(fruit)

#Changable, ordered,no duplicate , indexed
phoneDictionanry={
    "Hiren": 1234567,
    "Minal": 1234543,
    "Dheepu":5643232,
}
print(phoneDictionanry)

#nested dictionary

users = { "user1": 
         { "firstName": "Jane", 
          "lastName": "Doe", 
          "phoneNumber": "1234567890", 
          "email": "lorem@gmail.com", 
          "address": "123, Lorem Ipsum" }, 

        
          "user2": 
          
          { "firstName": "John", 
            "lastName": "Doe", 
            "phoneNumber": "1234567890",
            "email": "abc@mail.com", 
            "address": "123, Lorem Ipsum" } 
                    
        }
print(users)
#print(user2)