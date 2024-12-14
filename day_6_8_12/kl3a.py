from pprint import pprint


class ContactList(list['Contact']):
    """
    Lista z metodą serach()
    """

    def search(self, name):
        matching_contacts = []
        for c in self:
            if name.casefold() in c.name.casefold():
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    # all_contacts = []  # pusta lista
    all_contacts = ContactList()  # pusta lista

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    # __repr__ rownież zmienia __str__
    def __repr__(self):
        return f"{self.name!r} {self.email!r}"


class Suplier(Contact):
    """
    Klasa Suplier dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")

    def __repr__(self):
        return f"{self.name} {self.email}"


class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, mail, phone="000000000"):
        super().__init__(name, mail)
        self.phone = phone

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name} {self.email} +48{self.phone}"


c1 = Contact("Adam", "adam@wp.pl")
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c2.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c3.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
s1 = Suplier("Marek", "marek@o2.pl")
print(s1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]
print(c1.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]
s1.order("Kawa")  # Kawa zamówiono od Marek
s1.order("Herbata")  # Herbata zamówiono od Marek

lista = []
# lista.search("Marek") # AttributeError: 'list' object has no attribute 'search'

c_l = ContactList()
print(c_l.search("Marek"))  # []
c_l.append(c1)
c_l.append(c2)
c_l.append(c3)
c_l.append(s1)
print(c_l.search("Marek"))  # [Marek marek@o2.pl]
print(Contact.all_contacts)  # [Adam adam@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@o2.pl]
# !r - odaje automatycznie cudzysłów do stringów
# ['Adam' 'adam@wp.pl',  -> Contact
#  'Radek' 'radek@wp.pl',
#  'Tomek' 'tomek@wp.pl',
#  Marek marek@o2.pl] -> Suplier
f1 = Friend("Marcin", "marcin@marcin.pl")
print(f1)  # Friend Marcin marcin@marcin.pl +48000000000
print(f1.all_contacts)
# ['Adam' 'adam@wp.pl', 'Radek' 'radek@wp.pl',
#  'Tomek' 'tomek@wp.pl',
#  Marek marek@o2.pl,
#  Friend Marcin marcin@marcin.pl +48000000000]
f1.order("Kawa")  # Kawa zamówiono od Marcin

f2 = Friend("Ania", "ania@pl.pl", "987789987")
print(f2)  # Friend Ania ania@pl.pl +48987789987
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)

print(f2.all_contacts.search("Radek"))  # ['Radek' 'radek@wp.pl']
print(f2.all_contacts)
# ['Adam' 'adam@wp.pl', 'Radek' 'radek@wp.pl', 'Tomek' 'tomek@wp.pl',
#  Marek marek@o2.pl,
#  Friend Marcin marcin@marcin.pl +48000000000,
#  Friend Ania ania@pl.pl +48987789987]

pprint(f2.all_contacts)
# ['Adam' 'adam@wp.pl',
#  'Radek' 'radek@wp.pl',
#  'Tomek' 'tomek@wp.pl',
#  Marek marek@o2.pl,
#  Friend Marcin marcin@marcin.pl +48000000000,
#  Friend Ania ania@pl.pl +48987789987]
