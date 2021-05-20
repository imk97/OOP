print("Hello World")

# Blueprint the class of Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method/Function to display value
    def display(self):
        print(self.name + self.age)

# Subclass from the Superclass: Person using super(): Inheritance
class Student(Person):
    def __init__(self, name, age, studentID):
        super().__init__(name, age)
        self.studentID = studentID

    def display(self):
        print(self.name + self.age + self.studentID)

# Subclass from the Superclass: Person using Person : Inheritance
class Worker(Person):
    def __init__(self, name, age, workerID):
        Person.__init__(self, name, age)

    def display(self):
        print(self.name + self.age)

# Create the new object
# p1 = Person("itmam", "24")

# p1 = Student("Itmam", "25", 2017720431)
# p1 = Student("Khairi", "50", 1234556)
# p1 = Worker("Itmam", "25", 20177123123)


# List/Array of person
listPerson = []
listPerson.append(Student("Itmam", "25", 201231231))
listPerson.append(Student("Khairi", "50", 2123432432))

for obj in listPerson:
    print(obj.name, obj.age, obj.studentID, sep="|")


# Display output based on the object
# print(p1.name) # Outcome name
# print(p1.age) # Outcome age
# p1.display() # Outcome function in the class Person
# print(p1.studentID) # Outcome student id

p1 = Student("itmam", "021123123", "12313213123")
p1.display()


from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("Passed value: ", x)
    
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")

# object of test_class method
test_obj = test_class()
test_obj.task()
test_obj.print(100)

# object of example_class method
example_obj = example_class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))

# Pointers
x = 1
print("Address of x : ", hex(id(x)))

y = 2
print("Address of y : ", hex(id(y)))

# Data structure: Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def print(self):
        print(self.data)

def countNodes(Head):
    count = 1
    current = Head
    while current.next != None:
        count += 1
        current = current.next
    return count

class SLinkedList:
    def __init__(self):
        self.headval = None

    # Print the linked list
    def listprint(self):
        printval = self.headval # create an object because self.headval store value class Node(6)
        while printval is not None:
            print(printval.data, printval.next, sep='|')
            printval = printval.next

list = SLinkedList()
list.headval = Node(6)
a2 = Node(5)
a3 = Node(4)
a4 = Node(3)

list.headval.next = a2
a2.next = a3
a3.next = a4
a4.next = None

list.listprint()
print("Amount of nodes in linked list : ", countNodes(list.headval))