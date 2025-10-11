class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound")

    def description(self):
        print(f"This animal is named {self.name}.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Woof, woof!")

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Meow, Meow")

    def description(self):
        print(f"color: {self.color}.")

dog = Dog("rex", "Black")
dog.sound()
dog.description()

cat = Cat("Whiskers", "Black")
cat.sound()
cat.description()