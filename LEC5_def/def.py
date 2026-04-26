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