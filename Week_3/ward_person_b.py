# 2b
from abc import ABC, abstractmethod


class Ward:
    def __init__(self, name):
        self.name = name
        self.list_person = []

    def add_person(self, value):
        self.list_person.append(value)

    def describe(self):
        print(f"Ward Nmae: {self.name}")
        for person in self.list_person:
            print(type(person))
            person.describe()


class Person(ABC):
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name} - Yob: {self.yob} - Grade: {self.grade} ")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - Yob: {self.yob} - Specialist: {self.specialist} ")


if __name__ == "__main__":
    student1 = Student(name="studentA", yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    ward1 = Ward(name="Ward1")
    teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1 = Ward(name=" Ward1 ")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()
