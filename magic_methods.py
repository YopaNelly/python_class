class Person:
    def __init__(self, name, age):
        self.name =name
        self.age = age


# Method are:
    """
    __init__ : when object are created
    __str__ : when object is printed
    __add__ : when 2 objects are added

    """

    def __str__(self):
        return "Person: " + self.name
    

person1 = Person("Alice", 25)

print(person1)