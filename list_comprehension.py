#list of words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

#use list comprehension to create a new list with words of odd length
odd_length_words = [word for word in words if len(word) % 2 != 0]

#print the original list of words
print("Original list of words:", words)

#print the new list with words of odd length
print("Words with an odd number of characteristics:", odd_length_words)