# ORM - Mapowanie obiektowo-relacyjne, to nowoczesne podejście do zagadnienia współpracy z bazą danych
# charakterystyczną cechą jest wykorzystywanie filozofii programowania obiektowego
# zamian obiektów na tabele w bazie danych

# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, declarative_base, aliased

Base = declarative_base()


# klasy odwzorywujące tabele - encje
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age}>"


# Tworzenie połączenia z bazą danych
# echo=True - logowanie zdarzeń bazy danych
engine = create_engine('sqlite:///mydatabase.db', echo=True)  # zwraca silnik
Base.metadata.create_all(engine)  # Tworzy tabele w bazie danych

# utworzenie obiekty sesji za pomocą będziemy łaczyć się z bazą danych
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Jan Kowalski", age=30)
session.add(new_user)
session.commit()
session.close()
# INSERT INTO users (name, age) VALUES (?, ?)
# [generated in 0.00034s] ('Jan Kowalski', 30)

users = session.query(User).all()
# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
for user in users:
    print(user)
    print(f"imie: {user.name} wiek: {user.age}")
# <User(name=Jan Kowalski, age=30>
# <User(name=Jan Kowalski, age=30>
# <User(name=Jan Kowalski, age=30>
# imie: Jan Kowalski wiek: 30
# <User(name=Jan Kowalski, age=30>
# imie: Jan Kowalski wiek: 30
# <User(name=Jan Kowalski, age=30>
# imie: Jan Kowalski wiek: 30

result = session.execute(text("SELECT * FROM users"))
for row in result:
    print(row)
# (1, 'Jan Kowalski', 30)
# (2, 'Jan Kowalski', 30)
# (3, 'Jan Kowalski', 30)
# (4, 'Jan Kowalski', 30)
# (5, 'Jan Kowalski', 30)

# Session = sessionmaker(bind=engine)
# session = Session()

# user_alias = aliased(User)
# select = text("SELECT * FROM users").columns(user_alias)
# result = session.execute(select).scalars()
# for row in result:
#     print(type(row))
#     print(row)
