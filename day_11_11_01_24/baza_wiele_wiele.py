# relacja wiele do wielu N:N
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# definicja tabeli asocjacyjnej
# konieczna w relacji wiele do wielu
# nazwa tabeli: student_course
# będzie miała takie kolumny: student_id, course_id
student_course_table = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    courses = relationship("Course", secondary=student_course_table, back_populates="students")


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    students = relationship("Student", secondary=student_course_table, back_populates="courses")


engine = create_engine('sqlite:///kursy.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

student1 = Student(name="Anna Kowalska")
student2 = Student(name="Jan Nowak")

course1 = Course(title="Programowanie w Pythonie dla zaawansowanych")
course2 = Course(title="Wprowadzenie do SQL")

student1.courses.append(course1)
student1.courses.append(course2)
student2.courses.append(course1)

# session.add(student1)
# session.add(student2)
# session.commit()

our_student = session.query(Student).filter_by(name="Anna Kowalska").first()
print(f"Student: {our_student.name}")  # Student: Anna Kowalska
for course in our_student.courses:
    print(f"Zapisany na kurs: {course.title}")
# Student: Anna Kowalska
# Zapisany na kurs: Programowanie w Pythonie dla zaawansowanych
# Zapisany na kurs: Wprowadzenie do SQL

our_course = session.query(Course).first()
print(our_course.title)
for student in our_course.students:
    print(f"Uczeń: {student.name}")
# Programowanie w Pythonie dla zaawansowanych
# Uczeń: Anna Kowalska
# Uczeń: Jan Nowak
