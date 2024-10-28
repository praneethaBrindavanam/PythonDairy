Inheritance
Inheritance is a mechanism in OOP that allows a new class (child or derived class) to inherit attributes and methods from an existing class (parent or base class). This promotes code reusability and establishes a hierarchical relationship between classes.

Key Points:
Single Inheritance: A derived class inherits from a single base class.
Multiple Inheritance: A derived class inherits from multiple base classes.
Method Overriding: A derived class can provide a specific implementation of a method that is already defined in its base class.
Example of Inheritance
# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Animal speaks"

# Derived class
class Dog(Animal):
    def speak(self):  # Overriding the base class method
        return "Woof"

class Cat(Animal):
    def speak(self):  # Overriding the base class method
        return "Meow"

# Creating instances
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.name) 

 # Output: Buddy
print(my_dog.speak())

  # Output: Woof
print(my_cat.name) 

 # Output: Whiskers
print(my_cat.speak())

  # Output: Meow
Polymorphism
Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to be defined in a base class and overridden in derived classes, enabling the same method to behave differently based on the object that is calling it.

Key Points:
Method Overriding: As shown in the inheritance example, derived classes can override base class methods.
Duck Typing: In Python, polymorphism can also be achieved through duck typing, where the type or class of an object is less important than the methods it defines.
Example of Polymorphism
class Bird:
    def fly(self):
        return "Flies high"

class Penguin(Bird):
    def fly(self):  # Overriding the base class method
        return "Cannot fly"

class Sparrow(Bird):
    pass  # Inherits fly method from Bird

def make_bird_fly(bird):
    print(bird.fly())

# Creating instances
sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow) 

 # Output: Flies high
make_bird_fly(penguin) 

 # Output: Cannot fly

Summary
Inheritance allows for the creation of a new class based on an existing class, promoting code reuse and establishing a relationship between classes.
Polymorphism enables methods to be used interchangeably across different classes, allowing for flexibility and dynamic behavior in programs.
Both concepts are fundamental in OOP and help in building scalable and maintainable code.


