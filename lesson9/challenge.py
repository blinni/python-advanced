class Animal:
    def __init__(self, name ):
        self.name = name

animal_1 = Animal("Girafe")
print(animal_1.name)

class Dog:
    def __init__(self, name, breed ):
        self.name = name
        self.breed = breed

dog_1 = Dog("reksi", "Pit Bull")
print(dog_1.name, dog_1.breed)

class Cat:
    def __init__(self, color, sound ):
        self.color = color
        self.sound = sound

cat_1 = Cat("Brown and White", "Meow , Meow!")
print(cat_1.color, cat_1.sound)
