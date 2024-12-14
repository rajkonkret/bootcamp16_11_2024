import math


class MyFirstClass:
    """
    Klasa w Pyrhonie opisująca punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizująca (konstruktor)
        :param x:
        :param y:
        """
        # self.x = x
        # self.y = y
        self.move(x, y)

    # podpowiedzi typów
    def move(self, x: float, y: float) -> None:
        """
        Metoda przesuwa punkt we wskazane miejsce
        :param x: nowe x punktu
        :param y: nowe y punktu
        :return:
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
        Metoda zwraca odległość punktów przestrzeni euklidesowej
        :param other:
        :return:
        """

        return math.hypot(self.x - other.x, self.y - other.y)

    # metody tostring
    def __str__(self):
        return f"({self.x, self.y})"

    # reprezentacja obiektu dla programisty
    def __repr__(self):
        return f"Point({self.x, self.y}"


ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x0000026DE0787650>
# po dodaniu metody __str__ wyswietli się tak: ((0, 0))
print(ob.x)
print(ob.y)
ob.move(67, 64)
print(ob)  # ((67, 64))
ob.reset()
print(ob)  # ((0, 0))
ob_str = str(ob)  # rzutowanie na str
lista = [ob_str]
print(lista)  # ['((0, 0))']

ob2 = MyFirstClass(7, 98)
ob3 = MyFirstClass(43, 134)
print(ob.calculate(ob2))
print(ob.calculate(ob3))
print(ob3)  # ((43, 134))
# 98.2496819333274
# 140.73023839957068
# ob3.calculate("a")
#     return math.hypot(self.x - other.x, self.y - other.y)
#                                ^^^^^^^
# AttributeError: 'str' object has no attribute 'x'

lista_ob = [ob, ob2, ob3]
print(lista_ob)
# [<__main__.MyFirstClass object at 0x000001E9AFFF07A0>,
# <__main__.MyFirstClass object at 0x000001E9AFFF3230>,
# <__main__.MyFirstClass object at 0x000001E9AFFF20C0>]
# po nadpisaniu __repr__ lista obiektów wyglada tak:
# [Point((0, 0), Point((7, 98), Point((43, 134)]