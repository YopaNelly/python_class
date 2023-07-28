# Method overriding (provide != implementation for a method that is already definedin a superclass)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def say_hello(self):
        print("Hello, my name is", self.name, "and my ID is", self.student_id)

student1 = Student("Alice", 25, 123)
person1 = Person("Nelly", 90)
student1.say_hello()
person1.say_hello()
