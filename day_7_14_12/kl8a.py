# dziedziczenie diamentowe

class A:
    def method(self):
        print("Metoda z kalsa A")


class B(A):
    def method(self):
        print("Metoda z klasy B")


class C(A):
    def method(self):
        print("Metod a zkalsy C")


class D(B, C):
    """
    Klasa D dziedziczy po B i C a one dziedziczą z A
    """


d = D()
d.method()
print(D.__mro__)


# (<class '__main__.D'>,
# <class '__main__.B'>,
# <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>)
# class E(A, D):
#     pass
#
# print(E.__mro__)
# Traceback (most recent call last):
#   File "C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_7_14_12\kl8a.py", line 33, in <module>
#     class E(A, D):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, D
# E A D B C A
class F(D, A):
    pass


print(F.__mro__)
# (<class '__main__.F'>, <class '__main__.D'>,
# <class '__main__.B'>,
# <class '__main__.C'>,
# <class '__main__.A'>, <class 'object'>)
