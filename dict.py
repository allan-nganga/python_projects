#collecting user input
name = input("Enter your name: ")
age = input("Enter you age: ")
fav_color = input("Enter your favourite color: ")

#store user input in a dictionary
thisdict = {
    "name": name,
    "age": age,
    "favourite_color": fav_color
}

print(thisdict)