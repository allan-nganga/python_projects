#Create a class named employee. Define attributes of that class(self, name, age, id, dept)
class Employee:
    def __init__(self, name, age, emp_id, department):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.emp_id}, Department: {self.department}"

emp1 = Employee("John Doe", 25, 124354, "Technology")

print(emp1)