# relacje w bazach danych
# typy relacji

# jeden do jednego - Obydwie tabele mogą zawierać tylko jeden rekord po każdej stronie
# Każda wartość klucza podstawowego dotyczy tylko jednego lub nie dotyczy żadnego rekordu w tabeli powiązanej.
# Relacje "jeden do jednego" są w większości wymuszane przez reguły biznesowe i nie wynikają w sposób naturalny z danych.
# Jeśli taka reguła nie obowiązuje, możliwe jest łączenie obydwu tabel bez naruszania reguł normalizacji.

# jeden do wielu - tabele klucza podstawowego zawiera tylko jeden rekord, dotyczy jedenego, żadnego,
# wielu rekordów w powiązanej tabeli

# wiele do wiele - kazdy rekord obydwu tabel mozę odnośić się do dowolnej liczby rekordów
# W przypadku takich relacji wymagana jest trzecia tabela nazywana tabelą powiązań,
# ponieważ systemy relacyjne nie mogą bezpośrednio obsługiwać takiej relacji.
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///adress_book.db', echo=True)
Base = declarative_base()


# encje - klasy odwzorowujące tabele w bazie danych
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)
    addresses = relationship(
        'Address',
        back_populates='person',
        order_by='Address.email',  # ORDER BY address.email sortowanie po mailu
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __repr__(self):
        return self.email


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

anakin = Person(name='Anakin', age='38')
anakin2 = Person(name='Anakin Anakin', age=38)
anakin2.addresses = [Address(email='anakin@wp.pl')]

# obiekt z adresami, wiecej niz jeden adres
obi = Person(name='Obi Wan Kenobi', age=45)
obi.addresses = [
    Address(email="obi@exmple.com"),
    Address(email='waaka@wp.pl')
]
chewee = Person(name='Chewbacca', age=50)
chewee.addresses = [
    Address(email="chewbacca@exmple.com"),
    Address(email='chewee@wp.pl')
]

session.add(anakin)
session.add(anakin2)
session.add(obi)
session.add(chewee)

session.commit()

all_ = session.query(Person).all()
print(all_)
# [Anakin (id=1), Anakin Anakin (id=2), Anakin (id=3), Anakin Anakin (id=4),
# Obi Wan Kenobi (id=5), Anakin (id=6), Anakin Anakin (id=7), Obi Wan Kenobi (id=8)]

first = session.query(Person).first()
print(first)  # Anakin (id=1)
print(type(first))  # <class '__main__.Person'>
# wiek i imię?
print(first.name, first.age)  # Anakin 38

obi_list = session.query(Person).filter(
    Person.name.like('Obi%')  # WHERE person.name LIKE ?
).all()
print(obi_list)
# id, name, age, email
# Chewbacca

chwee_list = session.query(Person).filter(
    Person.name.like('Che%')  # WHERE person.name LIKE ?
).all()
print(chewee)

for o in chwee_list:
    print(o)
    print(f"{o.id=}, {o.name=}, {o.age=}, {o.addresses=}")

# o.id=31, o.name='Chewbacca', o.age='50', o.addresses=[chewbacca@exmple.com, chewee@wp.pl]
# Chewbacca (id=35)
# o.id=35, o.name='Chewbacca', o.age='50', o.addresses=[chewbacca@exmple.com, chewee@wp.pl]
# Chewbacca (id=39)
# o.id=39, o.name='Chewbacca', o.age='50', o.addresses=[chewbacca@exmple.com, chewee@wp.pl]
# Chewbacca (id=43)
# o.id=43, o.name='Chewbacca', o.age='50', o.addresses=[chewbacca@exmple.com, chewee@wp.pl]
# Chewbacca (id=47)
# o.id=47, o.name='Chewbacca', o.age='50', o.addresses=[chewbacca@exmple.com, chewee@wp.pl]
# Chewbacca (id=51)
# o.id=51, o.name='Chewbacca', o.age='50', o.addresses=[chewbacca@exmple.com, chewee@wp.pl]

# Chewbacca (id=63)
# 2025-01-11 11:28:17,389 INFO sqlalchemy.engine.Engine SELECT address.id AS address_id, address.email AS address_email, address.person_id AS address_person_id
# FROM address
# WHERE ? = address.person_id ORDER BY address.email
# 2025-01-11 11:28:17,389 INFO sqlalchemy.engine.Engine [cached since 0.009233s ago] (63,)
# o.id=63, o.name='Chewbacca', o.age='50', o.addresses=[chewbacca@exmple.com, chewee@wp.pl]
