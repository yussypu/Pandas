existingList = [4,3,5,3,2,8,9]

# Write a program to create empty list and add 1 to 10 values in the list	

integers = list((range(1,11)))
print(integers)

# I have 4 values in list first name, last name, age and occupation, insert first name, last name, age, accupation in the list and first the check how many characters are in each variable and add the number of characters in the list	

info = ["Yahya", "Ehsan","Twenty", "Student"]
firstName = info[0]
lastName = info[1]
age = info[2]
occupation = info[3]

firstNameChar = len(firstName)
lastNameChar = len(lastName)
ageChar = len(age)
occupationChar = len(occupation)

finalList = [firstName, firstNameChar, lastName, lastNameChar, age, ageChar, occupation, occupationChar]

# Write a prgram to add value to the existing list	

exisitingList = [4,3,5,3,2,8,9]
existingList.append(12)

# Write a program to delete the value from the list	
existingList.remove(12)

# Write a program to find the total number of elements in the list	

totalElements = len(existingList)
print(totalElements)

# Write a program to find the total number of elements in the list don't use any function	

count = 0
for element in existingList:
    count += 1
print(count)

# Write a program to sum the value of the list	

sum = 0
for element in existingList:
    sum = sum + element
print(sum)

# Write a program to count the number of elements in a list using recursion	

numOfElements = 0
index = 0
while True:
    if index == len(existingList):
        break
    numOfElements += 1
    index +=1

print(numOfElements)

# Write a program to interchange first and last elements in a list	

existingList = [4,3,5,3,2,8,9]
lastIndex = exisitingList[-1]
exisitingList[-1] = existingList[0]
exisitingList[0] = lastIndex

# Write a program to Program to Swap Two Elements in a List	

existingList = [4,3,5,3,2,8,9]
index1 = 1
index2 = 3
exisitingList[index1], exisitingList[index2] = exisitingList[index2], exisitingList[index1]

print(existingList)

# Write a program to Check if element exists in list in 	

elementToFind = 9
found = False
for i in existingList:
    if elementToFind == i:
        found = True
        break
if found == True:
    print("Found element")

# Write a program to clear a list	

for i in range(len(existingList)):
    existingList.pop()

# Write a program to Reversing a List don't use any function or loop or new list	

existingList = [4, 3, 5, 4, 3, 2, 2]

left = 0
right = len(existingList) - 1

while left < right:
    existingList[left], existingList[right] = existingList[right], existingList[left]
    left += 1
    right -= 1

print(existingList)

# Write a  progtam to Sum of number digits in List	

listToSum = [4,3,2,"Yes", "opo", 9]
sum = 0
for element in existingList:
    if element == type(int):
        sum = sum + element
print(sum)

# write a program to find smallest number in a list	

existingList = [4,3,5,4,3,2,2, 100, 1]
min = 10000000
for i in existingList:
    if i < min:
        min = i 

print(min)

# Write a program to find second largest number in a list	

existingList = [4,3,5,4,3,2,2, 100, 1, 98]

largest = secondLargest = int('-200000000')
for number in existingList:
    if number > largest:
        secondLargest = largest
        largest = number
    elif number > secondLargest and number != largest:
        second_largest = number

# Write a Program to print duplicates from a list of integers	

listOfInt = [4,5,4,3,3,2,1,3]
newList = []

for i in range(len(listOfInt)):
    for j in range(i + 1, len(listOfInt)):
        if listOfInt[i] == listOfInt[j]:
            print(listOfInt[i], end=" ")    

print(newList)

# write a program to Remove multiple elements from a list	

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elements = [2, 5, 8]

for element in elements:
    if element in myList:
        myList.remove(element)

print(myList) 

# write a program to find the even number, odd number, duplicate number and sum of each list and lasgest number from all the list and smallest number	

numbers = [1, 2, 3, 4, 2, 5, 1, 6, 7, 3]

evenNumbers = []
oddNumbers = []
duplicateNumbers = []
totalSum = 0
largestNumber = numbers[0]
smallestNumber = numbers[0]

for num in numbers:
    if num % 2 == 0:
        evenNumbers.append(num)
    else:
        oddNumbers.append(num)
    if numbers.count(num) > 1 and num not in duplicateNumbers:
        duplicateNumbers.append(num)
    totalSum += num
    largestNumber = max(largestNumber, num)
    smallestNumber = min(smallestNumber, num)
print("Even numbers:", evenNumbers)
print("Odd numbers:", oddNumbers)
print("Duplicate numbers:", duplicateNumbers)
print("Sum:", totalSum)
print("Largest number:", largestNumber)
print("Smallest number:", smallestNumber)

# Write a Python program to remove duplicates from a list of lists.	

listOfLists = [[1, 2], [3, 4], [1, 2], [5, 6]]
uniqueLists = []

for sublist in listOfLists:
  if sublist not in uniqueLists:
    uniqueLists.append(sublist)

print(uniqueLists)

# Write a Python program to find items starting with a specific character from a list.	

listOfStrings = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
character = 'c'

for item in listOfStrings:
    if item[0] == 'c':
        print(item)

# Write a Python program to check whether all dictionaries in a list are empty or not.	

listOfDic = [{}, {}, {}]
empty = True

for item in listOfDic:
    if item:
        empty = False
        break
if empty == True:
    print("All dictionaries are empty")

# Write a Python program to flatten a given nested list structure.	

nestedList = [1, [2, [3, [4, 5]]], 6]

flattened = []

def flatten(nested):
  for item in nested:
    if type(item) == list:
      flatten(item)
    else:
      flattened.append(item)

flatten(nestedList)
print(flattened)

# Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.	

listOfDup = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
result = []
prev = None  

for num in listOfDup:
  if num != prev:
    result.append(num)
    prev = num

print(result)

# Write a Python program to pack consecutive duplicates of a given list of elements into sublists.	

listOfDup = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
result = []
currentList = []
prev = None

for num in listOfDup:
  if prev is None or num == prev:
    currentList.append(num)
  else:
    result.append(currentList)
    currentList = [num]
  prev = num

if currentList:
  result.append(currentList)

print(result)

# Write a Python program to split a given list into two parts where the length of the first part of the list is given.	

listToSplit = [1, 1, 2, 3, 4, 4, 5, 1]
length = 3
firstPart = listToSplit[:length]
secondPart = [length:]
resultantList = [firstPart, secondPart]
print(resultantList)
