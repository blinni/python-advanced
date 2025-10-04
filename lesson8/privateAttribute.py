from lesson8.public_attribute import my_class


class MyClass:
    def __init__(self):
        self.__private_attribute = "This is a private attribute"
    def __private_method(self):
print("This is a method attribute")

my_class = MyClass()

#error attributes

print(my_class.__private_variable)
my_class.__private_method()