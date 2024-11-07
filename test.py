print("This is a python file")


# A method to get Username and say hello to the user
def sayName():
    name = input("What is your name: ")
    print("Hello " + name)

# sayName();

# Method to print numbers from specified range
def printNum(x):
    for i in range(2, x + 1):
        print(i)

# printNum(5)

# Search Array

#? Problem: Given an array of integers A and an integer v, if v is in A then return its position, otherwise return -1
# we are given an array A, and an integer v
# we return the position of v if its in the array A, if not return -1
# given array[1, 3, 2, 4 ,5], 4 return 3
# given array[1, 3, 2, 4 ,5], 6 return -1

# create a variable to store the position of the variable, set it as -1 since its not found yet
# create a loop that chcecks the array and compares with v, if v is in the array return the index(i)
# def checkArr(A , v):
#     found = -1
#     for i in range(len(A)):
#         if A[i] == v:
#             found = i
#     print(found) ;

# checkArr([1, 3, 2, 4 ,5] , 6);


# variables in python

def checkBalance():
    balance = input("How much do you have ")


    if balance == 0:
        print("You dont have enough money")
    else: 
        print("Your have money")

# checkBalance()


# Conjuctions

def checkBalance2():
    balance = input("How much do you have ")
    overdraft = input("What is your overdraft ")


    if overdraft == 0 and balance < 0 :
        print("You dont have enough money")
    else:
        print("You have money")

# checkBalance2()

# for loop
# for i in range(1, 6, 2):
#     print(i);


# while loop 
i = 10
while i > 5:
    if i == 0:
        break
    print(i)
    i -= 1;

print("-------")

# Function to print the first and last letter of an array
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def printFirs(arr):
    for i in arr:
        first = arr[0]
    print(first)
printFirs(arr1) 

def findLength(x):
    print(len(x)) 

findLength(arr1)


def printLast(arr):
    for i in arr:
        last = len(arr) - 1
    print(arr[last])
printLast(arr1)
    

# Tests

ls = []
for i in range(2, 7):
    ls.append(i)
print("initial list: " + str(ls))
ls.append(42) # Adds value to the end of array
ls.pop(2) # removes values from the specified index
ls.insert(1, 24) # insert the value 24 to index 1

print("Final list: " + str(ls))  # [2, 24, 3, 5, 42]