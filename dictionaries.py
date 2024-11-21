# Basic: Create a dictionary with three key-value pairs representing a student's
#  information: name, age, and grade. Print each key-value pair on a new line.
student_details = {
    'name':'Daniela',
    'age': 20,
    'grade': 'A'
}
print(student_details ['name'])
print(student_details ['age'])
print(student_details ['grade'])
# Intermediate: Write a function that takes a dictionary of people's names and their
#  ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def names_and_age(details):
    adults = [names for names, age in details.items() if age >= 21]
    return adults
details= {'Alice': 24,
            'Bob': 19, 
            'Charlie': 30
            }

adults = names_and_age(details)
print(adults)

# Advanced: Given a dictionary representing items in a store with their 
# prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought
# , ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
prices= {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
items = ['apple', 'orange', 'banana', 'banana']
total_cost  = 0
for item in items:
    total_cost += prices.get(item,0)
print(total_cost)
# Challenge: Write a program that counts the occurrences of each word in a given sentence
# . Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
def count_words(sentence):
    # Convert the sentence to lowercase and split it into words
    words = sentence.lower().split()
   
    # Initialize an empty dictionary to store word counts
    word_count = {}
   
    # Loop through each word in the list of words
    for word in words:
        # Remove any punctuation
        word = word.strip(",.?!;:")
       
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
   
    return word_count

#using the sentence below
sentence = "hello everyone , hello people . Hello Africa , my Africa  . "

# Call the function and print the result
result = count_words(sentence)
print(result)