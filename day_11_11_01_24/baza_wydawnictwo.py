from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine("sqlite:///moja_baza_danych.db")
Base = declarative_base()


# Author, Book, Publisher

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates='author')


class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="publisher")


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates='books')
    publisher = relationship("Publisher", back_populates="books")


# tworzenie tabel w bazie danych na podstawie encji
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# new_author = Author(name='Adam Mickiewicz')
# new_publisher = Publisher(name="Wydawnictwo XYZ")
# new_book = Book(title="Pan Tadeusz", author=new_author, publisher=new_publisher)
#
# session.add_all(
#     [new_author, new_publisher, new_book]
# )

new_author = Author(name='Jan kowalski')
new_publisher = Publisher(name="Wydawnictwo ABC")
new_book = Book(title="Python średniozaawansowany", author=new_author, publisher=new_publisher)

session.add_all(
    [new_author, new_publisher, new_book]
)

session.commit()

# odczytac z bazy autorów i z autorów odczytac ich ksiązki
# z ksiązek odczytać wydawców
# wypisac autor, ksiązka, wydwaca

authors = session.query(Author).all()
print(authors)
for author in authors:
    print(f"Author: {author.name}")
    for b in author.books:
        # print(f"Ksiązka: {b.title}, wydawca {b.publisher}")  # <__main__.Publisher object at 0x000001ACBBF315B0>
        print(f"Ksiązka: {b.title}, wydawca {b.publisher.name}")  # <__main__.Publisher object at 0x000001ACBBF315B0>
# Author: Adam Mickiewicz
# Ksiązka: Pan Tadeusz, wydawca Wydawnictwo XYZ
# Author: Adam Mickiewicz
# Ksiązka: Pan Tadeusz, wydawca Wydawnictwo XYZ
# Author: Jan kowalski
# Ksiązka: Python średniozaawansowany, wydawca Wydawnictwo ABC
# Author: Jan kowalski
# Ksiązka: Python średniozaawansowany, wydawca Wydawnictwo ABC
# Author: Jan kowalski
# Ksiązka: Python średniozaawansowany, wydawca Wydawnictwo ABC
# Author: Jan kowalski
# Ksiązka: Python średniozaawansowany, wydawca Wydawnictwo ABC
# Author: Jan kowalski
# Ksiązka: Python średniozaawansowany, wydawca Wydawnictwo ABC

publishers = session.query(Publisher).all()

for publisher in publishers:
    print(f"Wydawca: {publisher.name}")
    for book in publisher.books:
        print(f"Ksiązka: {book.title}")
session.close()
