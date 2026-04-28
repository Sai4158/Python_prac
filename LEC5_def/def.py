def test():
    a = 5
    b = 5
    print(a + b)

# this is a comment

print("Hello, World!")
test()

hi = (2,3,4,5,6)
hi1 = [2,3,4,5,6]
hi2 = {2,3,4,5,6}
hi3 = {1: 'one', 2: 'two', 3: 'three'}

print(type(hi))
print(type(hi1))
print(type(hi2))
print(type(hi3))

def add(x, y):
    return x + y

print(add(10, 20))

class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!" + " Welcome to Python programming."

obj = MyClass("Alice")
print(obj.greet())

# Making class with employee tax class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_tax(self):
        tax_rate = 0.2  # Assuming a flat tax rate of 20%
        return self.salary * tax_rate
    
employee1 = Employee("Bob", 50000)
print(f"{employee1.name}'s tax: {employee1.calculate_tax()}")


# Print forloop and 35 left alingned spaces
word = "Python Programming"
for i in range(5):
    print(f"{i:<35} {word:>15}")   

