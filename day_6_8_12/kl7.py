class Animal:

    def __init__(self, name):
        self.name = name

    def wydaj_odglos(self):
        pass

    def info(self):
        print(f"Imię: {self.name}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def wydaj_odglos(self):
        print("Miau Miau")

    def info(self):
        super().info()
        print(f"Kolor: {self.color}")


class Tiger(Cat):
    def __init__(self, name, color, liczba_paskow):
        super().__init__(name, color)
        self.liczba_paskow = liczba_paskow

    def wydaj_odglos(self):
        print("Arr Arr!!!")

    def info(self):
        super().info()
        print(f"Liczba pasków: {self.liczba_paskow}")


animal = Animal("Bezimienny")
animal.wydaj_odglos()
animal.info()  # Imię: Bezimienny

cat1 = Cat('Filemon', "Biały w ciapy")
cat1.info()
cat1.wydaj_odglos()
# Imię: Filemon
# Kolor: Biały w ciapy
# Miau Miau

tiger1 = Tiger("Tygrysek", "Pomarańczowy", 15)
tiger1.info()
tiger1.wydaj_odglos()
# Kolor: Pomarańczowy
# Liczba pasków: 15
# Arr Arr!!!
