# Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.
def even_numbers():
    for even in range(2,20,2):
        print(even)
even_numbers()

# Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.
number = 0 
while number < 0:
    number = int(input("Enter a number:"))

    if number > 10:
        print(f"Enter a number greater than 10 ")

    else:
        print(f"Number  is greater than 10 ")
# # Advanced: Write a program that prints the multiplication table (from 1 to 10) 
# # for numbers from 1 to 5 using nested for loop
for i in range(1,11):
    for k in range(1,6):
        print(i*k, end= "\t")
    print("\n\n")


# # Challenge: Givena list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find
# #  the sum of all odd numbers and print the result.
# x =  [4, 7, 2, 9, 12, 15]
# for i in x :
#     print(i)
#     sum =0 
    
