import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'bark'


if __name__ == "__main__":
    cat = Cat()
    dog = Dog()
    animals = [cat, dog]
    for animal in animals:
        animal.make_sound()
