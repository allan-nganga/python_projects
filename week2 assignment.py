#create an empty list
my_list = []

#append the following values to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#Insert the value 15 to my list at the second position in the list
my_list.insert(1, 15)
#print the updated list
print(my_list)

#create another list with other elements
list = [50, 60, 70]
#extend my_list with elements form the new list
my_list.extend(list)
#Print the list after extending my-list
print(my_list)

#remove the last element from my_list
my_list.pop(7)
#print the new list after removing the last element
print(my_list)

#sort the list in ascending order
my_list.sort()
#print the sorted list
print(my_list)

#find and print the index of value 30 in my list
index_of_30 = my_list.index(30)
print(f"The index of value 30 in my_list is: {index_of_30}")