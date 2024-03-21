class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"My name is {self.name}. I am {self.age} years old and my gender is {self.gender}"

introduce = Person("John Doe", 25, "Male")

print(introduce)