#Accept user input for the first set of integers
set1 = set(input("Enter the first set of integers separated by spaces: ").split())

#Accept user input for the second set of integers
set2 = set(input("Enter the second set of integers separated by spaces: ").split())

#convert the input to integers
set1 = {int(num) for num in set1}
set2 = {int(num) for num in set2}

#create a new set that contains only the elements that are common to both sets
common_elements_set = set1.intersection(set2)

#print the new set
print("The set containing elements common to both sets is:", common_elements_set)