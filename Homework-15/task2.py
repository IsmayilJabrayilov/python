fruits=("apple", "Banana", "orange", "mango", "strawberry", "grape", "mandarin", "strawberry")
calories=(52, 96, 62, 605, 33, 68, 50, 33)


#Convert the previously defined tuples to lists
fruits_list=list(fruits)
calories_list=list(calories)

#Print out the 5th element (strawberry), out of the list, with its caloric value.
print (f'{fruits_list[4]} has {calories_list[4]} calories')

#Print out the second last food, and its caloric value
print (f'{fruits_list[-2]} has {calories_list[-2]} calories')

#Print out all the unique foods in the list

unique_fruits = list(set(fruits_list))
print (unique_fruits)

#Create a dictionary with their unique key, values from the table listed.


fruit_dic = {}

for i in range(len(fruits)):
    fruit_dic[fruits[i]] = calories[i]

print(fruit_dic)

