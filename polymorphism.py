# Polymorphism is the ability of an object or method to take on multiple forms

# methos overriding 

class Animals:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animals):
    def speak(self):
        print("The dog barks")

class Cat(Animals):
    def speak(self):
        print("The cat meows")


#create object

animal = Animals()
dog = Dog()
cat = Cat()

#call the method

print(animal.speak())
print(dog.speak())
print(cat.speak())


# method overloading

class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a+b+c
        else:
            return a+b
    
# create an object
calculator = Calculator()

#call the method

print(calculator.add(2, 5))
print(Calculator.add(5, 8, 7))