

class Student():
    def __init__(self, name, age, ):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Average grade: {self.average_grade()}"


class TopStudent(Student):
    def __init__(self, name, age, scholarship):
        super().__init__(name=name,
                         age=age,)
        self.scholarship = scholarship

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Average grade: {self.average_grade()}, Scholarship Staus: {self.scholarship}"


student1 = Student("Michael", 17)
student1.add_grade(85)
student1.add_grade(94)
student1.add_grade(90)
student1.add_grade(100)
print(student1)

student2 = TopStudent("Con", 18, scholarship=True)
student2.add_grade(95)
student2.add_grade(100)
student2.add_grade(98)
student2.add_grade(96)
print(student2)
