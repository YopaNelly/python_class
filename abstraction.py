# Abstraction is the process of breaking down a complex system into smaller, simpler components.

# import the Abstract Base Class (abc)

from abc import ABC, abstractmethod


# define an abstract class Animal that 
# subclasses the built-in ABC class. We 
# define a single abstract method speak(). 
# Notice that we do not supply an implementation 
# for the method, we only define the method signature.


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# To create a concrete implementation of the Animal class

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
# create an object
dog = Dog()
cat = Cat()

# call the methods
print(dog.speak())
print(cat.speak())
