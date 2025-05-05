#How super Function handle Multiple Inheritance.
#The super() function handles multiple inheritance by following the Method Resolution Order (MRO), which uses the C3 linearization algorithm to determine the order of parent classes. It ensures that each parent class's method is called exactly once, starting from the next class in the MRO after the current class, providing a predictable and consistent method resolution across the hierarchy.
class Human:
    def eat(self):
        print("Human eats")
        super().eat()

class Mammal:
    def eat(self):
        print("Mammal eats")

class Employee(Human, Mammal):
    def eat(self):
        print("Employee eats")
        super().eat()

emp = Employee()
emp.eat()
print(Employee.mro())

# Output:
# Employee eats
# Human eats
# Mammal eats
# (<class '__main__.Employee'>, <class '__main__.Human'>, <class '__main__.Mammal'>, <class 'object'>)

#Employee.eat() prints "Employee eats".
#super().eat() in Employee calls Human.eat() (next in MRO), which prints "Human eats".
#super().eat() in Human calls Mammal.eat(), which prints "Mammal eats".
#Since Mammal doesn’t call super(), the chain stops.
#----------------------------------------------------------------------------------------

#When Human and Mammal both have an eat method with different implementations, Python uses the Method Resolution Order (MRO) to decide which one Employee calls. Since Human comes first in the MRO, its eat method is executed first.
class Human:
    def eat(self):
        print("Human eats")

class Mammal:
    def eat(self):
        print("Mammal eats")

class Employee(Human, Mammal):
    def eat(self):
        print("Employee eats")
        super().eat()

emp = Employee()
emp.eat()

# Output:
# Employee eats
# Human eats