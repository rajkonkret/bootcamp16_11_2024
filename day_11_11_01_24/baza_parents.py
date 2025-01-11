from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)
# engine = create_engine('sqlite:///parents_databes.db', echo=True)
Base = declarative_base()


# 1:N - jeden do wielu
class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))  # maksymalna długośc tekstu
    children = relationship("Child", backref='parent')  # backref - doda pole parent w klasie Child automatycznie
    # przy back_populates musielismy w w klasie Child samodzielnie zdefiniowac to pole z relacją


class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parents.id'))

    def __repr__(self):
        return f"id={self.id}, name={self.name}"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

parent = Parent(name="Rodzic")
child1 = Child(name="Dziecko 1", parent=parent)
child2 = Child(name="Dziecko 2", parent=parent)

# session.add(parent)
# session.add(child1)
# session.add(child2)
session.add_all(
    [parent, child1, child2]
)
session.commit()

our_parent = session.query(Parent).all()
print(our_parent)

our_parent_filtered = session.query(Parent).filter_by(name="Rodzic").first()
print(f"Rodzic: {our_parent_filtered.name}")  # Rodzic: Rodzic
children = our_parent_filtered.children
for child in children:
    print(f"Dziecko: {child.name}")
    print(f"Rodzic: {child.parent.name}")
# Dziecko: Dziecko 1
# Rodzic: Rodzic
# Dziecko: Dziecko 2
# Rodzic: Rodzic
# ilter_by.first
# 2025-01-11 12:57:06,208 INFO sqlalchemy.engine.Engine SELECT parents.id AS parents_id, parents.name AS parents_name
# FROM parents
# WHERE parents.name = ?
#  LIMIT ? OFFSET ?
# parent
# 2025-01-11 12:57:06,213 INFO sqlalchemy.engine.Engine SELECT children.id AS children_id, children.name AS children_name, children.parent_id AS children_parent_id
# FROM children
# WHERE ? = children.parent_id
