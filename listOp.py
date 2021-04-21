numbers=[12,54,698,45,41,45,89,45]
print(numbers)
# numbers.append(25)  #to append a number
# numbers.insert(2,0) #to insert at specific postion
# numbers.remove(54) #to remove a specific item from the list
# numbers.clear() #to empty the list
# numbers.pop() #to remove the last element
# print(numbers.index(698)) #to get the index of first occurrence of the list
# x=50 in numbers #to find a number in list exists or not
# y=numbers.count(45) #to find the count of numbers in list
# numbers.sort()
# numbers.reverse()
n=numbers.copy()
x=numbers
numbers.append(100)
print(numbers)
print(n)
print(x)