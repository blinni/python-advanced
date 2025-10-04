from lesson8.public_attribute import my_class


class MyClass:
    def __init__(self):
        self._protected_variable = "This is a protected attribute"
    def _protected_method(self):
        print("This is a protected  method ")

my_class = MyClass()

#error attributes

print(my_class._protected_variable)
my_class._protected_method()