# Basic: Create a dictionary with three key-value pairs representing a
# student's information: name, age, and grade. Print each key-value pair on a new line.
def dictionary():
    student_information = {'name':'Favour' ,
                           'age': 20,
                           'grade':'A+'
                           }
    print(student_information['name'])
    print(student_information['age'])
    print(student_information['grade'])
dictionary()



# Intermediate: Write a function that takes a dictionary of people's names and their ages,
# {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def names_and_age(details):
    
    adults =[names for names, age in details.items() if age >= 21]
    return adults
details ={'Alice': 24,
          'Bob': 19, 
          'Charlie': 30}    
adults=names_and_age(details)
print(adults) 


# Advanced: Given a dictionary representing items in a store with their prices,
# {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, 
# write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'],
# and calculates the total cost.
def items_and_prices():
    prices= {'apple': 0.5,
              'banana': 0.3,
              'orange': 0.7}
    
    items =[ 'apple',
        'orange',
        'banana',
        'banana']
    
    total_cost = 0
    
    for item in items:
        total_cost += prices.get(item,0) 
    print(total_cost)
        
items_and_prices()
       
    

# Challenge: Write a program that counts the occurrences of each word in a given sentence.
# Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
sentence = 'hello world hello'
words = sentence.split()
word_count = {}
for word in words:
    word_count[word]=word_count.get(word,0)+1
    print('Word occurances')
    
for word, count in word_count.items():
    print(f'{word}:{count}')
   
