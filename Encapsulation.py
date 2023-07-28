# define the class

class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

# The @property decorator defines a method as a getter
    @property
    def name(self):
        print("Getting name")
        return self._name
    
# @name.setter and @age.setter decorators define the method as a setter. 
    @name.setter
    def name(self, value):
        print("Setting name")
        self._name = value

    @property
    def age(self):
        print("Getting age")
        return self._age
    
    @age.setter
    def age(self, value):
        print("Setting age")
        self._age = value


person = Person("Alice", 25)
print(person.name)   # "Getting name", "Alice"
person.name = "Bob"  # "Setting name"
print(person.name)   # "Getting name", "Bob"
print(person.age)    # "Getting age", 25
person.age = 30       # "Setting age"
print(person.age)    # "Getting age", 30
