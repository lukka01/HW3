class Person:
    def __init__(self, name: str, surname:str, age: int):
        self._name = name
        self._surname = surname
        self._age = age

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_age(self):
        return self._age

class PrinterMixin:
    def student_printer(self):
        print(f"name: {self.get_name()}, surname: {self.get_surname()},"
              f" age: {self.get_age()}, university: {self.get_university()}")


class Student(Person, PrinterMixin):
    def __init__(self, name: str, surname: str, age: int, university: str):
        super().__init__(name,surname, age)
        self._university = university

    def get_university(self):
        return self._university


s1 = Student("Luka", "Khurtsidze", 19, "TSU")
s1.student_printer()














































































































