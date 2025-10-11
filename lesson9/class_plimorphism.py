class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
         print(f"{self.name} make this sound: Woof")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
         print(f"{self.name} make this sound: Meow")


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
         print(f"{self.name} make this sound: chirp")

dog = Dog("buddy")
cat = Cat("whiskers")
bird = Bird("twetie")

for animal in (dog,cat,bird):
      animal.sound()

