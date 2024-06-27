class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


if __name__ == "__main__":
    student = Student('John', 22, 700)
    employee = Employee('Peter', 42, 15, 160)

    print(student.show_finance())
    print(employee.show_finance())
    print([student, employee])
    print(repr(student))
    print(employee.__str__() == str(employee))
    print(student.__str__())
