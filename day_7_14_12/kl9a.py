# dziedziczenie diamentowe
class Animal:
    def speak(self):
        print("Animal speaks")


class Mammal(Animal):
    def speak(self):
        super().speak()
        # Animal.speak(self)
        print("Mammal sounds")


class Bird(Animal):
    def speak(self):
        super().speak()
        print("Bird sounds")

# (<class '__main__.Bat'>,
# <class '__main__.Mammal'>,
# <class '__main__.Bird'>,
# <class '__main__.Animal'>,
# <class 'object'>)
class Bat(Mammal, Bird):
    pass


bat = Bat()
bat.speak()
# Animal speaks
# Bird sounds
# Mammal sounds
print(Bat.__mro__)