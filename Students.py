from zoneinfo import reset_tzpath


class Student:
    # I preferred for instance attributes to be private, while it provides more security

    __university = "TSU"

    def __init__ (self, name, grade, age):
        self.__name = name
        self.__grade = grade
        self.__age = age

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def get_age(self):
        return self.__age

    @classmethod
    def get_university(cls):
        return cls.__university

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}, Grade: {self.__grade}"

    @property
    def is_passing(self):
        return self.__grade > 60

    def increase_grade(self, points):
        return self.__grade + points

    def increase_grade(self, points):
        if points > 0:
           self.__grade += points
           return True
        return False







