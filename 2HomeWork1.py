class Person:
    def __init__(self, foolname, age, is_married) -> None:
        self.foolname = foolname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"My name is {self.foolname}, I am {self.age} years old.")

class Student(Person):
    def __init__(self, foolname, age, marks):
        super().__init__(foolname, age, is_married=False)
        self.marks = marks

    def Summa(self):
        return sum(self.marks.values())

    def CenterMarks(self):
        total_marks = self.Summa()
        return total_marks / len(self.marks)

class Teacher(Person):
    base_salary = 30000 

    def __init__(self, foolname, age, is_married, experience):
        super().__init__(foolname, age, is_married)
        self.experience = experience
        self.salary = Teacher.base_salary 

    def adjust_salary(self):
        if self.experience >= 3:
            increase_years = self.experience - 2
            self.salary = Teacher.base_salary * (1 + 0.03 * increase_years)

    def get_info(self):
        print(f"Teacher: {self.foolname}, Experience: {self.experience} years, Salary: {self.salary:.2f}")

    @staticmethod
    def create_students():
        students = []  
        student1 = Student('Alihan', 18, {'Math': 98, 'History': 77, 'OOP': 100})
        student2 = Student('Aigerim', 19, {'Math': 85, 'History': 90, 'OOP': 80})
        student3 = Student('Daniyar', 17, {'Math': 75, 'History': 70, 'OOP': 95})

        students.extend([student1, student2, student3])
        return students

teacher = Teacher(foolname="Aitbek", age=35, is_married=True, experience=5)
teacher.adjust_salary()  
teacher.get_info() 

students_list = Teacher.create_students()

for student in students_list:
    print(f"Student: {student.foolname}, Age: {student.age}, Marks: {student.marks}")
    average_marks = student.CenterMarks()
    print(f"Average Mark: {average_marks:.2f}")
