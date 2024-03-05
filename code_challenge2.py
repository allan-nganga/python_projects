#accepts user input
num_list = input("Enter a list of integers seperated by spaces: ").split()
#convert user input to integers
num_list =[int(num) for num in num_list]

#compute the sum of all integers in the list
total_sum = sum(num_list)

#print the total
print("The sum of the integers in the list is:", total_sum)
