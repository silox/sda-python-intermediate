class Animal:
    def __init__(self, weight, age):
        self.weight = weight
        self.age = age
        print(self.age)

    def look(self):
        pass

    def breath(self):
        pass


class Fish(Animal):
    def swim(self):
        pass


class Mammal(Animal):
    def run(self):
        pass


class Bird(Animal):
    def fly(self):
        pass


class DomesticDog(Mammal):
    def __init__(self, weight, age, breed, coat_color):
        self.breed = breed
        self.coat_color = coat_color
        super().__init__(weight, age)

    def bark(self):
        print('bark!')

    def retrieve(self):
        pass


if __name__ == "__main__":
    doggie = DomesticDog(30, 11, 'doga', 'black')
