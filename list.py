# Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.
def list_of_fruits():
    list= ['Apple', 'PineApple', 'Mango', 'Passion', 'Avocado']
    
    for fruit in list:
        print(fruit)
list_of_fruits()

# Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared.
# Example: [1, 2, 3] should become [1, 4, 9].
def list_of_numbers():
    squared_list = []
    numbers=[1,2,3]
    
    for num in numbers:
        squared_list.append(num**2)
       
    return squared_list
result =list_of_numbers()
print(result)
list_of_numbers()

#Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], 
# and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
def lists():
    list1 = [1, 2, 3] 
    list2 = [4, 5, 6]
    combined=[]
    
    for i in range(len(list1)):
        combined.append(list1[i])
        combined.append(list2[i])
    print(combined)
lists()
 
# Given a list of numbers, [3, 1, 4, 1, 5, 9, 2],
# write a program to find and print the two largest numbers in the list without using the max() function.
def largest_numbers():
    a = [3,1,4,1,5,9,2]

    largest = second_largest= float('-inf')

    for val in a:
        if val > largest:
      
            second_largest = largest
            largest= val
        elif val > second_largest and val!=largest:
            largest=val
            
    print(f' The largest number is; {largest}')
    print(f'The second largest number is; {second_largest}')
largest_numbers()