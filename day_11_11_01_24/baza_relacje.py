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
        order_by='Address.email',
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