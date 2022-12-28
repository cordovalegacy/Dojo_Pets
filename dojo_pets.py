class Pet:

    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self. health = 100
        self.energy = 50

    def vet(self):
        print(f"{self.name} has {self.health} Health and {self.energy} Energy remaining")

    def sleep(self):
        self.energy = self.energy + 25
        print()
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        return self

    def play(self):
        self.health = self.health + 5
        self.energy = self.energy - 10
        return self

    def makes_noise(self):
        self.health = self.health + 5
        self.energy = self.energy + 20
        print(self.noise)
        return self

class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        print("All tuckered out from a walk")
        return self

    def feed(self):
        self.pet.eat()
        print("Feeding dog")
        return self

    def bathe(self):
        self.pet.makes_noise()
        print("Cleaning Dog")
        return self

    def checkup(self):
        self.pet.vet()
        print("Vet takes a look")
        return self

Charlie = Pet("Charlie", "Chihuahua", "Spin", "Yip")
some_treats = ["Greenies", "Bone", "Pizza"]
some_food = ["Wet Food", "Dry Food", "People Food"]

Ninja_1 = Ninja("Brendan", "Cordova", Charlie, some_treats, some_food)

print(Ninja_1)
Ninja_1.walk().feed().checkup().walk().walk().checkup()
Ninja_1.bathe().feed().checkup()