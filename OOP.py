print("Hello World")

# Blueprint the class of Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Function to display value
    def display(self):
        print(self.name + self.age)

# Subclass from the Superclass: Person using super()
class Student(Person):
    def __init__(self, name, age, studentID):
        super().__init__(name, age)
        self.studentID = studentID

# Subclass from the Superclass: Person using Person
class Worker(Person):
    def __init__(self, name, age, workerID):
        Person.__init__(self, name, age)

# Create the new object
# p1 = Person("itmam", "24")

p1 = Student("Itmam", "25", 2017720431)
# p1 = Worker("Itmam", "25", 20177123123)

# Display output based on the object
print(p1.name) # Outcome name
print(p1.age) # Outcome age
p1.display() # Outcome function in the class Person
print(p1.studentID) # Outcome student id