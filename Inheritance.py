# main class
class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass moth implement adstract methods")
    
# sub 1

class Dog(Animals):
    def speak(self):
        return "Woof!"
    
class Cat(Animals):
    def speak(self):
        return "Meow!"
    


dog = Dog("Fido")
cat = Cat("Fluffy")

print(dog.name, dog.speak())   # Fido Woof!
print(cat.name, cat.speak())   # Fluffy Meow!

