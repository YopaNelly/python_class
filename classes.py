# create a class that  represents a person

class Person:

    # defining the constructor of a class

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # define methods that act on these attributes 

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name =name

    def set_age(self, age):
        self.age = age


# to creatr an odject of this class

person1 = Person("Nelly", 30)
person2 = Person("Alice", 40)

print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)        
#***************************************************
#***************************************************

# Inheritance

"""
create a new class that is a modified version of an existing class

use inheritance to create a class student that inherits from the Person class
"""
class Student(Person):
    SCHOOL = "NAHPI Bamenda"

    def __init__(self, name, age, student_id):

        """
        In Python, the super() function returns a temporary object 
        of the superclass, and it allows you to call methods of 
        that superclass. The super().__init__(name, age) line is 
        calling the constructor (the __init__() method) of the 
        superclass (Person), passing in the name and age parameters.
        """

        super().__init__(name, age)

        self.student_id = student_id

        def get_student_id(self):
            return self.student_id

print(Student.SCHOOL)
