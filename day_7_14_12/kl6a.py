# dziedziczenie po wielu klasach

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


a = A()
a.method()  # Metoda z klasy A

b = B()
b.method()  # Metoda z kalsy B


class C(B, A):  # kolejność ma znaczenie
    """
    Klasa C dziedziczy po klasie B i A
    """


c = C()
c.method()  # Metoda z kalsy B
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


class D(A, B):
    """
    Klasa dziedziczy po A i B
    """


d = D()
d.method()  # Metoda z klasy A


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E
print(E.__mro__)


# (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

class F(B, A):
    """
    Klasa dziedziczy po klasie B i A
    """

    def method(self):
        A.method(self)


f = F()
f.method()  # Metoda z klasy A


class G(A, B):
    """
    Dziedziczy po A i B
    """

    def method(self):
        super().method()  # super() - użycie klasy wyższej
        print("Dopisane")


g = G()
g.method()


# Metoda z klasy A
# Dopisane


class H(A, B):

    def method(self):
        B.method(self)
        super().method()
        print("Dopisane w H")


h = H()
h.method()
# Metoda z klasy B
# Metoda z klasy A
# Dopisane w H
