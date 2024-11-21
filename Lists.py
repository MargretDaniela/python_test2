# Basic: Create a list of 5 fruits and print each 
# fruit on a new line using a for loop.
def fruits ():
    fruits = ['apple','banana','jackfruit','orange','berries']

    for x in fruits:
        print(x) 
fruits()

# Intermediate: Write a function that takes a list of numbers and 
# returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].
def squared_numbers():
    squared_list = []
    numbers = [1, 2, 3]
    for num in numbers:
        squared_list.append(num ** 2)
    return squared_list 
result = squared_numbers()
print(result)
# Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] 
# and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
def combined_lists():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = []
    for num in range(len(list1)):
        combined.append(list1[num])
        combined.append(list2[num])
    print(combined)
combined_lists()


# Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2],
#  write a program to find and print the two largest numbers in the list without using the max() function.
 
numbers = [3, 1, 4, 1, 5, 9, 2]
largest = numbers[2]
for num in numbers[1:]:
    if num > largest:
        print(num)